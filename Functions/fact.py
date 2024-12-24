"""
This file calculates the factorial of all the number in a list.
"""

from list_input import custum_input
d = {1:1, 0:1}
def fact(n):
    if n in d.keys():
        return d[n]
    else: 
        f = n*fact(n-1)
        d[n] = f
        return f


l = custum_input(2)
l = [fact(i) for i in l]
print(l)

