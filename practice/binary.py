def bs(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [2, 4, 6, 7, 8, 9, 12, 15, 17, 19, 34, 37, 50]
target = int(input("Enter Target : "))

result = bs(arr, target)
if result != -1:
    print(f"Element found at index : {result} and target value is {target}")
else:
    print("Index not found")
