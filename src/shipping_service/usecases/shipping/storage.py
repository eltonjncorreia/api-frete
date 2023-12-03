from abc import ABC, abstractmethod

from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO


class IShippingStorage(ABC):
    @abstractmethod
    def save_shipping(self, shipping_dto: ShippingCalculationDTO):
        raise NotImplementedError
