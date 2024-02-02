'''

s = input()
print(s)
s = input("Enter your name:")
print(s)
'''

'''
a = int(input("Enter a number"))
b = int(input("Enter a another number"))
print("Sum is ", a+b)
'''

lst = [int(x) for x in input("Enter three numbers separated by comma:").split(',')]
print(lst)
print(lst[1])
s = 0
for i in range(len(lst)):
   s = s + lst[i]
print("Sum is : ",s)
