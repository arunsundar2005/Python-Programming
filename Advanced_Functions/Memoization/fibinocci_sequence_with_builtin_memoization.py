import functools
from functools import lru_cache
"""

The functools package provids a decorator that performs similar memoization as the one we performed. 
But the use of this is very easy and you just need to call the decorator, you need not initialize any global dictionaries, etc.

"""

@lru_cache
def fib(n):
    if(n == 0 ):
        return 0
    elif(n == 1):
        return 1 
    else: 
        return fib(n-2) + fib(n-1)


n = int(input("Enter the Number?"))
for i in range(1,n+1):
    print(fib(i), end= "\t")
