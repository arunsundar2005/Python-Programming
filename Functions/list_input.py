# this file depicts the multiple ways of populating the list from the user's data.


if __name__ == '__main__': 

    """
    This line is used to check if the file is run on it's own or is it used as a package and called
    in some other files. 

    If the file is run on it's own (__name__ = '__main__') the following code will be executed, else if the file is used as 
    package and called by some other file (__name__ != '__main__'), then the following lines are not executed.
    """

    # Method 1:

    s = input("Enter all the numbers seprerated by space")
    l = s.split()
    l = [int(i) for i in l]

    # Method 2:

    n = int(input("Enter the max number of value"))
    l = []
    for i in range(n):
        l.append(int(input(f"Enter the {i+1}th value.")))
    l = [int(i) for i in l]

    # Method 3:

def custum_input(n):
    l = []
    for i in range(n):
        l.append(int(input(f"Enter the {i+1}th value.")))
    return [int(i) for i in l]


# Method 4 : Creative Approach

def multiple_inputs():
    try:
        l=[]
        while True:
            l.append(int(input("Enter the number, if you have entered enough numbers press Ctrl+ C : ")))
    except KeyboardInterrupt:
        print("\n", l, sep='') # Printing the list in a new line, the sep='' is used to remove the space provided by the comnma operator


