"""
Given two numbers, find their product using recursion
"""

x = 5
y = 3

def product_iterative(a,b):
    return a*b

print(product_iterative(x,y))

def product_recursion(a,b):
    if b == 0:
        return 0
    return x+product_recursion(a,b-1)
print(product_recursion(x,y))