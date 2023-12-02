from typing import Any
from typing import Dict
from typing import List

from src.shipping_service.domain.product.entities import Product
from src.shipping_service.domain.shipping.entities import NinjaDelivery
from src.shipping_service.domain.shipping.entities import ShippingOption
from src.shipping_service.domain.shipping.entities import StoreDelivery
from .dtos import ShippingCalculationDTO
from .storage import IShippingStorage


class ShippingService:

    def __init__(self, storage: IShippingStorage) -> None:
        self.storage: IShippingStorage = storage

    def calculate_shipping(self, shipping_calculation_dto: ShippingCalculationDTO) -> List[Dict[str, Any]]:
        shipping_list = []
        ninja_delivery = NinjaDelivery()
        store_delivery = StoreDelivery()

        self.storage.save_shipping(shipping_calculation_dto)

        shipping_aggregate: Product = shipping_calculation_dto.to_product()

        shipping_list = self.response(ninja_delivery, shipping_aggregate, shipping_list)
        shipping_list = self.response(store_delivery, shipping_aggregate, shipping_list)

        return shipping_list

    def response(self, delivery: ShippingOption, aggregate: Product, shipping_list: List) -> List[Dict[str, Any]]:
        try:
            delivery.is_valid(aggregate)
        except Exception:
            pass
        else:
            shipping_json = self.to_json(delivery, aggregate)
            shipping_list.append(shipping_json)

        return shipping_list

    def to_json(self, shipping: ShippingOption, product: Product) -> dict:
        return {
            "name": shipping.name,
            "valor_frete": shipping.shipping_cost(product.weight),
            "prazo_dias": shipping.delivery_time
        }
