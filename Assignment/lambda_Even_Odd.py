f = lambda x: 'YES' if x%2 == 0 else 'NO'
print(f(10))
print(f(11))


y = lambda a, b, c : a + b + c
print(y(5, 6, 2))


# def myfunc(n):
# #   return lambda a : a * n
# #
# # mydoubler = myfunc(2)
# #
# # print(mydoubler(11))