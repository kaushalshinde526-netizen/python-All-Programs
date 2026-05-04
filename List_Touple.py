mrks=[96.20,59.23,84.27,85.23,78.12]
print(type(mrks))
print("lenth show kar ",len(mrks))
print(mrks[1])
mrks[1]=60.00
print(mrks[1])
print(mrks)
##student record in printable format
students =["ram shastri",95.20,22,"bsc-cs","male","mumbai","+90224212356"]
print(students)
print(list(students))
print("Name of student :" ,students[0])
print("Marks of student :" ,students[1])
print("Age of student :" ,students[2])  
print("Course of student :" ,students[3])
print("Gender of student :" ,students[4])
print("City of student :" ,students[5])
print("Phone of student :" ,students[6])    
students[0]="shyam shastri" #update name of student is totaly mutable in list 
print(students)
#Python मध्ये slicing (स्लायसिंग) म्हणजे list (किंवा string, tuple) मधून काही specific भाग (subset) काढणे
my_list = [10, 20, 30, 40, 50, 60] #simpleslicing
print(my_list[1:4])
print(my_list[2:]) #start point slicing 
print(my_list[:4]) #end point slicing
print(my_list[:]) #full slicing
reversed_list = my_list[::-1] #reverse slicing
print(reversed_list)       
negative_step_list = my_list[::2] #negative step slicing
print(negative_step_list) 
#LIST METHODS
my_list.append(70) #append method add element at the end of list
print("After appending 70:", my_list)  
my_list.insert(2,25) #insert method add element at specific index
print("After inserting 25 at index 2:", my_list)                  
my_list.remove(40) #remove method remove element by value
print("After removing element 40:", my_list)
my_list.pop(3) #pop method remove element by index
print("After popping element at index 3:", my_list)
my_list.sort() #sort method sort the list in ascending order
print("Ascending order:", my_list)
my_list.sort(reverse=True) #sort method sort the list in descending order   
print("Descending order:", my_list)
my_list.clear() #clear method remove all elements from the list 
print("Cleared list:", my_list)
#1. Tuple reverse करा
t = (10, 20, 30, 40)
print("Original tuple:", t)
#2. Tuple मधून max element शोधा
t2 = (5, 15, 2, 40, 8)
print("Original tuple:", t2)
#3. Tuple मधून min element शोधा
t3 = (5, 15, 2, 40, 8)
print("Original tuple:", t3)
#4. Tuple length शोधा
t4 = (5, 15, 2, 40, 8)
print("Original tuple:", t4)    
#5. Tuple मध्ये specific element count करा
t5 = (5, 15, 2, 40, 8, 15, 5)
print("Original tuple:", t5)
#6. Tuple मधून duplicate elements काढा
t6 = (5, 15, 2, 40, 8, 15, 5)
print("Original tuple:", t6)    
#7. Tuple मध्ये element exist आहे का check करा
t7 = (5, 15, 2, 40, 8)
print("Original tuple:", t7)        
#8. Tuple concatenate करा
t8_1 = (1, 2, 3)
t8_2 = (4, 5, 6)        
print("Tuple 1:", t8_1)
print("Tuple 2:", t8_2)
t8_3 = t8_1 + t8_2
print("Concatenated tuple:", t8_3)  
#9. Tuple unpack करा
t9 = (10, 20, 30)
print("Original tuple:", t9)    
a, b, c = t9
print("Unpacked values:", a, b, c)
#10. Tuple slicing करा
t10 = (10, 20, 30, 40, 50)      
print("Original tuple:", t10)
print("Sliced tuple (index 1 to 3):", t10[1:4])
#11. Tuple मधून even numbers काढा
t11 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Original tuple:", t11)           
even_numbers = tuple(x for x in t11 if x % 2 == 0)
print("Even numbers:", even_numbers)        
#12. Nested tuple access करा
t12 = (1, 2, (3, 4), 5)
print("Original tuple:", t12)
print("Accessing nested tuple:", t12[2])
#13. Tuple मध्ये element count करा
t13 = (1, 2, 3, 4, 5, 2, 3)
print("Original tuple:", t13)           
count_2 = t13.count(2)
print("Count of element 2:", count_2)       
#14. Tuple मध्ये element index शोधा
t14 = (1, 2, 3, 4, 5)
print("Original tuple:", t14)       
index_3 = t14.index(3)
print("Index of element 3:", index_3)   
#15. Tuple मध्ये element exist आहे का check करा
t15 = (1, 2, 3, 4, 5)           
print("Original tuple:", t15)
element_to_check = 3
if element_to_check in t15:
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")
     


