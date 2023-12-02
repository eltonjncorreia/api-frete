from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Product(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[str] = mapped_column(String, nullable=False)
    width: Mapped[str] = mapped_column(String, nullable=False)
    weight: Mapped[str] = mapped_column(String)


class ShippingCalculate(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[str] = mapped_column(String)
    delivery_time: Mapped[str] = mapped_column(String)
