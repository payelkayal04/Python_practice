"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
Example 2:
Input: [1,3,5,6], 2
Output: 1
Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 4:
Input: [1,3,5,6], 0
Output: 0
"""

nums = [1, 3, 5, 6, 8, 9]
target = 4


def serach_insert(nums, target):
    low = 0
    high = len(nums) - 1
    print("low: {}, high: {}".format(low, high))
    while (low <= high):
        mid = (low + high) // 2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            high = mid - 1
        else:
            low = mid + 1
    print("nums[high]: {}, high: {}".format(nums[high], high))
    print(low)
    if (nums[high] < target):
        return high + 1
    elif (nums[low] >= target):
        return low+1
    else:
        return high


print(serach_insert(nums, target))
