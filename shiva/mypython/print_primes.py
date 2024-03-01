def is_prime (n):
    condition = True
    if n != 2:
        if n%2 == 0:
            condition = False
        else:
            m = int(n/2)
            while m > 2:
                if n%m == 0:
                    condition = False
                    break
                m += -1
    return condition

def primes(n):
    m = 1
    while n >= 1:
        if is_prime(m) == True:
            print(m)
            n += -1
        m += 1
    return None

n = int(input("Please enter the number of primes: "))

primes(n)
