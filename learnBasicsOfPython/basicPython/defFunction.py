def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


num = 7

if num < 0:
    print("No Factorial")
elif num == 0:
    print("Factoroial of 0 is 1")
else:
    print("factorial of ", num, "is", factorial(num))
