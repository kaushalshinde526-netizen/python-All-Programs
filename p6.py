#WAPP to print sum of first "n" natural +ve integer
from time import sleep
n=int(input("Enter a number: "))
if n>0:
    i=1
    sum=0
    while i<=n:
        sum=sum+i
        i=i+1
    print("enter num",n,"sum = ",sum)
        

else:
    print("invalid input")