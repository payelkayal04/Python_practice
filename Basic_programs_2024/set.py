s = {1,2,3,4,1,4} #set is unique
print(type(s))
print(s)
s.update([88,99])
print(s)
#print(s[0]) Set object does not support indfexing
s.remove(3)
print(s)
'''
f = frozenset(s)
print(f)
f.update([12])
print(f)
'''