conact = ["Alice", "Bob", "Charlie", "David"]

find = input("Enter name : ")


def ls(arr, key):
    for i, item in enumerate(arr):
        if item == key:
            return i

    return -1


index = ls(conact, find)

if index != -1:
    print(f"contact found at index :{index}")
else:
    print("Index not found in array")
