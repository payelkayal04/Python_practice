arr = []
with open("book.txt") as df:
    for line in df:
        arr.append(line)

    print(arr[2])


def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            print(i+1, end=",")

findline("Hello")


