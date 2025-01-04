# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Class inheriting from Animal
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

# Grandchild Class inheriting from Mammal
class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Example usage:
dog = Dog()
dog.speak()  # Inherited from Animal class
dog.walk()   # Inherited from Mammal class
dog.bark()   # Defined in Dog class
