def bsearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    mid=int((first+last)/2)
    while first<=last and not found:
        if alist[mid]==item:
            found=True
            print("element found in position",mid)
        else:
            if item<alist[mid]:
                last=mid-1
            else:
                first=mid+1
        mid=int((first+last)/2)
    if found==False:
        print("Element not found")
    return found
a=[]
n=int(input("Enter upper limit:"))
print("Enter ",n," numbers")
for i in range(0,n):
    e=int(input())
    a.append(e)
x=int(input("Enter element to search"))
bsearch(a,x)
