# a list of strings
#sort it
# print the last 4 strings

a=[1,2,3,4,5,6,7,8]
a.sort()
print(a)
print(a[-4:])
#print(a[-4:].reverse)
print(a[-1:3:-1])

# create a list of numbers(integers and floats)
#remove the smallest one
#find out if 9 is there in the list
a=[1,2.5,3,4.5,5,6.5,7,8.5]
b=print(min(a))
a.remove(min(a))
print(a)
print( 9 in a)
