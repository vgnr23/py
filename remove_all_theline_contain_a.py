file1=open("myfile.txt")
file2=open("mynew.txt","w+")
for i in file1:
    if 'a' in i:
        i=i.replace('a',' ')
        file2.write(i)
    else:
        file2.write(i)
file1.close()   
file2.close()
f=open("mynew.txt",'r')
print(f.readlines())
