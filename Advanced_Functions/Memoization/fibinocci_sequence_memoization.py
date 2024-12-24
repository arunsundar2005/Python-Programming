#Fibonacci Sequence using Memoisation 
# 1 , 1, 2, 3, 5, 8, ....
d = {0:0, 1:1} # Global Variable 
def fib(n):
    if(n in d.keys()):      # Prevents calculating already calculated values,
        return d[n]         # as all the values are stored in the dicrionary and reused when necessary, thus reducing the time required.
    else: 
        t = fib(n-2) + fib(n-1)
        d[n] = t # Populate the Dictionary 
        return t 



if __name__ == '__main__':
    n = int(input("Enter the Number?"))
    for i in range(1,n+1):
        print(fib(i), end= "\t")



"""
As all the numbers from 1 to n are calculated exactly once, thus
the overall Big O complexity of the program is given as : O(n)
"""