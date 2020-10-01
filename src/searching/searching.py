def linear_search(arr, target):
    # Your code here
    index = 0
    for i in arr:

        if i == target:

            return index
        index += 1

    return -1
    # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            high = middle - 1
        else:
            low = middle + 1

    # Your code here

    return -1  # not found
