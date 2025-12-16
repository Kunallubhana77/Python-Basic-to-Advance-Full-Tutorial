# Word frequency counter from a paragraph (use dict)

paragraph = "this is a test this is only a test python is great python is fun"
words = paragraph.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Paragraph:", paragraph)
print("Word Frequencies:", frequency)
