"""
Define a bitonic sequence as sequence of integers such data:
x_1 <= .... <= x_k >= ...>=x_n-1 for some k, 0 <= k <n

For example:
1, 2, 3, 4, 5, 4, 3, 2, 1

is a bitoic sequence. write a program to find the largest element in such asequence.
In the above example , the program should return "5".

We assume that such a peak element exist
"""

# Peak element is 5
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is "4"
B = [1, 2, 3, 4, 1]

# Peak element is "6"
C = [1, 6, 5, 4, 3, 2, 1]

def find_pick_element(input_list):
    for i in range(len(input_list)-1):
        if input_list[i+1]<input_list[i]:
            return input_list[i]

def find_pic_element_binary(input_list):
    high = len(input_list) -1
    low = 0

    # Require atleast three elements
    if len(input_list)<3:
        return False

    while low <= high:
        mid = (high+low)//2

        mid_left = input_list[mid-1] if mid -1 > 0 else float("-inf")
        mid_right = input_list[mid+1] if mid+1<len(input_list) else float("inf")

        if mid_left < input_list[mid] and mid_right > input_list[mid]:
             low = mid +1
        elif mid_left > input_list[mid] and mid_right <input_list[mid]:
           high = mid -1
        elif mid_left<input_list[mid] and mid_right<input_list[mid]:
            return input_list[mid]





# print(find_pick_element(A))
# print(find_pick_element(B))
# print(find_pick_element(C))

print(find_pic_element_binary(A))
print(find_pic_element_binary(B))
print(find_pic_element_binary(C))
