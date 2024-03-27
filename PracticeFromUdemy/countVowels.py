# s = input("Enter your word: ")
# c = 0
# for i in s:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
#         c = c + 1
# print("Vowels: ", c)


s = input("Enter your word: ")
count = 0
vowel = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i.lower() in vowel:
        count += 1
print("Vowel=", count)
