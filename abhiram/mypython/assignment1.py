#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.1
def sum_of_digits(number):
    digit1 = number//100
    digit2 = (number//10) % 10
    digit3 = number%10
    
    
    sum = digit1+digit2+digit3
    return sum

number = int(input("Enter a three digit number"))
result = sum_of_digits(number)
print("Sum of digits of the given number is: ",result)


# In[ ]:


#1.2
def reverse_of_number(num):
    digit1 = num//100
    digit2 = (num//10) % 10
    digit3 = num%10
    
    reverse= digit3*100+digit2*10+digit1
    return reverse
num = int(input("Enter a 3 digit number"))
result = reverse_of_number(num)
print("The reverse of the given number is: ",result)


# In[11]:


#1.3
def palindrome(num):
    digit1 = num//100
    digit2 = (num//10) % 10
    digit3 = num%10
    
    reverse= digit3*100+digit2*10+digit1
    return reverse

num = int(input("Enter a 3 digit number"))
result = palindrome(num)

if num == result:
    print("The number is a palindrome ")
else:
    print("Not a palindrome")


# In[ ]:


#1.4

1,3,12.5


# In[15]:


#1.5
def check_promotion(subjects):
    if subjects[0] >= 35:
        if subjects[1] >= 35:
            if subjects[2] >= 35:
                return True
    else:
        return false

S1 = int(input("Enter marks for subject S1: "))
S2 = int(input("Enter marks for subject S2: "))
S3 = int(input("Enter marks for subject S3: "))

if check_promotion([S1, S2, S3]):
    print("Promoted")
else:
    print("Not Promoted")


# In[18]:


i = 0
n = 7
for i in range(0, n):
 print (i)
print (i)


# In[20]:


i = 0
n = 7
while(i < n):
 print (i),
 i += 1
print (i)


# In[25]:


i = 0
n = 10
for i in range(1, n+1, 2):
 print (i)
print (i)


# In[26]:


i = 1
n = 10
while( i <= n):
 print (i)
 if (i % 5 == 0):
   i += 4
 i = i + 1
print (i)


# In[27]:


i = 1
j = 1
while (i <= 5):
  print (i),
  j = 1
  while (j <= 5):
    print (j),
    j += 1
  print ("")
  i += 1
print (i, j)


# In[1]:


i = 1
j = 1
while (i <= 5):
 print (i),
 j = 1
 while (j <= 5):
  print (j),
  if (j%2 == 0):
    i += 2
  j += 1
 print ("")
 i += 1
print (i, j)


# In[3]:


#3-1 Fibonacci series
def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_series = [0, 1]  # Initialize the Fibonacci series with the first two terms
        sum_terms = 1  # Initialize the sum of terms with the first term (0 + 1 = 1)

        # Generate the Fibonacci series up to n terms
        for i in range(2, n):
            next_term = fib_series[-1] + fib_series[-2]  # Calculate the next term
            fib_series.append(next_term)  # Append the next term to the series
            sum_terms += next_term  # Add the next term to the sum

        return sum_terms

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Calculate and print the sum of the first n terms of the Fibonacci series
print("Sum of the first", n, "terms of the Fibonacci series:", fibonacci_sum(n))


# In[4]:


#3-2 factorial of n

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input the number
n = int(input("Enter a non-negative integer: "))

# Calculate and print the factorial
print("Factorial of", n, "is", factorial_recursive(n))


# In[7]:


#3-3 and 3-4 check is a number is prime or not and print first n prime numbers

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def first_n_primes(n):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

# Input the value of n
n = int(input("Enter the value of n: "))

# Print the first n prime numbers
print("First", n, "prime numbers are:", first_n_primes(n))


# In[8]:


#3-5
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def first_n_primes(n):
    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

def sum_of_primes(n):
    primes = first_n_primes(n)
    return sum(primes)

# Input the value of n
n = int(input("Enter the value of n: "))

# Print the sum of the first n prime numbers
print("Sum of the first", n, "prime numbers:", sum_of_primes(n))


# In[12]:


#3-6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input the value of n
n = int(input("Enter the value of n: "))

# Print the factorial values from 1 to n
print("Factorial values from 1 to", n, "are:")
for i in range(1, n + 1):
    print(i, "!", "=", factorial(i))


# In[14]:


#3-7
sum_factorials = sum(factorial(i) for i in range(1, n + 1))
# Print the sum
print("Sum of factorials from 1 to", n, "is:", sum_factorials)


# In[15]:


#3-8
# Input the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum of the expression
sum_expr = sum(i + 1 for i in range(1, n + 1))

# Print the sum
print("Sum of the expression from 2 to", n + 1, "is:", sum_expr)


# In[6]:


#3-9
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i, end=" ")

# Print numbers from 4 to 1
for i in range(4, 0, -1):
    print(i, end=" ")


# In[7]:


#3-10
# Outer loop for the number of lines
for i in range(5, 0, -1):
    # Inner loop for printing numbers on each line
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Print newline after each inner loop


# In[32]:


#3-11
# Outer loop for the number of lines
for i in range(5, 0, -1):
    # Print spaces before the numbers
    print(" " * (5 - i), end="")
    # Inner loop for printing numbers on each line
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Print newline after each inner loop


# In[8]:


#3-12
# Outer loop for the number of lines
for i in range(1, 6):
    # Inner loop for printing numbers on each line
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Print newline after each inner loop


# In[33]:


#3-13
# Outer loop for the number of lines
for i in range(1, 6):
    # Print spaces before the numbers
    print(" " * (5 - i), end="")
    # Inner loop for printing numbers on each line
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Print newline after each inner loop


# In[1]:


#4-1
def replace_duplicates(arr):
    encountered = {}
    for i in range(len(arr)):
        if arr[i] in encountered:
            arr[i] = 0
        else:
            encountered[arr[i]] = True

# Example usage:
arr = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8]
print("Original array:", arr)
replace_duplicates(arr)
print("After replacing duplicates:", arr)


# In[37]:


#4-2
def remove_duplicates(arr):
    frequency = {}
    unique_elements = []
    for num in arr:
        if num not in frequency:
            frequency[num] = 1
            unique_elements.append(num)
    return unique_elements

# Example usage:
arr = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8]
print("Original array:", arr)
unique_arr = remove_duplicates(arr)
print("Array after removing duplicates:", unique_arr)


# In[38]:


#4-3
# Input the number of elements and the array from the user
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Sort the array using the sorted() function
sorted_arr = sorted(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)


# In[39]:


#4-4
def add_matrices(a, b):
    # Get the dimensions of the matrices
    m = len(a)  # Number of rows
    n = len(a[0])  # Number of columns

    # Initialize the result matrix c with zeros
    c = [[0] * n for _ in range(m)]

    # Perform matrix addition
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c

# Input the dimensions of the matrices
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Input elements of matrix 'a'
print("Enter elements of matrix 'a':")
a = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(m)]

# Input elements of matrix 'b'
print("Enter elements of matrix 'b':")
b = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(m)]

# Add the matrices
c = add_matrices(a, b)

# Print the result matrix 'c'
print("Resultant matrix 'c' after addition:")
for row in c:
    print(row)


# In[10]:


variable = 10
print(f'The value of variable is {variable}')


# In[4]:


string1 = "Hello"
string2 = "World"
result = string1 + ", " + string2 + "!"
print(result)


# In[ ]:




