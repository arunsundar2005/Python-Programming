# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Example usage:
dog = Dog()
dog.speak()  # Inherited from Animal class
dog.bark()   # Defined in Dog class
