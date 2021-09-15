"""
Write a program to find the substring in a string.
String = "ABABACADAB"
Substring = "AB"
Output: [0,2,7] --> Index value of the staring of the Substring
"""
string1 = "ACABACADAB"
Substring = "AB"


def find_substring(string, substr):
    n = len(string)  # 10
    m = len(substr)  # 2
    index = []
    #print(n - m)
    for i in range(n - m + 1):
        flag = 0
        for j in range(m):
            if string[i + j] != substr[j]:
                flag = 1
                break
        if flag == 0:
            index.append(i)
            # print("index = ", index)
    if len(index):
        print("Substring found in index value: {}".format(index))
    else:
        print("Substring not found")


find_substring(string1, Substring)
