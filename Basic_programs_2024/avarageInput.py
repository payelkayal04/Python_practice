"""
a = int(input("Enter first number: "))
print(a)
b = int(input("Enter a second number:"))
print(b)
"""

lst = input("Enter the numbers: ").split(',')
print(lst)
s = 0
r = len(lst)
for i in lst:
    s = s+int(i)
print("Sum : ", s)
average = (s/(len(lst)))
print("The average is : ", average)

