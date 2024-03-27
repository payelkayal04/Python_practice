"""s = input("Enter a sentence : ")
lst = s.split()
print(lst)
f = input("Enter a word which you want to find: ")
c = 0
for i in lst:
    if i == f:
        c += 1

print("The count is : ", c)
        """

s = input("Enter a sentence : ")
lst = s.split()
f = input("Enter a word which you want to find: ")
dict1 = {}
for i in lst:
    dict1[i] = dict1.get(i, 0) + 1

for k, v in dict1.items():
    if k == f:
        print(f, "Value is ", v)
