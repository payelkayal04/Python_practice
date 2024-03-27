def myFun(x, *args, **kwargs):  #positional arguments and Keyword arguments
    for each_arg in args:
        print(each_arg)
    for key, value in kwargs.items():
        print(key, value)


myFun(20, 10, 40, 30, name="= payel", age="= 30")
