#set does not allow duplicate
a={1,1,2,2,3,3,4,4}
print(a)
b={1,1,2,2,3,3,4,4}
print(b)
c= b.union(a)
print(c)
d= b.intersection(a)
print(d)