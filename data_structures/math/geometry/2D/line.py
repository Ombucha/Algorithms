from __future__ import annotations

import typing
import sympy

from point import Point

if typing.TYPE_CHECKING:
    from vector import Vector

class Line:

    def __init__(self, point_1: Point, point_2: Point) -> None:
        self._point_1 = point_1
        self._point_2 = point_2

    @property
    def slope(self) -> float:
        gradient = (self._point_2.y_coordinate - self._point_1.y_coordinate) / (self._point_2.x_coordinate - self._point_1.x_coordinate)
        return gradient

    @property
    def x_intercept(self) -> Point:
        intercept = Point(0, (0 - self.y_intercept) / self.slope)
        return intercept

    @property
    def y_intercept(self) -> Point:
        intercept = Point(0, self._point_1.y_coordinate - self.slope * self._point_1.x_coordinate)
        return intercept

    @classmethod
    def from_slope(cls, slope: float, point: Point) -> Line:
        y_intercept = point.y_coordinate - slope * point.x_coordinate
        _point = Point((0 - y_intercept) / slope, 0)
        return Line(point, _point)

    def has_point(self, point: Point) -> bool:
        if point.y_coordinate == self.slope * point.x_coordinate + self.y_intercept:
            return True
        return False

    def perpendicular(self, point: Point) -> Line:
        return self.from_slope((0 - self.slope), point)

    def distance_from(self, point: Point) -> float:
        distance = ((0 - self.slope) * point.x_coordinate + point.y_coordinate - self.y_intercept.y_coordinate) / (float(sympy.sqrt((0 - self.slope)) ** 2 + 1))
        return distance

    def parallel(self, point: Point) -> Line:
        return self.from_slope(self.slope, point)

    def translate(self, vector: Vector) -> None:
        self._point_1.translate(vector)
        self._point_2.translate(vector)

    def rotate(self, pivot: Point, angle: float) -> None:
        self._point_1.rotate(pivot, angle)
        self._point_2.rotate(pivot, angle)    

    def reflect(self, line: Line) -> None:
        self._point_1.reflect(line)
        self._point_2.reflect(line)
