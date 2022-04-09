fname = input("filename: ")
with open(fname, "w") as fh:
  fh.write(input("Enter file data:"))

  
fh = open(fname,'r')
unique = list()                       
words=[]
for line in fh:                    
    words += line.split()
words.sort()

print("The unique words in  alphabetical order are:")

for word in words:
    if words.count(str(word))==1:
        unique.append(word)
print(unique)
