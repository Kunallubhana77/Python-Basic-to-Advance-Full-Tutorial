total_steps = 10000
steps_per_input = total_steps // 2  # User will enter half in two parts

for i in range(2):  # Loop twice for two inputs
    steps = int(input(f"Enter {steps_per_input} steps: "))
    if steps == steps_per_input:
        print(f"Great! You entered {steps} steps.")
    else:
        print("Please enter the correct number of steps.")
