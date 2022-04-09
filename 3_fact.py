def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num =int(input("Enter a number:"))
print("Factorial value:",fact(num))
