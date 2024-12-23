import math
from math import floor

def calc(n):
    if n == 1 and n == 2:
        return 1
    else:
        return (floor(n/2) + math.ceil(n/2))

def series(x,n):
    if (x == n):
        return x
    else:
        return calc(x) + series(x+1,n)


def tree(x, n):
    if n == 0:
        print("Invalid Input")
    else:
        series(x,n)