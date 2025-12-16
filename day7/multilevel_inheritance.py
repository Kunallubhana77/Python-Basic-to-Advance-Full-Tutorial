# Multi-level Inheritance Example
# A class inherits from another class, which in turn inherits from a third class

class Animal:
    """Base class - Level 1"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def move(self):
        return f"{self.name} is moving"


class Mammal(Animal):
    """Intermediate class - Level 2"""
    def __init__(self, name, body_temp):
        super().__init__(name)
        self.body_temp = body_temp
    
    def warm_blooded(self):
        return f"{self.name} is a warm-blooded animal with temperature {self.body_temp}°C"


class Dog(Mammal):
    """Derived class - Level 3"""
    def __init__(self, name, body_temp, breed):
        super().__init__(name, body_temp)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} barks loudly"
    
    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Mammal):
    """Another derived class - Level 3"""
    def __init__(self, name, body_temp, color):
        super().__init__(name, body_temp)
        self.color = color
    
    def speak(self):
        return f"{self.name} meows"
    
    def scratch(self):
        return f"{self.name} scratches the furniture"


# Testing the multi-level inheritance
if __name__ == "__main__":
    # Create instances
    dog = Dog("Buddy", 38.5, "Golden Retriever")
    cat = Cat("Whiskers", 38.0, "Orange")
    
    print("=" * 50)
    print("DOG (Multi-level Inheritance: Dog -> Mammal -> Animal)")
    print("=" * 50)
    print(dog.speak())                    # Overridden method
    print(dog.move())                     # Inherited from Animal
    print(dog.warm_blooded())             # Inherited from Mammal
    print(dog.fetch())                    # Dog-specific method
    print()
    
    print("=" * 50)
    print("CAT (Multi-level Inheritance: Cat -> Mammal -> Animal)")
    print("=" * 50)
    print(cat.speak())                    # Overridden method
    print(cat.move())                     # Inherited from Animal
    print(cat.warm_blooded())             # Inherited from Mammal
    print(cat.scratch())                  # Cat-specific method
    print()
    
    print("=" * 50)
    print("Inheritance Chain Summary")
    print("=" * 50)
    print(f"Dog's MRO: {[c.__name__ for c in Dog.__mro__]}")
    print(f"Cat's MRO: {[c.__name__ for c in Cat.__mro__]}")
