def factorial(n):
    print(f"n :{n}")
    
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

if __name__ == "__main__":
    n = 5
    t = factorial(n)
    print(f"fact value of {n} is {t}")
