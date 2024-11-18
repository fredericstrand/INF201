import numpy as np
from abc import ABC, abstractmethod

class Point:
    def __init__(self, value, index) -> None:
        self._value = value
        self._index = index

class Cell():
    def __init__(self, id, points):
        self._id = id
        self._points = points

    @abstractmethod
    def cell_size(self):
        pass

    @property
    def id(self):
        return self._id

class Line(Cell):
    def __init__(self, id, points):
        super().__init__(id, points)

    def cell_size(self):
        return self._points[1] - self._points[0]

class BoundaryPoint(Cell):
    def __init__(self, id, points):
        super().__init__(id, points)

    def cell_size(self):
        return 0.0

if __name__ == "__main__":
    point_values = np.linspace(0, 1, 100)
    points = []
    for idx, pt in enumerate(point_values):
        points.append(Point(pt, idx))

    cells = []
    for idx, (pt1, pt2) in enumerate(zip(point_values[:-1], point_values[1:])):
        cells.append(Line(idx, [pt1, pt2]))
        
    cells.append(BoundaryPoint(len(cells), point_values[0]))
    cells.append(BoundaryPoint(len(cells), point_values[-1]))

    for c in cells:
        print(f"Cell {c.id}: size is {c.cell_size()}")