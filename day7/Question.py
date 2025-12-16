import math as m
scores = [88, 92, 75, 81, 95, 78, 85, 90, 70, 84]

num_students = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
total_score = sum(scores)
average_score = total_score / num_students


print("Number of students who took the quiz:", num_students)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Total score:", total_score)
print("Average score:", average_score)
