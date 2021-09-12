#approach: recursion method:

def fibonacci_recursion(n):
    if type(n) != int:
        raise AssertionError("n must be a positive integer")
    elif n <= 0:
        raise AssertionError("n must be a positive integer greater than 0")
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print(fibonacci_recursion(7))
