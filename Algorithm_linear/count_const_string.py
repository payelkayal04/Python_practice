input_string_1 = "HELlo World"
input_string_2 = "PythonProGramming"
# output = HllWrld
vowel = "aeiou"


def iterative_const_count(input_string):
    count = 0
    input_string = input_string.lower()
    for i in range(len(input_string)):
        if input_string[i] not in vowel and input_string[i].isalpha():
            count += 1
    return count


print(iterative_const_count(input_string_1))
print(iterative_const_count(input_string_2))


def recursive_cons_count(input_string):
    if input_string == '':
        return 0

    if input_string[0].lower() not in vowel and input_string[0].isalpha():
        return 1 + recursive_cons_count(input_string[1:])
    else:
        return recursive_cons_count(input_string[1:])


print(recursive_cons_count(input_string_1))
print(recursive_cons_count(input_string_2))
