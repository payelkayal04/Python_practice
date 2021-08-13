"""
A fixed point is an array "A" and index "i" such that A[i] is equal to "i".

Given a array of "n" distinct intergers sorted in ascending order , write a function that returns
a "fixed point" in the array. If there is a not a fixed point return "None".
"""

# Fixed point is 3
A = [-10, -5, 0, 3, 7]
# Fixed point is 0:
B = [0, 2, 5, 8, 17]
# Fixed point is None:
C = [-10, -5, 3, 4, 7, 9]

def find_fixed_point(input_list):
    if len(input_list) <= 0:
        return "List is empty"
    for i in range(len(input_list)):
        if input_list[i] == i:
            return i

def find_fixed_point_binary(input_list):
    low = 0
    high = len(input_list) - 1
    while low<=high:
        mid = (high+low)//2
        if mid < input_list[mid]:
            high = mid - 1
        elif mid > input_list[mid]:
            low = mid + 1
        else:
            return mid




print(find_fixed_point(A))
print(find_fixed_point(B))
print(find_fixed_point(C))

print(find_fixed_point_binary(A))
print(find_fixed_point_binary(B))
print(find_fixed_point_binary(C))
