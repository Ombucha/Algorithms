from __future__ import annotations

import sympy

class Vector:

    def __init__(self, magnitude: float, direction: float) -> int:
        self.magnitude = magnitude
        self.direction = direction

    @property
    def components(self):
        vector = (float(sympy.cos(self.direction) * self.magnitude), float(sympy.sin(self.direction) * self.magnitude))
        return vector

    @classmethod
    def from_components(cls, components: tuple[float]):
        vector = Vector(float(sympy.sqrt(components[0] ** 2 + components[1] ** 2)),  float(sympy.atan(components[1] / components[0])))
        return vector

    @classmethod
    def dot_product(cls, vector_1: Vector, vector_2: Vector) -> float:
        product = vector_1.components[0] * vector_2.components[0] + vector_1.components[1] * vector_2.components[1]
        return product
