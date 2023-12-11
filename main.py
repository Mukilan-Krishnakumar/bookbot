from collections import Counter

lines = open("./books/frankenstein.txt").read().split("\n")
word_count = 0
characters = []
for line in lines:
    for word in line.split(" "):
        if word != "":
            for character in word:
                if character.isalpha():
                    characters.append(character.lower())

counter = Counter(characters)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
for key, val in counter.items():
    print(f"The '{key}' character was found {val} times")
print("--- End report ---")
