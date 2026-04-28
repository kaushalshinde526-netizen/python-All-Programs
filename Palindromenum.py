text = input("Enter string: ")

clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    print("By Kaushal")