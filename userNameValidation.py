username = input("Enter username: ")

if len(username) >= 5 and " " not in username:
    valid = True
    for ch in username:
        if not (ch.isalnum() or ch == "_"):
            valid = False
            break

    if valid:
        print("Valid Username")
    else:
        print("Invalid Username")
else:
    print("Invalid Username")
    print("By Kaushal")