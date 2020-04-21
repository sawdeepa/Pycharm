a=10
b=5
a,b=b,a
print(a)
print(b)

a=b=c=2
print (a,b,c)
a,b,c=2,3,4
print (a,b,c)
a=[4,5,6]
x,y,z=a
print (x,y,z)
#x,y=a
#w,x,y,z=a

print("{} is my age".format(20))

def add (x,y=10):
    return x+y
a=add(1,2)
b=add(1)
print(a)
print(b)

def wish(name,age):
    print("Hello {} you are {} years old".format(name,age))
wish('India',67)
wish(67,'India')#error
wish(age=27,name="India")

ips=[
    "www.google.com",
    "www.memooo.com"
]
def myping(ip):
    compand="ping -c 5 {}>/dev/null".format(ip)
    response=os.system(command)
    if response==0:
        return True
    else :
        return False

for ip in ips:
    if myping(ip) == True:
         print("{} is up".format(ip))
    else
