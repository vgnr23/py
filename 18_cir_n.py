no_of_terms = int(input("Enter number of values : "))

#Read values
list1 = []
for val in range(0,no_of_terms,1):
    ele = int(input("Enter integer : "))
    list1.append(ele)



#Circulate and display values
print("Circulating the elements of list ", list1)
   
for val in range(0,no_of_terms,1):
    ele = list1.pop(0)
    list1.append(ele)
    print(list1)

