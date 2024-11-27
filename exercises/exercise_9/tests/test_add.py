import pytest
from warm_up import Vector2D

def test_add():
    a = Vector2D(1.0, 2.0)
    b = Vector2D(4.0, 4.0)
    c = a + b
    assert c._x == a._x + b._x
    assert c._y == a._y + b._y