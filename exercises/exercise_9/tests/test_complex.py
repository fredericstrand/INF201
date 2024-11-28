from part_1 import Complex

def test_addition():
    z1 = Complex(1, 2)
    z2 = Complex(3, 4)
    r = 5

    assert z1 + z2 == Complex(4, 6), f"Addition failed: {z1} + {z2} != 4 + 6i (got {z1 + z2})"
    assert z1 + r == Complex(6, 2), f"Addition failed: {z1} + {r} != 6 + 2i (got {z1 + r})"
    assert r + z1 == Complex(6, 2), f"Reversed addition failed: {r} + {z1} != 6 + 2i (got {r + z1})"

def test_subtraction():
    z1 = Complex(5, 6)
    z2 = Complex(2, 3)
    r = 4

    assert z1 - z2 == Complex(3, 3), f"Subtraction failed: {z1} - {z2} != 3 + 3i (got {z1 - z2})"
    assert z1 - r == Complex(1, 6), f"Subtraction failed: {z1} - {r} != 1 + 6i (got {z1 - r})"
    assert r - z1 == Complex(-1, -6), f"Reversed subtraction failed: {r} - {z1} != -1 - 6i (got {r - z1})"

def test_multiplication():
    z1 = Complex(2, 3)
    z2 = Complex(1, -4)
    r = 2

    assert z1 * z2 == Complex(14, -5), f"Multiplication failed: {z1} * {z2} != 14 - 5i (got {z1 * z2})"
    assert z1 * r == Complex(4, 6), f"Multiplication failed: {z1} * {r} != 4 + 6i (got {z1 * r})"
    assert r * z1 == Complex(4, 6), f"Reversed multiplication failed: {r} * {z1} != 4 + 6i (got {r * z1})"

def test_equality():
    z1 = Complex(1, 2)
    z2 = Complex(1, 2)
    z3 = Complex(2, 3)
    r = 1

    assert z1 == z2, f"Equality failed: {z1} should be equal to {z2}"
    assert z1 != z3, f"Inequality failed: {z1} should not be equal to {z3}"
    assert z1 != r, f"Inequality failed: {z1} should not be equal to {r}"
    assert Complex(r) == r, f"Equality failed: {Complex(r)} should be equal to {r}"

def test_conjugate():
    z = Complex(3, 4)
    expected = Complex(3, -4)
    assert z.conjugate() == expected, f"Conjugate failed: {z}.conjugate() != {expected} (got {z.conjugate()})"

def test_str_representation():
    assert str(Complex(1, 2)) == "1 + 2i", f"String representation failed: str(Complex(1, 2)) != '1 + 2i'"
    assert str(Complex(1, -2)) == "1 - 2i", f"String representation failed: str(Complex(1, -2)) != '1 - 2i'"
    assert str(Complex(0, 2)) == "0 + 2i", f"String representation failed: str(Complex(0, 2)) != '0 + 2i'"
    assert str(Complex(3, 0)) == "3", f"String representation failed: str(Complex(3, 0)) != '3'"
