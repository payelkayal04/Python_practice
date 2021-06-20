def rev_sentence():
    sentence = input()
    print(sentence)
    sentence = sentence[::-1]
    return sentence


word = "payel"


def rev_word(word):
    word = word[::-1]
    return word


# print(rev_word(word))
# print(rev_sentence())


def reverse_string(str):
    str1 = ""  # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1
        # print(i)
    # print(str1)
    return str1  # It will return the reverse string to the caller function


str = "JavaTpoint site"  # Given String
print("The original string is: ", str)
print("The reverse string is", reverse_string(str))  # Function call
