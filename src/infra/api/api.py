import os

from flask import Flask, jsonify

from src.infra.databases.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/postgres")
db.init_app(app)

with app.app_context():
    db.create_all()
