class School():
    def __init__(self, name, no_of_students, location, estabilshed_on, principal):
        self.school_name = name
        self.school_population = no_of_students
        self.school_location = location
        self.school_establised = estabilshed_on
        self.__controler = principal # private Variable

    def aboutSchool(self): # This is a method not a function, as it has self as a parameter.
        return f"There is a school named {self.school_name} at {self.school_location} with around {self.school_population} students studying there, that was established on {self.school_establised}."
    
    def __privateInfo(self):
        return f"Principal of {self.school_name} is {self.__controler}, and trust me he is worst."
    
    def __changeControler(self, Name):
        self.__controler = f"Brother {Name}"
        print("Thanks a lot, Hope he does good")

    def __del__(self):
        print(f"\a\a\aDeletting... ... ...\n\a\t\tOh Shit\a, It's all your fault, didn't I tell you that {self.__controler} would bring doom to {self.school_name} one day :( :(\n\t\tMy era is over, Bye ! ! !\nDeleted Successfully")


sma = School("St. Michael's Academy", 10000, "Gandhi Nagar", 2005, "Brother Paul")

print(sma.school_name)
print(sma.school_establised)
# print(sma.__controler)  -> Not accessable
print(sma._School__controler) # Accessing the private variable using double underscore
print(sma.aboutSchool())
# print(sma.__privateInfo()) -> Not Accessable
print(sma._School__privateInfo())
# sma._School__changeControler("Jacob") -> Not accessable
sma._School__changeControler("Jacob")
print(sma.__module__) # Tells in which module is this present
# print(sma.__bases__) # Tells all the classes this object is based on
del(sma)



def funct():
    print("This is a function not a method")