text = input("Enter text: ")

count = text.count(":")
new_text = text.replace(":", "-")

print(f"Number of replacements: {count}")
print(f"New text: {new_text}")