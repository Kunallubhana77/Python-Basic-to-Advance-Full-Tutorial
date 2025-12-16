import math as m
radius = float(input("Enter the radius of the circle: "))
area_circle = m.pi * radius ** 2
print("Area of the circle:", area_circle)

circumference_circle = 2 * m.pi * radius
print("Circumference of the circle:", circumference_circle)

cost = int(input("Enter the cost of the circle: "))
cost_per_unit = cost / circumference_circle
print("Cost per unit of the circle:", cost_per_unit)


