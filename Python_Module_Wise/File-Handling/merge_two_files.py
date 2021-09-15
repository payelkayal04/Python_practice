data = data2 = ""

with open("input_append.txt") as fp:
    data = fp.read()

with open("output_append.txt") as fp:
    data2 = fp.read()
    

data += "\n"
data += data2

data3 = open("file3.txt","w")
data3.write(data)