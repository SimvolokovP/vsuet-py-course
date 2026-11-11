text = input("Enter text: ")

cleaned_text = text.lower().replace(" ", "")

if len(cleaned_text) == 0:
    print("Text empty")
    exit()

if cleaned_text == cleaned_text[::-1]:
    print("PALINDROM!!!")
else:
    print("no palindrom")

print("with pointers")

pointer1 = 0
pointer2 = len(cleaned_text) - 1

while pointer1 < pointer2:
    if cleaned_text[pointer1] != cleaned_text[pointer2]:
        print("no palindrom")
        exit()

    pointer1 += 1
    pointer2 -= 1

print("PALINDROM!!!")
