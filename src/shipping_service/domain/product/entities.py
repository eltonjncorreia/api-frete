from dataclasses import dataclass


@dataclass
class Size:
    height: int
    width: int


@dataclass
class Product:
    dimension: Size
    weight: int
