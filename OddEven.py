num= input("Enter a number: ")
last_digit=num[-1]
if last_digit in "02468":
    print(num,"is an even number")
elif last_digit in"13579":
    print(num,"is an odd number")
else:
    print("invalid input")

print("By Kaushal")