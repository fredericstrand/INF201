import pytest
from simple_mesh import Line
import numpy as np

@pytest.fixture
def cells():
    point_values = np.linspace(0, 1, 10)
    cells = []
    
def test_id_positive():
    l = Line(1, [0, 1])
    assert l.id >= 0, f"Line ID is {l.id}, but needs to be positive"

def test_id_matches():
    l = Line(1, [0, 1])
    assert l._id == 1, f"Line ID has wrong id of {l.id}, but should be 1"

def test_getter():
    l = Line(1, [0, 1])
    l._id = 1
    assert l.id == 1, f"Line ID has wrong id of {l.id}, but should be 1"