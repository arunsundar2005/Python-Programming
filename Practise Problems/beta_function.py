def fact(x):
    if x == 0:      
        return 1
    else:
        return x*fact(x-1)
    


def beta(x,y):
    num = fact(x-1) * fact(y-1)
    denom = fact(x+y-1)
    return num/denom

print(beta(2,3))