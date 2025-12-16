total_fine = 0
for book in range(1,6):
    days_late = int(input(f"enter days ; late for book (book): "))
    if days_late == 0:
        continue
    fine = days_late * 2
    print(f"fine for book (book): rs {fine}")
    total_fine += fine
print("\total fine to be paid: rs", total_fine)