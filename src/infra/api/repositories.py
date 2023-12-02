from src.shipping_service.usecases.shipping.storage import IShippingStorage
from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO


class ShippingRepository(IShippingStorage):

    def save_shipping(self, shipping_dto: ShippingCalculationDTO):
        pass
