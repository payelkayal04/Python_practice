s = input("Enter your string: ")
print(s)
dict1 = {}
for i in s:
    dict1[i] = dict1.get(i, 0) + 1

for k,v in dict1.items():
    print(k,"is present", v, "times")