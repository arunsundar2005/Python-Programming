#Assignment 
#Python is Basic Calculator ; Based Constants 
#We Need Variables; Variable --> Memory Container to Store values 
#Memory Size --> Bits and Bytes 1 Byte = 8 Bits 
a = 10  #Variable "a" which allocates memory to store the value 10. 

#What type is the "a" ? 
print(type(a))
#<class 'int'> class --> Object Oriented Programming (OOPs); 
#Name of the Class = "int"

b = c = 10 

print(b, c)
#Location of b and C  #function Used: id 
print(id(b))
print(id(c))
print(id(a))
d = 11 
print(id(d))
e = 10 
print(id(e))
e = e + 1
print(id(e))
#Opertors Boolean Operators 
#Equality a == b 
#less than a < b 
#Less Than or Equal to a <= b 
#Greater Than a > b 
#Greater Than or Equal to a >= b 
#Not Equal to a != b 
print(e, d)
print(id(e) != id(d))
d = 5.0
print(id(e) != id(d))

