s = input("Enter a sentence: ").lower()
word = input("Enter a word which you want the position: ").lower()
pos = -1
length = len(s)
found = False

while True:
    pos = s.lower().find(word.lower(), pos + 1, length)
    if pos == -1:
        break
    print("Found the sub string at position ", pos)
    found = True

if found == False:
    print("Sub string not found")

