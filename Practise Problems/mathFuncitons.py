from math import *
x, y = 1, 2
z = exp(x)+log10(sqrt(y/x))
print(z)
print(log1p(-2))
print(log10(10))
print(log2(2))

for i in range(1000):
    if log1p(i)==1.0:
        print(f'The base of the log function is {i}')
        break
    else:
        print(i)
    
    