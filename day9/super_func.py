class parent:
    def __init__(self):
        print("parent constructor")

class child(parent):
    def __init__(self):
        super().__init__()
        print("child constructor")

c = child()                


# We use super() here to explicitly invoke the parent class’s __init__ method
# so that any initialization logic defined in Parent runs before (or alongside)
# the Child’s own initialization. Without super(), the parent constructor
# would be skipped and the Child would start with an uninitialized parent part.


# super() ka use isliye kiya gaya hai taaki child class apne parent class ke __init__ method ko
# call kar sake. Isse parent class ka constructor execute hota hai aur parent ke attributes/methods
# child mein available ho jaate hain. Agar super() na use karein to parent ka constructor skip ho jaayega
# aur child class parent ki initialization miss kar degi.



# Class: A blueprint that defines attributes (data) and methods (functions) common to all objects created from it.
# Object: A specific instance of a class; it holds actual data in the attributes defined by the class.
# Attribute: A variable stored inside a class or object that holds data related to the object’s state.
# Method: A function defined inside a class that describes the behaviors or actions an object can perform.
# __init__(): The constructor method automatically called when a new object is created; used to initialize the object’s attributes.



