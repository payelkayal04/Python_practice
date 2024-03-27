# n = int(input("Enter your number: "))
# print(n)
# if n%2 == 0:
#     print("It's a Even number")
# else:
#     print("It's a odd number")


def EvenOdd(num):
    print(type(num))
    # if type(num) != int or type(num) != float:
    #     print("Invalid")
    if num == 0:
        print("Value is zero", num)
    elif num % 2 == 0:
        print("It's a Even number")
    else:
        print("It's a odd number")


n = int(input("Enter your number: "))
EvenOdd(n)
