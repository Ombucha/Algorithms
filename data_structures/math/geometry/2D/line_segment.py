from __future__ import annotations

import typing
import sympy

from point import Point
from line import Line

if typing.TYPE_CHECKING:
    from vector import Vector

class LineSegment:

    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def __iter__(self) -> typing.Iterator[float]:
        for item in (self.point_1, self.point_2):
            yield item

    @property
    def length(self) -> float:
        return self.point_1.distance(self.point_2)

    @property
    def points(self) -> tuple[float]:
        return (self.point_1, self.point_2)

    @property
    def midpoint(self) -> Point:
        coordinates = ((self.point_1.x_coordinate + self.point_2.x_coordinate) / 2, (self.point_1.y_coordinate + self.point_1.y_coordinate) / 2)
        return Point(*coordinates)

    @property
    def line(self) -> Line:
        return Line(self.point_1, self.point_2)

    def perpendicular(self, point: Point) -> Line:
        return Line.from_slope((0 - self.line.slope), point)

    def has_point(self, point: Point) -> bool:
        if LineSegment(self.point_1, point).length + LineSegment(self.point_2, point).length == self.length:
            return True
        return False

    def distance_from(self, point: Point) -> float:
        distance = ((0 - self.line.slope) * point.x_coordinate + point.y_coordinate - self.line.y_intercept.y_coordinate) / (float(sympy.sqrt((0 - self.line.slope)) ** 2 + 1))
        return distance

    def translate(self, vector: Vector) -> None:
        self.point_1.translate(vector)
        self.point_2.translate(vector)

    def rotate(self, pivot: Point, angle: float) -> None:
        self.point_1.rotate(pivot, angle)
        self.point_2.rotate(pivot, angle) 

    def reflect(self, line: Line) -> None:
        self.point_1.reflect(line)
        self.point_2.reflect(line)
