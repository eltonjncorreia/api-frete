from typing import Any
from typing import Dict
from typing import List

from src.shipping_service.domain.product.entities import Product
from src.shipping_service.domain.shipping.entities import NinjaDelivery
from src.shipping_service.domain.shipping.entities import ShippingOption
from src.shipping_service.domain.shipping.entities import StoreDelivery
from .dtos import ShippingCalculationDTO


class ShippingService:

    def calculate_shipping(self, shipping_calculation_dto: ShippingCalculationDTO) -> List[Dict[str, Any]]:
        shipping_list = []
        ninja_delivery = NinjaDelivery()
        store_delivery = StoreDelivery()
        product = shipping_calculation_dto.to_product()

        try:
            ninja_delivery.is_valid(product)
        except Exception:
            pass
        else:
            shipping_json = self.to_json(ninja_delivery, product)
            shipping_list.append(shipping_json)

        try:
            store_delivery.is_valid(product)
        except Exception:
            pass
        else:
            shipping_json = self.to_json(store_delivery, product)
            shipping_list.append(shipping_json)

        return shipping_list

    def to_json(self, shipping: ShippingOption, product: Product) -> dict:
        return {
            "name": shipping.name,
            "valor_frete": shipping.shipping_cost(product.weight),
            "prazo_dias": shipping.delivery_time
        }
