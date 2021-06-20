input_str_1 = "kolKata"
input_str_2 = "kolkAta"
input_str_3 = "kolkata"


# Iterative way
def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))
print("--------------------------------")


# Recursive way
def find_uppercase_recursive(input_str, indx=0):
    if input_str[indx].isupper():
        return input_str[indx]
    if indx == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, indx + 1)


print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))
