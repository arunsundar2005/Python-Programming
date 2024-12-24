# Recursion Function for Factorial 

def fact(n):
    if(n == 1 or n == 0): #0! = 1! = 1 
        return 1
    else:
        return n * fact(n-1) # Recursive Call 

print(f"Factorial of the number is {fact(int(input("Enter a Number")))}")