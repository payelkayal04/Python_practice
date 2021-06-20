data = [1, 4, 6, 7, 8, 9, 12, 14, 16, 19, 26, 30, 35, 37, 40]
target = 4


# linear search

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


print(linear_search(data, target))


# Iterative Binary search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(binary_search_iterative(data, target))


# Recursive binary search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_recursive(data, target, 0, len(data) - 1))
