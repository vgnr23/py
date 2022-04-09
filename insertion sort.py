def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
alist = []
n=int(input("enter the upper limit"))
print("enter",n,"numbers")
for i in range(0,n):
    x=int(input())
    alist.append(x)
insertionSort(alist)
print("The Sorted list are")
print(alist)
