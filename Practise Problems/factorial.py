def factorial(x):
    if x ==0:
        return 1
    return x * factorial(x-1)


def fact_lib(x):
    import math
    return math.factorial(x)



if __name__ == '__main__':
    print(factorial(5))