s = input("Enter a string: ")
print(s)
lst = []
for i in s:
    if i not in lst:
        lst.append(i)

print(''.join(lst))