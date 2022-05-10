from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from point import Point
    from line import Line
    from vector import Vector

class Polygon:

    def __init__(self, *points: Point) -> None:
        self.points = points

    @property
    def area(self) -> float:
        length = len(self.points)
        x_coordinates, y_coordinates = [point.x_coordinate for point in self.points], [point.y_coordinate for point in self.points]
        total = lambda list_1, list_2: sum([list_1[index] * list_2[index + 1] for index in range(length - 1)]) + list_1[length - 1] * list_2[0]
        area = 0.5 * abs(total(x_coordinates, y_coordinates) - total(y_coordinates, x_coordinates))
        return area

    @property
    def perimeter(self) -> float:
        total = 0
        for index in range(len(self.points) - 1):
            total += self.points[index].distance(self.points[index + 1])

    def translate(self, vector: Vector) -> None:
        for index, _ in enumerate(self.points):
            self.points[index].translate(vector)

    def rotate(self, pivot: Point, angle: float) -> None:
        for index, _ in enumerate(self.points):
            self.points[index].rotate(pivot, angle)

    def reflect(self, line: Line) -> None:
        for index, _ in enumerate(self.points):
            self.points[index].reflect(line)
