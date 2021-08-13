input_string_1 = "Prog raMming"  # prgrmmng"
vowel = "aeiou"


def count_constant_iterative(input_str):
    input_str = input_str.lower()
    input_str = input_str.replace(" ", "")

    for i in vowel:
        if i in input_str:
            input_str = input_str.replace(i, "")
    print(len(input_str))


def recursive_cons_count(input_string):
    if input_string == '':
        return 0

    if input_string[0].lower() not in vowel and input_string[0].isalpha():
        return 1 + recursive_cons_count(input_string[1:])
    else:
        return recursive_cons_count(input_string[1:])


count_constant_iterative(input_string_1)
print(recursive_cons_count(input_string_1))
