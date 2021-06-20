#prime numbers: 2,3,5,7,11 etc..

# print("Enter your number : ")
# n = int(input())
# count = 0
#
# if n<2:
#     print("not valid")
# else:
#     for i in range(2,(n//2)+1):
#         if n % i == 0:
#             count = +1
#     if count > 0:
#         print("The number is not a Prime number")
#     else:
#         print("The number is a Prime number")

#using flag
# Program to check if a number is prime or not

num = 29

# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


