"""
Write a function that takes a non-negative integer and returns the largest integer whose square
is less than or equal to the integer given.

Example:
    Assume input is integer 300

    Then the expected output of the function should be 17,
    since 17^2 = 289 < 300. Note that 18^2 = 324 >300,
    So the number 17 is the correct response.
"""

input_num = 300


def int_square_root(num):
    for i in range(num):
        if i * i > 300:
            return i - 1


print(int_square_root(input_num))

def in_square_root_binary(num):
    low = 0
    high = num

    while low<=high:
        mid = (high+low)//2
        mid_square = mid*mid
        if mid_square <= num:
            low = mid+1
        else:
            high = mid - 1
    return low - 1
print(in_square_root_binary(input_num))

