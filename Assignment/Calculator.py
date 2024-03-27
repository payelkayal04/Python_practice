def calculator(n, m):
    f = input("Enter your choice of operation: ").lower()
    if f == "sum":
        return n + m
    elif f == "sub":
        return n - m
    elif f == "mul":
        return n * m
    elif f == "div":
        return n / m
    else:
        print("Incorrect Input")


x = int(input("Enter first number: "))
y = int(input("Enter second number :"))
print(calculator(x, y))
