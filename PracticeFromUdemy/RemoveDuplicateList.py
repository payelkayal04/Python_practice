lst = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)

