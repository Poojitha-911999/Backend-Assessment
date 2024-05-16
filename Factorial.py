def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = 6
print(f"The factorial of {num} is: {factorial(num)}")

num = 5
print(f"The factorial of {num} is: {factorial(num)}")

num = 4
print(f"The factorial of {num} is: {factorial(num)}")

num = 0
print(f"The factorial of {num} is: {factorial(num)}")

