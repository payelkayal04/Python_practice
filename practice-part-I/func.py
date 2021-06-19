def add_ten(x):
    return x+10

def twice(func,arg):
    return func(func(arg))

print(add_ten(10))
print(twice(add_ten,10))