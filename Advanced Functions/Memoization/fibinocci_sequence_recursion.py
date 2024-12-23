#Fibonacci Sequence 
# 1 , 1, 2, 3, 5, 8, ....
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


"""
The above code causes a delay for higher values for n.
This happens due to the fact that some values are calculated redundantly.
This can be prevented using memoization. Each number from 1 to n may be calculated more than once,
so the overall Big O complexity of the program is given as : O(2^n) 
"""