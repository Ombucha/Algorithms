from __future__ import annotations

import typing
import sympy

if typing.TYPE_CHECKING:
    from circle import Circle
    from point import Point

class Arc:

    def __init__(self, circle: Circle, point_1: Point, point_2: Point) -> None:
        self.circle = circle
        self.point_1 = point_1
        self.point_2 = point_2

    @property
    def central_angle(self) -> float:
        distance = self.point_1.distance(self.point_2)
        angle = float(sympy.acos((distance ** 2 - 2 * (self.circle.radius ** 2)) / (2 * (self.circle.radius ** 2))))
        return angle

    @property
    def length(self) -> float:
        return self.circle.radius * self.central_angle
