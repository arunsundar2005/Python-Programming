"""
The "for" loop is used to iterate over a sequence (like a list, tuple, string, etc.)
and execute a block of code for each element in the sequence

Syntax:
for item in sequence:
    Code to execute for each item in the sequence
    print(item)


"""

l = [1,5,6,5,9,45,7]

sum = 0
for i in l:
    sum = sum + i

print(f"The sum of the list is {sum}")


# The for loop can be integrated with range function
s = 0
for i in range(1, 11):
    s = s + i

print(f"The sum of 1st 10 natural numbers is {s}")


# The range function can be modified in various ways, will be discussed in nexr files


#----------------------------------------------------------------------------------------------------------------------------
# The Break Statement
# The "break" statement allows you to exit the loop prematurely if a certain condition is met.
for i in range(10):
    if i == 5:
        break  # Exits the loop when i reaches 5
    print(i)

#----------------------------------------------------------------------------------------------------------------------------
# The Continue Statement
# The "continue" statement allows you to skip the current iteration and continue with the next iteration.
for i in range(5):
    if i == 2:
        continue  # Skips the current iteration when i is 2
    print(i)
#----------------------------------------------------------------------------------------------------------------------------
## For-else Loop:

# The else block is placed after the bnody of the for loop.
# and will be executed after the for loop exhits
"""
Syntax:

for item in sequence:
    statement 1
    ..
else:
    print("The for loop exited naturally")

"""


sum = 0
for i in l:
    sum = sum + i
else:
    print(f"The sum of the list is {sum}")