from abc import ABC
from abc import abstractmethod
from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO


class IShippingStorage(ABC):

    @classmethod
    @abstractmethod
    def save_shipping(cls, shipping_calculation_dto: ShippingCalculationDTO):
        raise NotImplemented
