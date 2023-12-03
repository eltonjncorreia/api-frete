from dataclasses import dataclass

from src.shipping_service.domain.product.entities import Product
from src.shipping_service.domain.shipping import exceptions

from .enums import ErrorCodes


@dataclass
class ShippingOption:
    """ShippingOption represents the carrier that will calculate shipping"""

    name: str
    shipping_calculation: float
    min_height: int
    max_height: int
    min_width: int
    max_width: int
    delivery_time: int
    min_weight: int = 0

    def is_valid(self, product: Product) -> None:
        self.validate_height(product.dimension.height)
        self.validate_width(product.dimension.width)
        self.validate_weight_greater_zero(product.weight)

    def shipping_cost(self, weight: int) -> float:
        return (weight * self.shipping_calculation) / 10

    def validate_width(self, width: int) -> None:
        if width > self.max_width:
            raise exceptions.WidthCannotBeGreaterThanPermitted(
                ErrorCodes.WIDTH_GREATER.value
            )

        if width < self.min_width:
            raise exceptions.WidthCannotBeLessThanPermitted(ErrorCodes.WIDTH_LESS.value)

    def validate_height(self, height: int) -> None:
        if height > self.max_height:
            raise exceptions.HeightCannotBeGreaterThanPermitted(
                ErrorCodes.HEIGHT_GREATER.value
            )

        if height < self.min_height:
            raise exceptions.HeightCannotBeLessThanPermitted(
                ErrorCodes.HEIGHT_LESS.value
            )

    def validate_weight_greater_zero(self, weight: int) -> None:
        if weight < self.min_weight:
            raise exceptions.WeightCannotLessThanZero(ErrorCodes.WIDTH_LESS.value)


@dataclass
class NinjaDelivery(ShippingOption):
    """Represent the "Ninja Delivery" shipping option"""

    name: str = "Entrega Ninja"
    shipping_calculation: float = 0.3
    min_height: int = 10
    max_height: int = 200
    min_width: int = 6
    max_width: int = 140
    delivery_time: int = 6


@dataclass
class StoreDelivery(ShippingOption):
    """Represent the "Store Delivery" shipping option"""

    name: str = "Entrega KaBuM"
    shipping_calculation: float = 0.2
    min_height: int = 5
    max_height: int = 140
    min_width: int = 13
    max_width: int = 125
    delivery_time: int = 4
