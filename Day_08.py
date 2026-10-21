#Build a program that asks the user to enter a sentence and analyses it.

sentence=input("Enter a sentence")
print("Original sentence:",sentence)
print("Uppercase:",sentence.upper())
print("Lowercase:",sentence.lower())
print("Character count:",len(sentence))
print("First Character:",sentence[0])
print("Last Character:",sentence[-1])
print("First three characters:",sentence[0:3])
print("Reversed:",sentence[::-1])

search=input("Enter the word to search for")
print("Occurrences:", sentence.lower().count(search.lower()))