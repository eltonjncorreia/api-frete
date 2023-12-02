from dataclasses import dataclass

from src.shipping_service.domain.product.entities import Product, Size


@dataclass
class ShippingCalculationDTO:
    height: int
    width: int
    weight: int

    def to_product(self) -> Product:
        dimension = Size(height=self.height, width=self.width)
        return Product(
            dimension=dimension,
            weight=self.weight
        )
