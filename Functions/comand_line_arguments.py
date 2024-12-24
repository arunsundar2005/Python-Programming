
"""
Inputs to the file can also be given via the command line that is the terminal.

usually a python file is run in the below depicted way:

    python main.py

here arguments can be passed to the file as below:

    python main.py arg1 arg2 arg3

These arguments can be extracted via the sys package, a default package of python.
These arguments are saves in the varible argv of the sys package. It can be extracted as below. 
"""




def command_line_data_retrival():
    import sys
    data = sys.argv[1:]
    return [int(i) for i in data]  # Converting the strings to int. 


print(command_line_data_retrival())