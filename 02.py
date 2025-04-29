def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    moves = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
            moves += 1

        elif arr[mid] > x:
            high = mid - 1
            moves += 1

        else:
            return (moves, mid)

    return -1

if __name__ == "__main__":
    arr = [2.4, 3.6, 4.9, 10.1, 10.11, 10.112, 40.1]
    x = 10.11
    # arr = [2, 3, 4.9, 10, 10, 10, 10, 40]
    # x = 3
    step, result = binary_search(arr, x)
    if result != -1:
        print(f"On step {step}, element was found at index {result}")
    else:
        print("Element is not present in array")
