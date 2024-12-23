def fact(n):
    if n==0 or n==1:
        return 1
    else:
        # print(n)
        return n* fact(n-2)
    

# def numer(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         print(n)
#         return n* numer(n-2)
    

# n = 5
# for i in range(n-1, 1, -2):
#     print(i)
#     print("----------------------------------")

# print(denom(n-1))

def main(x):
    if x%2 == 0:
        print(f"Numerater is {fact(x-1)}")
        print(f"Denominator is {fact(x)}")
        return str(fact(x-1)/fact(x)) + "pi / 2"
    else:
        print("hi")
        print(f"Numerater is {fact(x-1)}")
        print(f"Denominator is {fact(x)}")
        return str(fact(x-1)/fact(x))
    


print(main(5))