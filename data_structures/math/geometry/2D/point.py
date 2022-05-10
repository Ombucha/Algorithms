from __future__ import annotations

import typing
import sympy

if typing.TYPE_CHECKING:
    from line import Line
    from vector import Vector

class Point:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def distance(self, point: Point) -> float:
        distance = sympy.sqrt((point.x_coordinate - self.x_coordinate) ** 2 + (point.y_coordinate - self.y_coordinate) ** 2)
        return distance

    def translate(self, vector: Vector) -> None:
        self.x_coordinate += vector.components[0]
        self.y_coordinate += vector.components[1]

    def rotate(self, pivot: Point, angle: float) -> None:
        x_coordinate = float(pivot.x_coordinate + sympy.cos(0 - angle) * (self.x_coordinate - pivot.x_coordinate) - sympy.sin(0 - angle) * (self.y_coordinate - pivot.y_coordinate))
        y_coordinate = float(pivot.y_coordinate + sympy.sin(0 - angle) * (self.x_coordinate - pivot.x_coordinate) + sympy.cos(0 - angle) * (self.y_coordinate - pivot.y_coordinate))
        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate

    def reflect(self, line: Line) -> None:
        try:
            self.x_coordinate = (self.x_coordinate * (1 - line.slope ** 2) + 2 * line.slope * (self.y_coordinate - line.y_intercept.y_coordinate)) / (1 + line.slope ** 2)
            self.y_coordinate = (self.y_coordinate * (line.slope ** 2 - 1) - 2 * line.slope * (line.slope * self.x_coordinate - line.y_intercept.y_coordinate)) / (1 + line.slope ** 2)
        except ZeroDivisionError:
            self.x_coordinate = 0 - self.x_coordinate
