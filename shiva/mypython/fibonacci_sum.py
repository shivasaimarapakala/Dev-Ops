def fibonacci_sum (n):
    a = 1
    b = 1
    sum = 2
    if n <=2:
        sum = n
    else:
        for i in range(n-2):
            nth_term = a+b
            a = b
            b = nth_term
            sum += nth_term
    
    return sum

print("******************")
print("This program prints the sum of the first n numbers in the fibonacci series")
print("******************")
n = int(input("Please enter the number of terms: "))
print(fibonacci_sum(n))