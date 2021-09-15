file1 = open("story.txt","r")
file2 = open("updated_story.txt","w")

for line in file1:
    if not (line.startswith("YYYY")):
        print(line)
        file2.write(line)

file1.close()
file2.close()