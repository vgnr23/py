file1=open(r'myfile.txt')
v,c,u,l=0,0,0,0
str1=file1.read()
for i in str1:
    if(i>='a' and i<='z'):
        l+=1
    elif(i>='A' and i<='Z'):
        u+=1
for j in str1:
    j=j.lower()
    if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
        v+=1
    else:
        if j.isalpha():
            c+=1

print("lowercase count:",l)
print("uppercase count:",u)
print("vowels count:",v)
print("consonants count:",c)
