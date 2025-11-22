

'''decorator function'''
# def display(func):
#     def wrapper(*args, **kwargs):
#         print("before calling the function")
#         result = func(*args, **kwargs)
#         print("after calling the function")
#         return result
#     return wrapper

# @display
# def f1(n):
#     print("inside the function f1", n)

# sir ka logic
#  logic h  ki jo decorater mera displayy vala finction vo mere f1 functionn ko as a argument lega or uske andar ek wrapper function h jo ki mere f1 function ko call karega or uske pehle or baad me kuch print karega ager me f1 function ke under koi perameter pass karna chahta hu to mera display ke under function as argument ayega or wrapper function jo h vo jo f1 ke argument h unko lega or unme jo opperation kerna h vo karva ke ham return bhi ker sakte h ya unhe yha pe print bhi ker sakte h me ek or code likh rha hu iske nichee usme mene y logic likha h 
# def display(func):
#     def wrapper():
#         print("before calling the function")
#         func()
#         print("after calling the function")
    
#     return wrapper

# @display
# def f1(n):
#     print("inside the function f1", n)

# f1(1)


# #  yha pe wrapper function kya karea vo
# def display(func):
#     def wrapper(n,x):
#         print("before calling the function")
#         func(n,x)
#         print("after calling the function")
#         print(n+x)
    
#     return wrapper

# @display
# def f1(n,x):
#     print("inside the function f1", n)

# f1(1,2)


'''multiply decorater'''

def multiply(func):
    def wrapper(a,b):
        func(a,b)
        print (f"multiply of {a} and {b} is ",a*b)
        print (f"addition of {a} and {b} is ",a+b)
    return wrapper

@multiply
def main(a,b):
    print("main function")
    
main(2,3)


''' nonlocal '''
# def f1():
#     a=20# nonlocal for f2() and local for f1()
#     def f2():
#         a=90
#     f2()
#     return a
# print(f1())# 20


#  use nonlocal
# def f1():
#     a=20# nonlocal for f2() and local for f1()
#     def f2():
#         nonlocal a
#         a+=90
#     f2()
#     return a
# print(f1())# 110
# def foo(a, b, *, c=10, **kwargs):
#     print(a, b, c, kwargs)
# foo(1,2, d=4, e=5)

# def outer(f):
#     def inner(*args, **kwargs):
#         print("Before call")
#         result = f(*args, **kwargs)
#         print("After call")
#         return result
#     return inner

# @outer
# def add(a,b):
#     return a+b
# print(add(3,4))

def outer():
       x = 'hello'
       def inner():
           print(x)
       inner()
outer()