def myFun(x, *pos_param, **key_param):
    print(x)
    key_param['id'] = 123
    for each_pos_param in pos_param:
        print(each_pos_param)
    for key,value in key_param.items():
        print(key,value)
    modified_pos_param = pos_param +(50,)
    myFun2(x,*modified_pos_param,**key_param)


def myFun2(*args, **kwargs):
    print(args)
    print(kwargs)


myFun(20, 10, 40, 30, name=" payel", age=" 30")