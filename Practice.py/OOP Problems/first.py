# Create a Student class with name, roll, and marks; add method to compute average.

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def calculate_average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        return avg

# Creating a student object
student1 = Student("Rahul", 101, [85, 90, 78, 92, 88])

print(f"Student Name: {student1.name}")
print(f"Roll Number: {student1.roll}")
print(f"Marks: {student1.marks}")
print(f"Average Marks: {student1.calculate_average()}")
