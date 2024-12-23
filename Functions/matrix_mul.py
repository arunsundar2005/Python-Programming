"""
A = [   [2, 3, 4]
        [5, 6, 7]
        [8, 9, 0]   ]

    
B = [   [1, 6, 9],
        [5, 8, 7],
        [5, 8, 7],
        [4, 0, 2]   ]

        
"""

def mat_mul(A, B, m, n, p):
    C = []
    for i in range(0, m):
        r = []
        for j in range(0, p):
            t = 0
            for k in range(0, n):
                t += A[i][k] * B[k][j]
                
            r.append(t)
        C.append(r)

    return C

def validity(A, B):
    if len(A) == len(B[0]):
        return True
    else:
        raise TypeError("The Matrices cannot be multiplied")
    


def get_mat(param = False):
    X = []
    m = int(input("Enter the number of rows of matrix A"))
    n = int(input("Enter the number of columns of matrix A"))

    for i in range(m):
        r = []
        for j in range(n):
            t = int(input(f"Enter the element at position at: row - {i}, column - {j}"))
            r.append(t)
        X.append(r)
    return X if param else X,m,n

def main():
    A,m, n = get_mat(True)
    print(A)
    B, p, q = get_mat(True)
    print(B)
    MM =  []
    if validity(A, B):
        print(mat_mul(A, B, m,n,q))


if __name__ == '__main__':
    main()