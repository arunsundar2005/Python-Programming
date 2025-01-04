#Data Structures 
#List []
#List :- List is the collection of heterogeneous elements
#any different datatypes 
l = ["a", "e", "i", "o", "u", 1, 2, 3]
print(l)
#Indexing; Zero Indexing; 
# "a" -> 0 --> l[0]
# "e" -> 1 --> l[1] 
# "i" -> 2 --> l[2]
# "o" -> 3 --> l[3]
# "u" -> 4 --> l[4]
# 1   -> 5 --> l[5]
# 2   -> 6 --> l[6]
# 3   -> 7 --> l[7]
print(l[0])
print("Eigth Term is", l[8-1]) ##Eigth Element 
print("Fifth Element is ", l[4])

#Slicing -> Chunking of Sequential Indices 
print(l[0:7]) #l[1:4] #l[i:j] -- i, i+1, i+2, ... ,j-1
print("Second to Sixth Element", l[1:6])

#dir function on list 
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', 
'__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] """
list1 = [1,2,3,1,2,3,4,5,6]

#count method represent the frequence of element in the list 
print("Number of times 1 repeated is", list1.count(1))

#SORT 
lst = [10, 12, 9, 11, 15]
lst.sort() #Ascending Order 
print(lst)

lst.sort(reverse = True) #Descending Order #Reverse is one Argument in sort method 
#By Default, reverse = False 
print(lst)


#Append (append)
e = "ASDF"
lst.append(e) #Add the e to the last and e could be any data type 


#range()
#range(a) --> Starting from 0 to a-1 with increment of 1 
#range(a,b)
#range(a,b,c)
#Create a Range Variable 
r = range(5) 
print(type(r))
#Converting range to list 
r_list = list(r) 
print(r_list)

#Range Type 2 
r1 = range(2,10)
r1_list = list(r1)
print(r1_list)

#Range Type 3 
r2 = range(2, 10, 2)
r2_list = list(r2)
print(r2_list)

#For Loop 
"""
for variable in iterable: 
    Action Block 
"""
#List and Range are coming under iterable 
