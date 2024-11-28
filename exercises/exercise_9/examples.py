import random
from part_1 import Complex

def random_complex():
    real = random.randint(-10, 10)
    imag = random.randint(-10, 10)
    
    return Complex(real, imag)

z1 = random_complex()
z2 = random_complex()

r1 = random.randint(-10, 10)
r2 = random.randint(-10, 10)

print("-"*60,"\n")
print(f"Addition object test (z1 + z2): {z1 + z2}")
print(f"Addition int test (z1 + r1): {z1 + r1} \n")

print("-"*60,"\n")
print(f"Subraction object test (z1 - z2): {z1 - z2}")
print(f"Subraction int test (z1 - r1): {z1 - r1} \n")

print("-"*60,"\n")
print(f"Multiplication object test (z1 * z2): {z1 * z2}")
print(f"Multiplication int test (z1 * r1): {z1 * r1} \n")

print("-"*60,"\n")
print("Other tests")
print(f"z1 == z2: {z1 == z2}")
print(f"z1 != z2: {z1 != z2}")
print(f"Conjugate of z1: {z1.conjugate()}")