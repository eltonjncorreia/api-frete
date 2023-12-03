from dataclasses import dataclass

from src.shipping_service.domain.product.entities import Product


@dataclass
class ShippingCalculationDTO:
    name: str
    price: float
    delivery_time: int
    product: Product
