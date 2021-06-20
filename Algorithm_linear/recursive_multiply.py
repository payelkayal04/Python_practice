x = 500
y = 2000


def recursive_multiply(x, y):
    if y == 0:
        return 0
    if x < y:
        return y + recursive_multiply(y, x - 1)
    else:
        return x + recursive_multiply(x, y - 1)


print(recursive_multiply(x, y))
