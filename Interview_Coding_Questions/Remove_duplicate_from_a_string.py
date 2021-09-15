# Program without using any external library
#s = "Python is great and Java is also great"
s = "Payel Payel Kayal"
#split() will convert string into list
l = s.split()
print(l)
k = []
for i in l:

    # If condition is used to store unique string
    # in another list 'k'
    print(s.count(i))
    if (s.count(i) >= 1 and (i not in k)):
        k.append(i)

print(' '.join(k))