import random

winner = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Winner:", winner)

backup1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
backup2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("backup 1:", backup1)
print("backup 2:", backup2)


while backup1 == winner:
    backup1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


while backup2 == winner or backup2 == backup1:
    backup2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

