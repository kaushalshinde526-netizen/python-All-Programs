# Given a string s containing lowercase alphabets and digits, 
# return a string of all missing digits (0-9) followed by all missing lowercase letters (a-z).
def missingCharacters(s):

    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for d in digits:
        if d not in s:
            result += d
            

    for ch in letters:
        if ch not in s:
            result += ch

    return result


s = input("Enter String: ")
print(missingCharacters(s))