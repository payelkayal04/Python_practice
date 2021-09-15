f1 = open("abc1.txt","r")
f2 = open("abc2.txt", "w")

content = f1.readlines()
#print(type(content))
print(len(content))
for i in range(0, len(content)):
    if(i%2 == 0):
        f2.write(content[i])
    else:
        pass

f1.close()
f1 = open("abc1.txt","r")
content1 = f1.read()
print(content1)

f1.close()
f2.close()