#Print Testing
"""This file is to print the given string; 
this is called as doc string!!! --> Can be regarded as multiline comments; 
"""
print("Welcome to Python Programming!!!")

print("Welcome ", end='') #By Default end = "\n" \n ==> New Line Escape Sequence 
print("to Python Programming", end = " ")
print("!!!")

#Using Concatenation of Strings, Strings --> Sequence of Character is called as strings 
#s = "hello123" 
#t = "123"
print("Welcome " + "to Python" + " " + "Programming  " + "!!!")
print("Welcome", " ", "to", " ", "Python", " ", "Programming", "!!!") #sep = " "
print("Welcome", "to", "Python ", "Programming", "!!!", sep= "-")
print("Welcome", "to", "Python ", "Programming", "!!!", sep= " ")#BY Default sep = " "
print("Welcome", "to", "Python ", "Programming", "!!!", sep= " ", end = "!!$")
print("\n")
#fstrings -> formatted strings 
name = "Python" #Variable -> "name" --> Variable identifier 
#value stored in variable name --> "Python"
print("Welcome to", name, "Programming")
##Fstrings: 
print(f"Welcome to {name} Programming", " Using fstrings")
print("Welcome to {name} Programming", " Using strings")

#Type Specifiers 
print("Welcome to %s Programming!!! Using Data Specifier"%name)  #%s --> Strings %d --> Integer %f --> FLoat
print("Welcome to %s Programming!!! Using Data Specifier"%name, end="$$\n")  

#Mutliple Data Types 
print(1 + 2) ##Integer 
print("1" + "2") ##String --> Concatenation 
print(1.0 + 2) #1.0 --> Float; Integer is converted to Float and then addition happened 
#print("1" + 2) --> Throw an error as string is concatenated with integer. Made the process to string function 
print("1",2) #concatination but using "," Makes the process under print function 
print("Welcome", "to", "python", "class", 1, "on", "Saturday", "tech", 5.0) 
print(f"Welcome to {name} Class {1} on Saturday tech {5.0}")
print("Welcome to %s class %d on Saturday tech %.1f"%(name, 1, 5.0)) #Ordering must be precise 
print("Welcome to %s class %d on Saturday tech %.2f"%(name, 1, 5.0)) #Ordering must be precise 

i = 1 
f = 5.0
print("Welcome to %s class %d on Saturday tech %.2f"%(name, i, f)) #Ordering must be precise 

#Single Line Multiple Statements 
i = 1; f = 5.1
print("Welcome to %s class %d on Saturday tech %.2f"%(name, i, f)) #Ordering must be precise 

print("Size Occupied by i", i.__sizeof__(), "bits")
#8 Bits = 1 Byte 
#Garbage Collector --> Collect unwanted memory allocations 
# Ther is a thing called Garbage Overload 
#Generally INT in Python would take 32 Bits --> 4 Bytes of Memory Allocation 
print("Size Occupied by i", i.__sizeof__()/8, "bytes") #Single / -> Normal Division output float 
print("Size Occupied by i", i.__sizeof__()//8, "bytes") #// -> Integer Division 

import sys #sys --> system package ; #import keyword 
print(dir(sys)) #dir will print the methods (functions) and attributes (variables) along with the given one 
print("Size of", sys.getsizeof(i))