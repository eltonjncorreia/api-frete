from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db: SQLAlchemy = SQLAlchemy(model_class=Base)


class Product(db.Model):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    height: Mapped[str] = mapped_column(String, nullable=False)
    width: Mapped[str] = mapped_column(String, nullable=False)
    weight: Mapped[str] = mapped_column(String)


class ShippingCalculate(db.Model):
    __tablename__ = "shipping_calculate"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[str] = mapped_column(String)
    delivery_time: Mapped[str] = mapped_column(String)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship()
