"""
Write a function that takes an array of sorted integers and a key
and returns the index of the first occurance of that key from the array

Example:
    idx     0       1       2       3       4       5       6       7       8       9
    A =   [-14  ,  -10   ,  2   ,  108  ,  108  ,  243  ,  285  ,  285  ,  285  ,  401]
"""

A = [-14, -10, 108, 108, 108, 243, 285, 285, 285, 401]


def find_first_entry(input_list, target):
    high = len(input_list) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        if target < input_list[mid]:
            high = mid - 1
        elif target > input_list[mid]:
            low = mid + 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1


print(find_first_entry(A, 108))
