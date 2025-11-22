# Write a Python program to reverse a string using recursion.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


string = "hello"
print("Reversed String:", reverse_string(string))

# Write a Python program to find the sum of digits of a number using recursion.

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


num = 1234
print("Sum of digits:", sum_of_digits(num))

# Write a Python program to print the Fibonacci series up to n terms using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


terms = 7
print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")

# Write a Python program to count the number of digits in a number using recursion.

def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

num = 12345
print("Number of digits:", count_digits(num))
