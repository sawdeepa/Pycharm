#A tuple is a read only list.
a=(1,5,8,3,5,9,7)
print(type(a))
print(a[0])
print(a[-1])
print(len(a))
print(sum(a))
print(min(a))
print(max(a))
print(a[2:5])
print(a[::2])
b=3,4,5
print(type(b))
print(b.count(4))
print(b.index(3))
print(b[2])
#b[2]=45
#b.append(3)
#b.sort()