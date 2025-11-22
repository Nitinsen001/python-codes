# a,b=5,15
# a=a-b
# b=a+b
# a=b-a
# print(a,b)

# a=15

# print(str(a)[::-1])
# or




# b=55 now print(b)and output are give 10

# b=55
# b=b%10
# print(b+b)
# s=set()
# print(type(s))

# a=15
# b=a%2
# print("if there result are  true then number is even else its odd : ",b==0)

# Example of map in Python
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print("Squared numbers:", squared)

# Simple calculator program
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /): ")

# if operator == '+':
#     print("Result:", num1 + num2)
# elif operator == '-':
#     print("Result:", num1 - num2)
# elif operator == '*':
#     print("Result:", num1 * num2)
# elif operator == '/':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid operator")

# Simple user authentication program with options
# username = input("Enter username: ")
# password = input("Enter password: ")

# print("Choose an option:")
# print("1. Login")
# print("2. Exit")
# print("3. Reset Password")

# option = input("Enter your choice (1/2/3): ")

# if option == '1':
#     # Replace 'admin' and '1234' with desired credentials
#     if username == "babubhai" and password == "1234":
#         print("Login successful!")
#     else:
#         print("Invalid username or password.")
# elif option == '2':
#     print("Exiting program.")
# elif option == '3':
#     newpassword = input("Enter new password: ")
#     password = newpassword
#     print("Password has been reset.")
# else:
#     print("Invalid option.")


# def f1(a):
#     if a<=0:
#        return 0
#     print(a)
#     return f1(a-1)
# f1(10)

# data = [123,34,45,67]
# def f2(a,data):
#     if a == 4:
#         return 
         
#     print(data[a])
#     return f2(a+1,data)
# f2(0,data)


data = [123,34,5,5,45,34,67]
l = []
def f2(a):
    if a == len(data):
        return
  
    if data[a] not in l:
            l.append(data[a])
    return f2(a+1)

f2(0)
print(l)