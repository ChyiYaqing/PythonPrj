"""
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8...
The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
This means to say the nth term is the sum of (n-1)th and (n-2)th term.
"""
import math


# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
# change this value for a different result
nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 2

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    print(n1,",",n2,end=', ')
    while count < nterms:
        nth = n1 + n2
        print(nth,end=' , ')
        # update values
        n1 = n2
        n2 = nth
        count += 1

"""
Check input that belong to Fibonacci numbers in Python
https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
    --Recognizing Fibonacci numbers--
The question may arise whether a positive integer x is a Fibonacci number.This is true if and only if one or both of
5x^2 + 4 or 5x^2 -1 is a perfect square.
"""
def is_fibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return abs(round(a) - a) < 1.0 / n

number = int(input("\nCheck number is a fibonacci: "))
print(is_fibonacci(number))

"""
Possibly a not very efficient solution Check input that belong to Fibonacci numbers in Python
"""
def fibs():
    a,b = 0,1
    """
yield is deemed important when we are interested in resuming execution at the last point where the function (generator) exited,and where we are also interested in keeping the values of local variables between the 
    """
    yield a
    yield b
    while True:
        a,b = b, a+b
        yield b

n = int(input("please, enter a number "))
for fib in fibs():
    if n == fib:
        print("your number is a Fibonacci number!")
        break
    if fib > n:
        print("your number is not a Fibonacci number!")
        break

    
    
