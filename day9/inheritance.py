class animal:
    def speak(self):
        print("animal is speaking")

class dog(animal):
    def bark(self):
        print("dog is barking")        

d = dog()
d.speak()
d.bark()



# Inheritance: A mechanism where a new class (child/derived) acquires properties and behaviors (methods & attributes)
# of an existing class (parent/base), promoting code reuse and establishing a natural hierarchy.

# Types of Inheritance:
# 1. Single Inheritance: One child class inherits from one parent class.
# 2. Multiple Inheritance: One child class inherits from multiple parent classes.
# 3. Multilevel Inheritance: A class inherits from a derived class, forming a chain.
# 4. Hierarchical Inheritance: Multiple child classes inherit from one parent class.
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.
