a = 0
b = 1
fib = []
fib.append(a)
fib.append(b)
while (b < 1000):
    a, b = b, a + b
    fib.append(b)

print(fib)
