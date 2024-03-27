n = int(input("Enter a number : "))
c = 0
for i in range(2, n - 1):
    if n % i == 0:
        c += 1
if c >= 1:
    print("The given number is not a Prime number")
else:
    print("The given number is a Prime number")