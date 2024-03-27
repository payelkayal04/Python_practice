def decor(fun):
    def inner():
        result = fun()
        return result * 2

    return inner


# def num():
#     return 5

@decor
def num():
    return 5


#result_fun = decor(num)
#print(result_fun())

print(num())
