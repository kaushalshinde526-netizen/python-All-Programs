name = input("Enter a name : ")
if name == name[::-1]:
    print("The name is a palindrome" , name)
else:
    print("The name is not a palindrome" ,name )