"""
check-string-substring-another
"""


def search(txt, pat):
    m = len(txt)
    n = len(pat)

    for i in range(m - n + 1):
        flag = 0
        for j in range(n):
            if txt[i + j] != pat[j]:
                flag = 1
                break
        if flag == 0:
            print("pat {} found in {}".format(pat, i))


txt = "sky is blue"
pat = "is"
search(txt, pat)
