from __future__ import annotations

import typing
import sympy

from arc import Arc
from sector import Sector
from segment import Segment

if typing.TYPE_CHECKING:
    from point import Point

class Circle:

    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    @property
    def diameter(self) -> float:
        return self.radius * 2

    @property
    def area(self) -> float:
        return float(sympy.pi * (self.radius ** 2))

    @property
    def circumference(self) -> float:
        return float(2 * sympy.pi * self.radius)

    def get_arc(self, point_1: Point, point_2: Point) -> Arc:
        return Arc(self, point_1, point_2)

    def get_sector(self, point_1: Point, point_2: Point) -> Sector:
        return Sector(self, point_1, point_2)

    def get_segment(self, point_1: Point, point_2: Point) -> Segment:
        return Segment(self, point_1, point_2)

    def has_point(self, point: Point):
        if (point.x_coordinate - self.center.x_coordinate) ** 2 + (point.y_coordinate - self.center.y_coordinate) ** 2 == self.radius ** 2:
            return True
        return False
