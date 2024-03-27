def fibbo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    c = 1
    temp = n
    while temp <= n:
        for i in range(temp):
            print(c)
            a = b
            b = c
            c = a + b
        # print("temp = ", temp)

        break


fibbo(5)
