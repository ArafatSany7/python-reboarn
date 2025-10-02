num = int(input("Enter a number : "))
facto = 1

if num < 0:
    print("Factorial does not exists for your negetive number : ")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        facto = facto * i
    print(f"The factorial of number {num} is {facto}")
