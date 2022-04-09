n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
i = 1
sum = 1
while i <= n :
    t= 1/(x ** i)
    sum+=t
    i += 1
print("Sum =", sum)

