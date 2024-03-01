def factorial (n):
    fact = 1
    while n>= 1:
        fact = fact*n
        n += -1
    
    return fact

n = int(input("Please enter the number: "))
print(f"factorial of {n} is: {factorial(n)}")