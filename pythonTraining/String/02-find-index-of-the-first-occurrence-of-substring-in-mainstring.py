def strstr(heystack: str, needle: str):
    if needle in heystack:
        index = heystack.index(needle)
        return index
    else:
        return -1


print(strstr(heystack="Hello", needle="ll"))
