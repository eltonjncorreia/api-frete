from src.infra.databases.db import ShippingCalculate, db, Product
from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO
from src.shipping_service.usecases.shipping.storage import IShippingStorage


class ShippingRepository(IShippingStorage):

    def save_shipping(self, shipping_dto: ShippingCalculationDTO):
        product = Product(
            height=shipping_dto.product.dimension.height,
            width=shipping_dto.product.dimension.width,
            weight=shipping_dto.product.weight
        )
        db.session.add(product)
        db.session.flush()

        shipping = ShippingCalculate(
            delivery_time=shipping_dto.delivery_time,
            price=shipping_dto.price,
            name=shipping_dto.name,
            product=product
        )
        db.session.add(shipping)
        db.session.commit()
