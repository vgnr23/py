def fun(n):
    i = 1
    sum = 0
    while i <= n :
        sum += i ** 2
        i += 1
    print("Sum =", sum)

n = int(input("Enter the value of n: "))
fun(n)
