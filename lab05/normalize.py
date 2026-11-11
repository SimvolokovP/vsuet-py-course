text = input("Enter text: ")
length = len(text)

words = text.split()
normalized_text = " ".join(words)

new_length = len(normalized_text)
word_count = len(words)

print(f"Original length: {length}")
print(f"New length: {new_length}")
print(f"Normalized text: {normalized_text}")
print(f"Word count: {word_count}")
