n = int(input("Enter a number: "))
if n == 1 or n == 0:
    print("Factorial of ",n, " is 1")
elif n < 0:
    print("Enter a positive number!!!")
else:
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n- 1)
    fact = 1
    fact = factorial(n)
    print("Factorial of ",n," is ",fact)

# else:
#     for i in range(1,n + 1):
#         fact = fact * i
#     print("Factorial of ",n," is ",fact)