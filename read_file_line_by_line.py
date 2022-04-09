file1=open("myfile.txt",'r')
lines=file1.readlines()
count=1
for i in lines:
    print(f"line{count}:{i.strip()}")
    count+=1
