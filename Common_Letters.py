#WAPP TO find out common letters betwwen two strings.
#name:naina
#name2: reena
def common_letters():
    str1=input("Enter First Name : ")
    str2=input("Enter Second Name : ")
    s1=set(str1)
    s2=set(str2)
    common=s1.intersection(s2)
    print("Common letters are : ",common)   
common_letters()
