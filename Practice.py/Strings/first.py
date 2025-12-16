text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in text:  #for loop / char is variable / text for store the string in char
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")





