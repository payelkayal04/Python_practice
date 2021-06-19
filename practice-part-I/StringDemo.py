string = "Payel.Kayal"
string1 = "Kolkata"
string2 ="K"
print(string[1])
print(string[0:5])

print(string+ string1)

print("{} {}".format(string,string1))   #concatanation using format
print(string2 in string1)          #substring check

var = string.split(".")
print(var)

print(var[0])

string3 = " great      "

print(string3.strip())
print(string3.lstrip())
print(string3.rstrip())
