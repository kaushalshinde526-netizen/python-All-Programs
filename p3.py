# WAPP to print numbers from 1 to n

n = int(input("Enter a number "))

if n > 0:
    i = 1
    while i <= n:
        print(i)
        i = i + 1
else:
    print("Enter a positive number")