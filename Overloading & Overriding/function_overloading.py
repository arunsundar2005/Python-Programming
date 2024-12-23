from multipledispatch import dispatch



@dispatch(int, int)
def add(x,y):
    return x+y


@dispatch(float, float)
def add(x,y):
    return x+y



print(add(2,3))
print(add(2.5,3.5))
