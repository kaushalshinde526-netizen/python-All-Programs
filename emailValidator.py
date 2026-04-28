email = input("Enter email: ")

if email.count("@") == 1 and "." in email and " " not in email:
    print("Valid Email")
else:
    print("Invalid Email")