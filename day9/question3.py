class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Soham", 85)
student1.print_details()
