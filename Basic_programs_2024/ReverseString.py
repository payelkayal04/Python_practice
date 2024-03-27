# str1 = input("Enter your string : ")
# print(str1)
# str2 = str1[len(str1)::-1]
# print(str2)


def revStr(str1):
    s = " "
    for i in str1:
        s = i + s
    return s


str2 = input("Enter your string : ")
print(revStr(str2))
