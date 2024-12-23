def divide(x,y):
    def subtract(x,y):
        return x-y
    c=0
    while x > 1:
        c=c+1
        x = subtract(x,y)
    
    return c 

print(divide(10,2))   
#print(divide.subtract(10,2)) -> Not possible