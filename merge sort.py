def merge(left, right, Array):
    i,j,k = 0,0,0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            Array[k] = left[i]
            i = i+1
        else:
            Array[k] = right[j]
            j = j+1
        k = k+1
    while(i<len(left)):
        Array[k] = left[i]
        i = i+1
        k = k+1
    while(j<len(right)):
        Array[k] = right[j]
        j = j+1
        k = k+1
#function for dividing and calling merge function
def mergesort(Array):
    n = len(Array)
    if(n<2):
        return
    mid = n//2
    left = []
    right = []
    for i in range(mid):
        number = Array[i]
        left.append(number)
    for i in range(mid,n):
        number = Array[i]
        right.append(number)
    mergesort(left)
    mergesort(right)
    merge(left,right,Array)
#calling mergesort
Array = []
n=int(input("enter the upper limit"))
print("enter",n,"numbers")
for i in range(0,n):
    x=int(input())
    Array.append(x)
mergesort(Array)
print("The Sorted list are")
print(Array)
