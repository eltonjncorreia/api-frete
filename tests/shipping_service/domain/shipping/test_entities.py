import pytest

from src.shipping_service.domain.product.entities import Product, Size
from src.shipping_service.domain.shipping import exceptions
from src.shipping_service.domain.shipping.entities import NinjaDelivery, StoreDelivery
from src.shipping_service.domain.shipping.enums import ErrorCodes


class TestNinjaDelivery:
    def test_ninja_delivery_has_default_values(self) -> None:
        delivery = NinjaDelivery()
        assert delivery.name == "Entrega Ninja"
        assert delivery.shipping_calculation == 0.3
        assert delivery.min_height == 10
        assert delivery.max_height == 200
        assert delivery.min_width == 6
        assert delivery.max_width == 140
        assert delivery.delivery_time == 6
        assert delivery.min_weight == 0

    def test_height_cannot_be_greater_than_permitted(self) -> None:
        dimension = Size(height=201, width=40)
        product = Product(dimension=dimension, weight=400)

        delivery = NinjaDelivery()
        with pytest.raises(exceptions.HeightCannotBeGreaterThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.HEIGHT_GREATER.value == ex.value.args[0]

    def test_height_cannot_be_less_than_permitted(self) -> None:
        dimension = Size(height=0, width=40)
        product = Product(dimension=dimension, weight=400)

        delivery = NinjaDelivery()
        with pytest.raises(exceptions.HeightCannotBeLessThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.HEIGHT_LESS.value == ex.value.args[0]

    def test_width_cannot_be_greater_than_permitted(self) -> None:
        dimension = Size(height=200, width=200)
        product = Product(dimension=dimension, weight=400)

        delivery = NinjaDelivery()
        with pytest.raises(exceptions.WidthCannotBeGreaterThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_GREATER.value == ex.value.args[0]

    def test_width_cannot_be_less_than_permitted(self) -> None:
        dimension = Size(height=150, width=0)
        product = Product(dimension=dimension, weight=400)

        delivery = NinjaDelivery()
        with pytest.raises(exceptions.WidthCannotBeLessThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_LESS.value == ex.value.args[0]

    def test_weight_cannot_less_than_zero(self) -> None:
        dimension = Size(height=150, width=10)
        product = Product(dimension=dimension, weight=-1)

        delivery = NinjaDelivery()
        with pytest.raises(exceptions.WeightCannotLessThanZero) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_LESS.value == ex.value.args[0]


class TestStoreDelivery:
    def test_store_delivery_has_default_values(self) -> None:
        delivery = StoreDelivery()
        assert delivery.name == "Entrega KaBuM"
        assert delivery.shipping_calculation == 0.2
        assert delivery.min_height == 5
        assert delivery.max_height == 140
        assert delivery.min_width == 13
        assert delivery.max_width == 125
        assert delivery.delivery_time == 4
        assert delivery.min_weight == 0

    def test_height_cannot_be_greater_than_permitted(self) -> None:
        product = Product(dimension=Size(height=201, width=40), weight=400)

        delivery = StoreDelivery()
        with pytest.raises(exceptions.HeightCannotBeGreaterThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.HEIGHT_GREATER.value == ex.value.args[0]

    def test_height_cannot_be_less_than_permitted(self) -> None:
        product = Product(dimension=Size(height=0, width=40), weight=400)

        delivery = StoreDelivery()
        with pytest.raises(exceptions.HeightCannotBeLessThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.HEIGHT_LESS.value == ex.value.args[0]

    def test_width_cannot_be_greater_than_permitted(self) -> None:
        product = Product(dimension=Size(height=140, width=200), weight=400)

        delivery = StoreDelivery()
        with pytest.raises(exceptions.WidthCannotBeGreaterThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_GREATER.value == ex.value.args[0]

    def test_width_cannot_be_less_than_permitted(self) -> None:
        product = Product(dimension=Size(height=140, width=0), weight=400)

        delivery = StoreDelivery()
        with pytest.raises(exceptions.WidthCannotBeLessThanPermitted) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_LESS.value == ex.value.args[0]

    def test_weight_cannot_less_than_zero(self) -> None:
        product = Product(dimension=Size(height=140, width=13), weight=-1)

        delivery = StoreDelivery()
        with pytest.raises(exceptions.WeightCannotLessThanZero) as ex:
            delivery.is_valid(product)

        assert ErrorCodes.WIDTH_LESS.value == ex.value.args[0]
