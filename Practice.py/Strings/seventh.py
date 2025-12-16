text = input("Enter a sentence: ")

words = text.split()

if words:
    # Find the longest word
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")
else:
    print("No words found.")

    
