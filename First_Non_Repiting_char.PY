text = input("Enter string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating:", ch)
        break
else:
    print("No unique character")