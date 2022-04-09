def search(alist,item):
    pos=0
    found=False
    stop=False
    while pos<len(alist) and not found and not stop:
        if alist[pos]==item:
            found=True
            print("element found in position",pos)
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    return found
a=[]
n=int(input("enter the upper limit:"))
print("enter",n,"numbers")
for i in range(0,n):
    e=int(input())
    a.append(e)
x=int(input("Enter element to search"))
search(a,x)
