f1 = open("input_append.txt", "r")
f2 = open("output_append.txt", "r")

print(f1.read())
print(f2.read())

f1.close()
f2.close()

f1 = open("input_append.txt","a+")
f2 = open("output_append.txt", "r")
f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print(f1.read())
print(f2.read())

f1.close()
f2.close()