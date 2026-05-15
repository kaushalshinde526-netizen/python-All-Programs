#WAPP To print numbers from 1 to n but the process should be slow
from time import sleep
n=int(input("Enter a number: "))
if n>0:
    i=1
    while i<=n:
        print(i)
        i=i+1
        sleep(0.5)
else:
    print("ivalid input")
