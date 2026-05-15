#WAPP to chant hr hr rr "n" times and we have to count number of time repeatation
from time import sleep
n=int(input("Enter a chant: "))
if n>0:
    i=1
    c=1
    while i<=n:
        print("hr hr rr")
        i=i+1
        c=c+1
    print("number of repeatation is ",c-1)
    sleep(1)
else:
    print("invalid input")

        
