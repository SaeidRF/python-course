def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return n * factorial(n - 1)

number = 5
print("The factorial of",number,"is", factorial(number))