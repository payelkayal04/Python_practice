outputfile = open("output.txt", "w")
inputfile = open("input.txt", "r")

lines_seen_so_far = set()
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)

outputfile.close()
inputfile.close()