print("Student marks analyzer")

total_marks = 0
subject_count = 0

while True:
    marks = float(input("enter marks for subject (or -1 to stop): "))
    if marks == -1:
        break
    if marks < 0 or marks > 100:
        print("invalid marks")
        continue

    total_marks += marks
    subject_count += 1

if subject_count == 0:
    print("no marks entered. program ended.")

else:
    average = total_marks / subject_count

    print("\n result summary")
    print("total marks", total_marks)
    print("total marks", total_marks)
    print("average marks", round(average,2))

    if average>=90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"


    print("grade obtained :", grade)
    
    print("\n grade chart")
    grade_ranges = {
        "A": range(90, 101),
        "B": range(75, 90),
        "C": range(50, 75),
        "D": range(0, 50),

    }

    for g in grade_ranges:
        start = min(grade_ranges[g])
        end = max(grade_ranges[g])
        print("grade", g, ":", start, "to", end)


