# Parent Classes
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal:
    def walk(self):
        print("Mammal walks")

# Child Class inheriting from both Animal and Mammal
class Dog(Animal, Mammal):
    def bark(self):
        print("Dog barks")

# Example usage:
dog = Dog()
dog.speak()  # Inherited from Animal class
dog.walk()   # Inherited from Mammal class
dog.bark()   # Defined in Dog class
