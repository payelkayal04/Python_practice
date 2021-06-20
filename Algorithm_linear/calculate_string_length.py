# Given a string , calculate the length of the string

input_string = "PayelKayal"

print(len(input_string))


def iterative_str_len(input_str):
    count = 0
    for i in range(len(input_string)):
        count += 1
    return count


def recursive_str_len(input_string):
    count = 0
    count += 1
    print(input_string[1:])
    if input_string == '':
        return 0
    else:
        return count + recursive_str_len(input_string[1:])


print(iterative_str_len(input_string))
print(recursive_str_len(input_string))
