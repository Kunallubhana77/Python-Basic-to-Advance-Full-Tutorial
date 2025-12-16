# Nested If-Else Statements

print("=" * 50)
print("Example 1: Student Grade System")
print("=" * 50)

marks = 85
attendance = 75

if marks >= 60:
    print("✓ Marks sufficient for passing")
    if attendance >= 75:
        print("✓ Attendance requirement met")
        if marks >= 90:
            print("Grade: A+ (Excellent!)")
        elif marks >= 80:
            print("Grade: A (Very Good!)")
        else:
            print("Grade: B (Good!)")
    else:
        print("✗ Attendance below 75%")
        print("Result: Failed due to low attendance")
else:
    print("✗ Marks below passing threshold")
    print("Result: Failed")

print("\n" + "=" * 50)
print("Example 2: User Authentication System")
print("=" * 50)

username = "admin"
password = "admin123"
is_active = True

if username == "admin":
    print("✓ Valid username")
    if password == "admin123":
        print("✓ Correct password")
        if is_active:
            print("✓ Account is active")
            print("Login Successful! Welcome, Admin")
        else:
            print("✗ Account is deactivated")
            print("Access Denied")
    else:
        print("✗ Incorrect password")
        print("Access Denied")
else:
    print("✗ Invalid username")
    print("Access Denied")

print("\n" + "=" * 50)
print("Example 3: Age Category System")
print("=" * 50)

age = 25
has_license = True

if age >= 18:
    print("✓ Adult")
    if has_license:
        print("✓ Has driving license")
        if age >= 25:
            print("Eligible for: Car rental without extra fees")
        else:
            print("Eligible for: Car rental with young driver fees")
    else:
        print("✗ No driving license")
        print("Not eligible for car rental")
else:
    print("✗ Under 18")
    print("Not eligible for driving")

print("\n" + "=" * 50)
print("Example 4: Temperature Check")
print("=" * 50)

temperature = 28
humidity = 70

if temperature > 25:
    print("Hot weather")
    if humidity > 60:
        print("High humidity - Feels uncomfortable")
        print("Recommendation: Use AC or stay hydrated")
    else:
        print("Low humidity - Pleasant")
        print("Recommendation: Enjoy outdoor activities")
else:
    print("Cool weather")
    if temperature < 15:
        print("Cold - Wear warm clothes")
    else:
        print("Moderate - Perfect temperature")
