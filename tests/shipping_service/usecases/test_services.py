from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO
from src.shipping_service.usecases.shipping.services import ShippingService
from src.shipping_service.usecases.shipping.storage import IShippingStorage
from src.shipping_service.usecases.product.dtos import ProductDTO


class DummyStorage(IShippingStorage):
    def save_shipping(self, shipping_calculation_dto: ShippingCalculationDTO):
        return True

class TestShippingService:

    def test_calculate_shipping(self) -> None:
        dto = ProductDTO(height=102, width=40, weight=400)
        shipping_service = ShippingService(DummyStorage())
        response = shipping_service.calculate_shipping(dto)

        assert response == [
            {'nome': 'Entrega Ninja', 'prazo_dias': 6, 'valor_frete': 12.0},
            {'nome': 'Entrega KaBuM', 'prazo_dias': 4, 'valor_frete': 8.0}
        ]


    def test_calculate_shipping_should_return_ninja_delivery(self) -> None:
        dto = ProductDTO(height=152, width=50, weight=850)
        shipping_service = ShippingService(DummyStorage())
        response = shipping_service.calculate_shipping(dto)

        assert response == [
            {'nome': 'Entrega Ninja', 'prazo_dias': 6, 'valor_frete': 25.5},
        ]


    def test_calculate_shipping_should_return_empty_list(self) -> None:
        dto = ProductDTO(height=230, width=162, weight=400)
        shipping_service = ShippingService(DummyStorage())
        response = shipping_service.calculate_shipping(dto)

        assert response == list()
