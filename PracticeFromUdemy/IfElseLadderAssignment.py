m = float(input("Enter marks for Math: "))
print(m)
p = float(input("Enter marks for Physics: "))
print(p)
c = float(input("Enter marks for chemistry: "))
if m > 100 or p > 100 or c > 100:
    print("Invalid input")
elif m < 35 or p < 35 or c < 35:
    print("You are disqualified")
else:
    s = 1
    print("Pass")
    print(s)

    if s == 1:
        avg = (m + p + c) / 3
        print("Average is : ", avg)

        if avg <= 59:
            print("Grade : C")
        elif avg <= 69:
            print("Grade : B")
        else:
            print("Grade : A")
