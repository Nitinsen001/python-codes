# 🧩 PRACTICE SET 1

# ==========================================================
# SECTION 1 – FUNCTIONS
# ==========================================================

# 1. Define a function that prints your name.
def my_name():
    print("Nitin")

# 2. Define a function that takes two numbers and prints their sum.
def add_numbers(a, b):
    print("Sum:", a + b)

# 3. What keyword is used to define a function in Python?
# 👉 Answer: The keyword used is 'def'.

# ----------------------------------------------------------
# B. Positional and Default Arguments
# ----------------------------------------------------------

# 4. Write a function to calculate the area of a rectangle (length, width).
def area_rectangle(length, width):
    area = length * width
    print("Area of rectangle:", area)

# 5. Write a function welcome(name="Guest") that prints a welcome message.
def welcome(name="Guest"):
    print("Welcome,", name)

# 6. What happens if you pass fewer or more positional arguments?
# 👉 Answer:
# Fewer arguments → TypeError (missing positional argument)
# More arguments  → TypeError (too many positional arguments)

# ----------------------------------------------------------
# C. Local and Global Variables
# ----------------------------------------------------------

# 7. Program showing local and global variables with same name.
x = 10  # global variable
def show():
    x = 5  # local variable
    print("Inside function:", x)
show()
print("Outside function:", x)

# 8. How can you modify a global variable inside a function?
# 👉 Answer: Use the 'global' keyword.
count = 0
def modify():
    global count
    count += 1
    print("Inside function:", count)
modify()
print("Outside function:", count)

# 9. What happens if you try to access a local variable outside a function?
# 👉 Answer: It gives NameError (variable not defined outside function scope)

# ----------------------------------------------------------
# D. Use of Return
# ----------------------------------------------------------

# 10. Write a function that returns the product of two numbers.
def multiply(a, b):
    return a * b

# 11. Create a function that returns both sum and difference of two numbers.
def sum_and_diff(a, b):
    return a + b, a - b
result = sum_and_diff(10, 5)
print("Sum and Difference:", result)

# 12. What will happen if a function has no return statement?
# 👉 Answer: It automatically returns 'None'.

# ----------------------------------------------------------
# E. Nested Functions & Function Calling
# ----------------------------------------------------------

# 13. Write a function outer() that defines and calls an inner() function.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()

# 14. Program where one function calls another function inside it.
def greet():
    print("Hello!")
def welcome():
    greet()
    print("Welcome to Python!")
welcome()

# 15. Create a function that returns the square of the sum of two numbers using another function.
def add(a, b):
    return a + b
def square_of_sum(x, y):
    return add(x, y) ** 2
print("Square of sum:", square_of_sum(2, 3))

# ----------------------------------------------------------
# F. Function Calling in Variables
# ----------------------------------------------------------

# 16. Store a function’s return value in a variable and print it.
def cube(n):
    return n ** 3
result = cube(4)
print("Cube is:", result)

# 17. Pass a variable (that stores function result) to another function.
def double(n):
    return n * 2
def show_value(value):
    print("Value is:", value)
res = double(5)
show_value(res)

# 18. Can a function call another function in its return statement?
# 👉 Answer: Yes, a function can call another function in its return.
def square(n):
    return n * n
def cube(n):
    return n * square(n)
print("Cube:", cube(3))

# ----------------------------------------------------------
# G. Based on Parameter Type
# ----------------------------------------------------------

# 19. Write one example each of:
# • Function with no parameter
# • Function with parameter
# • Function with default value
# • Function with return
# • Function without return

# Function with no parameter
def say_hello():
    print("Hello!")

# Function with parameter
def greet_person(name):
    print("Hello,", name)

# Function with default value
def welcome_user(name="Guest"):
    print("Welcome,", name)

# Function with return
def add_nums(a, b):
    return a + b

# Function without return
def subtract_nums(a, b):
    print("Difference:", a - b)

# 20. Explain the relationship between default and local argument values with example.
# 👉 Answer:
# If a function has a default value but a local value is passed, 
# then the local value overrides the default one.

def greet_example(name="Guest"):
    print("Hello,", name)

greet_example()        # uses default "Guest"
greet_example("Nitin") # overrides default

# ==========================================================
# SECTION 2 – WRITE OUTPUT
# ==========================================================

# Q1.
def greet():
    print("Hello, welcome to Python!")
greet()
# Output:
# Hello, welcome to Python!

# Q2.
def add(a, b):
    print("Sum is:", a + b)
add(10, 20)
# Output:
# Sum is: 30

# Q3.
def greet(name="User"):
    print("Hello,", name)
greet()
greet("Shekhar")
# Output:
# Hello, User
# Hello, Shekhar

# Q4.
x = 10  # global
def show():
    y = 5  # local
    print("Inside:", x, y)
show()
print("Outside:", x)
# Output:
# Inside: 10 5
# Outside: 10

# Q5.
count = 0
def increase():
    global count
    count += 1
increase()
print(count)
# Output:
# 1

# Q6.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
# Output:
# Outer function
# Inner function

# Q7.
def add(a, b):
    return a + b
result = add(10, 5)
print("Result:", result)
# Output:
# Result: 15

# Q8.
def square(n):
    return n * n
def cube(n):
    return n * square(n)
print(cube(3))
# Output:
# 27

# Q9.
def add(a, b):
    return a + b
def multiply_sum(x, y):
    return add(x, y) * 10
print(multiply_sum(2, 3))
# Output:
# 50

# Q10.
def greet(name):
    return "Hello " + name
message = greet("Shekhar")
print(message)
def display(msg):
    print("Message:", msg)
display(message)
# Output:
# Hello Shekhar
# Message: Hello Shekhar
