import os

from flask import Flask, jsonify, request
from werkzeug.http import HTTP_STATUS_CODES

from src.infra.databases.db import db
from src.shipping_service.usecases.product.dtos import ProductDTO
from src.shipping_service.usecases.shipping.services import ShippingService
from src.infra.api.repositories import ShippingRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/postgres")
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/calcular-frete', methods=["POST"])
def calculate_shipping():
    data = request.get_json()

    altura = data.get('dimensao', {}).get('altura')
    largura = data.get('dimensao', {}).get('largura')
    peso = data.get('peso')

    if not altura or not largura or not peso:
        return jsonify({'error': 'requisição mal formatada'}), 400

    dto = ProductDTO(height=altura, width=largura, weight=peso)
    service = ShippingService(storage=ShippingRepository())
    response = service.calculate_shipping(dto)

    return jsonify(response)