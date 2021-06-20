print("Enter the value of n: ")
n = int(input())
print("Enter the value of sum: ")
s = int(input())
lst = []
for i in range(0, n):
    print("Enter the array elements: ")
    ele = int(input())
    lst.append(ele)
print(lst)


def count_pairs(n, s, lst):
    count = 0
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == s:
                count += 1
    return count


print(count_pairs(n, s, lst))
