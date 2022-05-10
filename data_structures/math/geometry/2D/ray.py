from __future__ import annotations

import copy
import typing

from line import Line

if typing.TYPE_CHECKING:
    from point import Point
    from vector import Vector

class Ray:

    def __init__(self, anchor: Point, director: Point) -> None:
        self.anchor = anchor
        self._director = director

    @property
    def line(self) -> Line:
        return Line(self.anchor, self._director)

    @classmethod
    def from_vector(cls, anchor: Point, vector: Vector) -> Ray:
        point = copy.deepcopy(anchor)
        point.translate(vector)
        return Ray(anchor, point)

    def has_point(self, point: Point) -> bool:
        return self.line.has_point(point)

    def translate(self, vector: Vector) -> None:
        self.anchor.translate(vector)
        self._director.translate(vector)

    def rotate(self, pivot: Point, angle: float) -> None:
        self.anchor.rotate(pivot, angle)
        self._director.rotate(pivot, angle)

    def reflect(self, line: Line) -> None:
        self.anchor.reflect(line)
        self._director.reflect(line)
