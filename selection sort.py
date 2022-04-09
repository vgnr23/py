def selectionSort(alist):
 for i in range(len(alist)-1,0,-1):
     pos = 0
     for location in range(1,i+1):
         if alist[location]>alist[pos]:
             pos=location
     temp = alist[i]
     alist[i]=alist[pos]
     alist[pos]=temp
alist = []
n=int(input("enter the upper limit"))
print("enter",n,"numbers")
for i in range(0,n):
    x=int(input())
    alist.append(x)
selectionSort(alist)
print("The Sorted list are")
print(alist)
