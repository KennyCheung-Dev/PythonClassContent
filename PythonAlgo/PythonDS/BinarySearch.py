def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1

num = [1, 1, 2, 3, 5, 8, 13]
print(binary_search(num, 0, len(num) - 1, -5))