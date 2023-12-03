import pytest

from src.infra.api.api import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_should_return_success_when_calculate_shipping(client) -> None:
    json: dict = {
        "dimensao": {
            "altura": 102,
            "largura": 40
        },
        "peso": 400
    }
    response = client.post("/calcular-frete", json=json)

    assert response.json == [
        {"nome": "Entrega Ninja", "prazo_dias": 6, "valor_frete": 12.0},
        {"nome": "Entrega KaBuM", "prazo_dias": 4, "valor_frete": 8.0}
    ]


def test_should_return_ninja_delivery(client) -> None:
    json: dict = {
        "dimensao": {
            "altura": 152,
            "largura": 50
        },
        "peso": 850
    }
    response = client.post("/calcular-frete", json=json)

    assert response.json == [
        {
            "nome": "Entrega Ninja",
            "valor_frete": 25.50,
            "prazo_dias": 6
        }
    ]


def test_should_return_bad_request(client) -> None:
    invalid_json: dict = dict()
    response = client.post("/calcular-frete", json=invalid_json)
    assert response.json == {'error': 'requisição mal formatada'}
    assert response.status_code == 400
