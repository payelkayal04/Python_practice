"""
Write a program which will take an input and do the following operation.
1. If its a string upper case character then it will make it lower case and visa versa
2. If the string contains a number which ends with another number then those two numbers will be swapped
below are the examples:
Input: "Hello -5LOL6"
Output: "hELLO -6lol5"
Input: "2S 6 du5d4e"
Output: "2s 6 DU4D5E"
"""

def num_swap(string):
    arr = list(map(str,string))    #split the string characters to a list
    start = 0
    for i in range(len(arr)):
        if arr[i].isupper():
            arr[i] = arr[i].lower()
        elif arr[i].islower():
            arr[i] = arr[i].upper()
        elif arr[i] == ' ':
            start = 0  # bcoz if a number is already seen and number ends with a space instead of another number
                          # for that condition we should not swap those two value
        elif (arr[i].isdigit()):
            #elif (arr[i].isdigit() != i>=len(arr)):
            if start == 0:
                start = i
            else:
                end = i
                arr[start], arr[end] = arr[end], arr[start]
                start = 0       # once swapped again start to zero
    print("".join(arr))


string1 = "Hello -5LOL6"
string2 = "2S 6 du5d4e"
string3 = "2ss *7&hhes9o hel23o"
string4 = "Hello -5L4OL6"

num_swap(string1)
num_swap(string2)
num_swap(string3)
num_swap(string4)


