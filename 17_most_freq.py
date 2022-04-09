fname = input("filename: ")
with open(fname, "w") as fh:
  fh.write(input("Enter file data:"))

  
fh = open(fname,'r')
freq = list()                       
words=[]
for line in fh:                    
    words += line.split()
words.sort()

print("The most freq words are:")

for word in words:
    if words.count(str(word))>1:
        if word not in freq:
            freq.append(word)
print(freq)
