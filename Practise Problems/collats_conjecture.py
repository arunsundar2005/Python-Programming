def colatz(x, c=0):
    if x %2 == 0:
        return colatz(x/2, c+1)
    elif x == 1:
        return f"Collatz Conjecture proved in {c} steps "
    else:
        return colatz(3*x + 1, c+1)
        

print(colatz())