"""
Given a string , find the first uppercase character.
Solve using both recursive and iterative solution.
"""

input_string_1 = "lucidProgramming"
input_string_2 = "LucidProgramming"
input_string_3 = "lucidprogramming"


def Find_uppercase_iterative(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].isupper():
            print(input_str[i])
            count += 1
    if count <= 0:
        print("No uppercase character found")


def Find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
    return Find_uppercase_recursive(input_str, idx + 1)


(Find_uppercase_iterative(input_string_1))
(Find_uppercase_iterative(input_string_2))
(Find_uppercase_iterative(input_string_3))
print("----------------------------------------------------")

print(Find_uppercase_recursive(input_string_1))
print(Find_uppercase_recursive(input_string_2))
print(Find_uppercase_recursive(input_string_3))
