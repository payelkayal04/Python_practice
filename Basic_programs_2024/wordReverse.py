s = input("Enter a sentence:")
temp = s.split()
print(temp)
result = []
i = len(temp) - 1
print(i)
print(result)
while i >= 0:
    result.append(temp[i])
    i = i - 1
print(result)
print(' '.join(result))