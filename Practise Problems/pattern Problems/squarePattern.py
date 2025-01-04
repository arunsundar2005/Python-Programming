def square_pat(n):
    for i in range(1,n+1):
        print('*'*n)



# square_pat(3)

def upper_traingle(n):
    for i in range(n, 0, -1):
        print('*'*i)

# upper_traingle(3)

def lower_traingle(n):
    for i in range(1, n+1):
        print('*'*i)

lower_traingle(5)



def num_triangle(n):
    for i in range(1,n+1):
        print(str(i)*i)