def check_anagram(s1,s2):
    if not len(s1)==len(s2):
        return False

    str1 = sorted(s1.lower())
    str2 = sorted(s2.lower())
    if str1 == str2:
        return True
    else:
        return False

str1 = "abcde"
str2 = "aBced"
print(check_anagram(str1,str2))
