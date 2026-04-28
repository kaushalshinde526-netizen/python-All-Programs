amount = float(input("Enter amount: "))

if amount > 1000:
    discount = 0.2
elif amount >= 500:
    discount = 0.1
else:
    discount = 0

final_amount = amount - (amount * discount)

print("Final Amount:", final_amount)
print("By Kaushal")