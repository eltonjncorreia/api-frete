from src.shipping_service.usecases.shipping.dtos import ShippingCalculationDTO
from src.shipping_service.usecases.shipping.services import ShippingService


def test_calculate_shipping() -> None:
    dto = ShippingCalculationDTO(height=102, width=40, weight=400)
    shipping_service = ShippingService()
    response = shipping_service.calculate_shipping(dto)

    assert response == [
        {'name': 'Entrega Ninja', 'prazo_dias': 6, 'valor_frete': 12.0},
        {'name': 'Entrega KaBuM', 'prazo_dias': 4, 'valor_frete': 8.0}
    ]


def test_calculate_shipping_should_return_ninja_delivery() -> None:
    dto = ShippingCalculationDTO(height=152, width=50, weight=850)
    shipping_service = ShippingService()
    response = shipping_service.calculate_shipping(dto)

    assert response == [
        {'name': 'Entrega Ninja', 'prazo_dias': 6, 'valor_frete': 12.0},
    ]


def test_calculate_shipping_should_return_empty_list() -> None:
    dto = ShippingCalculationDTO(height=230, width=162, weight=400)
    shipping_service = ShippingService()
    response = shipping_service.calculate_shipping(dto)

    assert response == list()
