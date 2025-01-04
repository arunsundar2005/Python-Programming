# Parent Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child Classes inheriting from Animal
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

# Hybrid Child Class inheriting from both Mammal and Bird
class Bat(Mammal, Bird):
    def hang(self):
        print("Bat hangs upside down")

# Example usage:
bat = Bat()
bat.speak()  # Inherited from Animal class
bat.walk()   # Inherited from Mammal class
bat.fly()    # Inherited from Bird class
bat.hang()   # Defined in Bat class
