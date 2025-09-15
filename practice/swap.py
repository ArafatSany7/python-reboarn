a = input("Enter the first variable(a): ")
b = input("Enter the second variable (b): ")

print(f"Original value of a = {a} and original value of b = {b}")

temp = a
a = b
b = temp

print("Swaped value is a = {a} and b = {b}")
