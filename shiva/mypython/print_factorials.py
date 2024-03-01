def factorial (n):
    fact = 1
    while n>= 1:
        fact = fact*n
        n += -1
    
    return fact

def fact_print(n):
    i = 1
    while i <= n:
        print(factorial(i))
        i += 1
    return None

n = int(input("Please enter the number of terms: "))
fact_print(n)