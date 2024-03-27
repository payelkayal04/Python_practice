word = input("Enter a word: ")
vowels = {'a','e','i','o','u'}
results = {}
for c in word:
    if c in vowels:
        results[c] = results.get(c, 0)+1

for k,v in results.items():
    print(k,"is present", v, "times")


# for i in word:
#     if i.lower() in vowels:
#         vowels[i.lower()] += 1
#     # for key in vowels.keys():
#     #     if i.lower() == key:
#     #         # print('found')
#     #         vowels[key] += 1
# print(vowels)


# for key,value in vowels.items():
#     # print(key,value)

# for value in results.values():
#     print(value)

# for key in vowels.keys():
#     print(key)


