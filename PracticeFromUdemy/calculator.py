def calculator(n, m):
    # f = input("Enter your choice of operation: ").lower()
    while True:
        try:
            f = input("Enter your choice of operation: ").lower()
            if f == "sum":
                print(n + m)
                break
            elif f == "sub":
                print(n - m)
                break
            elif f == "mul":
                print(n * m)
                break
            elif f == "div":
                print(n / m)
                break
            else:
                print("Incorrect Input")
        except ValueError:
            print("Enter correct operation: ")
            continue


x = int(input("Enter first number: "))
y = int(input("Enter second number :"))
calculator(x, y)
