import math

a = float(input("Enter coefficient of a : "))
b = float(input("Enter coefficient of b : "))
c = float(input("Enter coefficient of c : "))

discri = b**2 - 4 * a * c

if discri > 0:
    root1 = -b + math.sqrt(discri) / 2 * a
    root2 = -b - math.sqrt(discri) / 2 * a
    print(f"Root1: {root1} ")
    print(f"Root2: {root2} ")

elif discri == 0:
    root = -b / 2 * a
    print(f"Root: {root} ")

else:
    real_part = -b / 2 * a
    imig_part = math.sqrt(abs(discri) / 2 * a)
    print(f"Root1 = {real_part} + {imig_part}i")
    print(f"Root2 = {real_part} + {imig_part}i")
