"""
str1 = input("Enter a string: ")
str2 = ""
for i in str1:
    str2 = i + str2
print(str2)
"""

s = input("Enter a string: ")
print(''.join(reversed(s)))