file = open("books/frankenstein.txt", "r")

content = file.read()

words = content.split()

word_count = len(words)

print(word_count)

file.close()