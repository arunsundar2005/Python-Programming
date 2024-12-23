# x = int(input("Enter m"))
# y = int(input("Enter n"))

def main(x,y):
    if x %2 == 0 or y % 2 ==0:
        a = multiply(2*y-1)
        b = multiply(2*y)
        print(a,b)
        return str(a / b)+" pi/2"
    else:
        return "pi/2" 
        



def multiply(x):
    if x==0 or x==1:
        return 1
    return(x*multiply(x-2))

    

    
print(main(5,4))