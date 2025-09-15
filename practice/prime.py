num = int(input("Enter a number : "))
flag = False

if num == 1 or num == 0:
    print(f"{num} is not prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

if flag:
    print(f"{num} Number is not prime")
else:
    print(f"{num} Number is prime")
