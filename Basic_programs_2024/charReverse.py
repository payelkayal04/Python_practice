"""s = input("Enter a sentence: ")
temp = s.split()
print(temp)
result = []
i = len(temp) - 1
while i >= 0:
    result.append(temp[i][::-1])
    i = i - 1


print(' '.join(result))"""

# s = input("Enter a word: ")
# temp = s.split()
# print(temp)
# result = []
# i = 0
# while i < len(temp):
#     result.append(temp[i][::-1])
#     i = i + 1
# print(result)
# print(' '.join(result))


s = input("Enter a word: ")
temp = s.split()
result = []
for i in range(len(temp)):
    result.append(temp[i][::-1])

print(result)



