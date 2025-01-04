"""
A "while" loop repeats a block of code as long as a condition is true.
The condition is evaluated before each iteration.

Syntax:

While condition:
    statement 1
    statement 2
    ..

"""

i = 0
while i < 5:
    print(i)  # This will print values from 0 to 4
    i += 1  # Incrementing the value of i to eventually stop the 
#----------------------------------------------------------------------------------------------
# Break Statement
# The "break" statement allows you to exit the loop prematurely when a condition is met.
i = 0
while i < 10:
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
    i += 1
#---------------------------------------------------------------------------------------------
# Continue Statement
# The "continue" statement skips the current iteration and moves to the next one.
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue  # Skip printing when i equals 2
    print(i)
    i += 1


#---------------------------------------------------------------------------------------------

"""

Similar to for, else can also be used with While as well
TheThe else block goes after the body of the while loop.
"else" block runs when the while loop ends naturally (i.e., without a break).

Syntax:

While Condition:
    Statement 1
    Statement 2
    ..
else:
    print("The While loop exited naturaly")

 """

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("While loop completed without a break")

# The else is not executed if the loop exits via a break


# Infinit While loop 
# An infinite while loop runs indefinitely unless a break condition or external intervention occurs.
# It is often used for continuous execution until a specific condition is met.
while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input == 'exit':
        break  # Exit the loop if user types 'exit'
    print(f"You typed: {user_input}")
