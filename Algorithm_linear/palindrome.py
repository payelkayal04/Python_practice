import string

str = "Dammit I'm mad"
def check_palindrome(str1):
    exclist = string.punctuation + string.digits
    print(exclist)
    table_ = str.maketrans('', '', exclist)
    print(table_)
    newtext = str1.translate(table_)
    print(newtext)
    newtext = newtext.replace(" ","")
    newtext = newtext.lower()
    print(newtext)

    str2 = ""
    for i in newtext:
        str2 = i + str2
    print(str2)

    if newtext == str2:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome(str)
