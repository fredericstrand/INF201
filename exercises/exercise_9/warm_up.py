class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y)
