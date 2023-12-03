from typing import Any
from typing import Dict
from typing import List

from src.shipping_service.domain.product.entities import Product
from src.shipping_service.domain.shipping.entities import NinjaDelivery
from src.shipping_service.domain.shipping.entities import ShippingOption
from src.shipping_service.domain.shipping.entities import StoreDelivery
from src.shipping_service.usecases.product.dtos import ProductDTO
from .dtos import ShippingCalculationDTO
from .storage import IShippingStorage


class ShippingService:

    def __init__(self, storage: IShippingStorage) -> None:
        self.storage: IShippingStorage = storage

    def calculate_shipping(self, product_dto: ProductDTO) -> List[Dict[str, Any]]:
        shipping_list = []

        ninja_delivery = NinjaDelivery()
        store_delivery = StoreDelivery()

        product: Product = product_dto.to_product()

        self.add_shipping_list(ninja_delivery, product, shipping_list)
        self.add_shipping_list(store_delivery, product, shipping_list)

        return shipping_list

    def add_shipping_list(self, delivery: ShippingOption, product: Product, shipping_list: List) -> None:
        try:
            delivery.is_valid(product)
        except Exception:
            pass
        else:
            shipping_json = self.to_json(delivery, product)
            shipping_list.append(shipping_json)
            shipping_dto = ShippingCalculationDTO(
                name=shipping_json["nome"],
                price=shipping_json["valor_frete"],
                delivery_time=shipping_json["prazo_dias"],
                product=product
            )
            self.storage.save_shipping(shipping_dto)

    def to_json(self, shipping: ShippingOption, product: Product) -> dict:
        return {
            "nome": shipping.name,
            "valor_frete": shipping.shipping_cost(product.weight),
            "prazo_dias": shipping.delivery_time
        }
