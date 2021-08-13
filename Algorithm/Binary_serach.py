"""

"""

data = [2,4,5,7,8,9,12,22,25,27,28,33,37]
target = 1

#Linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return "The {} target value found at index {}".format(target, i)
    return "Not found"



print(linear_search(data,target))

#Iterative Binary serach
def binary_search_iterative(data,target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

print(binary_search_iterative(data,target))


def binary_search_recursive(data,target,low,high):
    if low>high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data,target,low-1,high)
        else:
            return binary_search_recursive(data,target,low,high+1)

print(binary_search_recursive(data,target,0,len(data)-1))