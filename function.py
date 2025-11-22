# function = function is a reuseable peace of code 
# it is reduced number of lene of code 

# def first():
#     pass

# def hello():
#     print("hello nitin , what's up bruuuuuuuuuuuuuuuuuu")
    
# hello()


# data=[1,2,3,4]
# def reverse_list():
    # print(data[::-1])
    # or 
    # print(data.reverse(),data)
    # or 
#     for i in reversed(data):
#         print(i)
# reverse_list()

# by pass the argument 

# def f1(data):
#     for i in reversed(data):
#         print(i,end=" ")
        
# f1([1,2,3,4])


# def f2(a,b):
#     print(a)
# f2(10,20)

# def f3(a,b=20):
#     print(a,b)
# f3(10)

# def f4(a,b):
#     print(b)
# f4(b=10,a=20)

# def table(a):
#     for i in range(1,11):
#         print(i*a,end=" ")


# table(int(input("eneter the no for table")))

# def reverse_string(s):
#     for i in range(len(s)-1,-1,-1):
#         print(s[i],end=" ")
#     or
#     a=' ' 
#     for i in s:
#         a=i+a
    # print(a)
# reverse_string("jatin")

# def febonachi(a,b):
#     print(a,b,end=' ')
#     n = int(input("enete a no you want the range : "))
#     for i in range(n):
    
#         c=a+b
#         a=b
#         b=c
#         print(b,end=" ")
# febonachi(0,1)


# def factorial(a):
#     if a== 1 or a==0:
#         return 1
    
#     return a*factorial(a-1)
# print(factorial(int(input("enter the no : "))))

# def demo1(n):
#     return n*n
# print(demo1(5))
# def demo2(n):
#     print( n*n*n)
# demo2(5)
# def demo3():
#     print("hello nitin")
# demo3()
# def demo4():
#     return "hello nitin"
# print(demo4())



# strs = ["act","pots","tops","cat","stop","hat"]

# # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# new=[]

# for i in strs:
#     a=[]
  
#     for j in strs:
#         if sorted(i) == sorted(j):
#             a.append(j)
#     if a not in new: 
#         new.append(a)    
# print(new)




# nums = [1,2,2,3,3,3]

# # Output: [2,3]
# new=[]

# for i in nums:
#     for j in nums:
#         if nums.count(i)>1:
#             if i not in new:
#                 new.append(i)
# print(new)
        
#  here lambda function

# c=lambda x,y:x*y
# print(c(5,6))

# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, numbers))
# print(squares)  # [1, 4, 9, 16, 25]


# numbers = [10, 15, 20, 25, 30]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_nums)  # [10, 20, 30]

# students = [("Nitin", 7.41), ("Amit", 8.5), ("Raj", 6.9)]
# # sort by CGPA
# sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
# print(sorted_students)  
# # [('Amit', 8.5), ('Nitin', 7.41), ('Raj', 6.9)]


# list complehanstion
# data = [x for x in range(1,11) if x%2==0]
# print(data)

# output = [*1*,**2**,***3***]
# data1=["*"*i+str(i)+"*"*i for i in range(1,4)]
# print(data1)

# for i in range(1,4):
#     print("*"*i+str(i)+"*"*i)


# now nested list comprestion
# General Syntax (nested for in list comprehension)

# [ expression for item1 in iterable1 for item2 in iterable2 ... if condition ]



# result = [(i, j) for i in range(3) for j in range(3)]
# print(result)
# # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


# table = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
# print(table)
# Output: ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3', '2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', '3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9']


# data = (lambda x:x**2,4)
# print(data)

# nums= [1,1,1,3,3,2,2,2,2,4]
# new=[]
# for i in nums:
#     for j in nums:
#         if nums.count(i)>1:
#             if i not in new:
#                 new.append(i)
# new=sorted(new)
# print(new[-1])

'''
RECURSION
'''
# def f(n):
#     print(n)
#     return f(n+1)
# f(1)

# def f1(n):
#     print(n)
#     if n==10:
#         return 0
#     return f1(n+1)
# f1(1)



# def f2(n,sum=0):
#     sum+=n
#     if n==10:
#         print(sum)
#         return 0
#     return f2(n+1,sum)
# f2(1)

# Factorial – Write a recursive function to calculate n!
# def factorial(n):
#     if n== 1 or n==0:
#         return 1
    
#     return  n*factorial(n-1)
# print(factorial(5))

# Sum of Natural Numbers – Find the sum of numbers from 1 to n recursively.
# def sum(n):
#     if n<1:
#         return 0
#     return (n) + sum(n-1)
# print(sum(5))

# Fibonacci Sequence – Print the first n Fibonacci numbers using recursion.
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# # Print first 10 terms
# for i in range(10):
#     print(fibonacci(i), end=" ")


# Power Function – Compute a^b using recursion (without using **).

# Reverse a String – Reverse a string recursively.


# print list number one by one
# l=[1,2,3,5]
# def l1(n):
#     print(l[n])
#     if n==len(l)-1:
#         return
     
#     return l1(n+1)
# l1(0)
        

'''
HIGH ORDERED FUNCTION
'''
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b

# def operation(a,b,c):
#     return c(a,b)
# print(operation(10,20,add))
# print(operation(10,20,sub))


# def compose(a,b,c):
#     return a(b(c))
# add_one = lambda x:x+1
# mul = lambda x:x*x
# div = lambda x: x/2
# a=compose(div,add_one,mul(2))
# print(a)





'''
MAP FUNCTION
'''
# def square(a):
#     return a*a
# data = [2,3,4,5]
# new = list(map(square,data))
# print(new)
# output = [4, 9, 16, 25]


# data = list(map(int,input().split()))
# print(data)


'''
filter FUNCTION
'''
# def filter_even(n):
#     return n%2==0
# data = list(filter(filter_even,[12,3,4,2,5,7]))
# print(data)

# data = ["cat","alpha","dog","beta","mat","doll"]
# def filter_length(n):
    
#     return len(n) == 3
# data = list(filter(filter_length,data))
# print(data)


'''
HIGH ORDER FUNCTION
 A function are pass as a argumnet on onather function is called high order function
'''
# def square(a):
#     return a**2
# def operation(a,b):
#     return a(b)
# print(operation(square,5))


# def square(a):
#     return a**2
# add = lambda a:a+2
# def operation(a,b):
#     return a(b)
# print(operation(add,5))


# def f(a=[]):
#     a.append(1)
#     print(a)
# f()
# f()# output = [1,1]

# def compose(a,b,c):
#     return a(b(c))


# add = lambda x:x+1
# square = lambda x:x*x
# print(compose(square,add,5))


'VARIABLE ARGUMENT FUNCTION'
'WE PARR MULTILE ARGUMENT AND ITS HOLD BY USING * IT MEAN ALL AND OUTPUTE ARE PRINT AS A TUPLE FORMAT'
# def add(*args):
#     print(args)
# add(1,2,3,4)

# def add_data(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# add_data(1,2,3)


# def even_no(*args):
#     for i in args:
#         if i % 2==0:
#             print(i)
# even_no(1,2,3,4,5,6)
    
    

# l = []
# def sum_even_no(*args):
    
#     for i in args:
#         if i % 2==0:
#             l.append(i)
#     return sum(l)
# print(sum_even_no(1,2,3,4,5,6))
    
    
    
    
'keyworrds argument function'
'it not a keyword you are allow to use any name'
'output are get in dicctionary format and pass argument in key and values payer'
'use **args'

# def data(**args):
#     print(args)
# data(a=10,b=11)# outpute = {'a': 10, 'b': 11}

# def data(**args):
#     args["c"]=30
#     print(args)
# data(a=10,b=11)# outpute ={'a': 10, 'b': 11, 'c': 30}

# def data(**args):
#     args["c"]=30
#     print(args)
# data(a=10,b=11,c=1000)# outpute ={'a': 10, 'b': 11, 'c': 30} local variable first priority

# def f1(**args):
#     return args["name"]
# print(f1(name='jit',age=28,staff=999))# utpute = jit



# def f1(**args):
#     args["name"] = "IIT"
#     print(args)#{'name': 'IIT', 'age': 28, 'staff': 999}
#     return args["name"]
# print(f1(name='jit',age=28,staff=999))# utpute = IIT



# def sumevenodd(a,b):
#     c=a+b
    
#     if c % 2==0:
#         return "even"
#     else:   
#         return "odd"
# print(sumevenodd(1,4))



# def f1(a,b):
#     return a+b
# print(f1(10,20))

# def f2(a,b):
#     print(a+b)
# f2(b=10,a=20)

# def f3(a=10,b=20):
#     print(a+b)
# f3()
# def f4(a=1,b=7):
#     return a+b
# print(f4())


# # we call the lambda function without identity
# # 1) single-arg lambda, turant call karke print
# print((lambda x: x * 2)(5))        # output: 10

# # 2) do-argument lambda
# print((lambda a, b: a + b)(7, 3))  # output: 10

# # 3) zero-argument lambda
# print((lambda: "Hello, Nitin!")()) # output: Hello, Nitin!

# # 4) conditional expression inside lambda
# print((lambda x: "Even" if x % 2 == 0 else "Odd")(11))  # output: Odd

# # 5) lambda used with map inside print (list banake print karein)
# print(list(map(lambda n: n**2, [1, 2, 3, 4])))  # output: [1, 4, 9, 16]

# # 6) nested call — lambda jo lambda return kare aur turant chain call ho
# print((lambda x: (lambda y: x + y))(5)(10))  # output: 15

# # 7) lambda ke through dictionary key-sort example, directly print karna
# d = {'a': 3, 'b': 1, 'c': 2}
# print(sorted(d.items(), key=lambda item: item[1]))  # output: [('b', 1), ('c', 2), ('a', 3)]


# """ sort the list by the length of string element"""
# # useing lambda function
# data = ["ac","a","bat","ball","doll","cat"]
# data.sort(key=lambda x:len(x))
# print(data)


""" recursion"""
# def f1(n):
#     print(n)
#     if n == 100:
#         return
    
    
#     return f1(n+1)
# f1(1)


# def table(n):
#     print(n*2)
#     if n==11:
#         return
    
#     return table(n+1)
# table(1)

# def fact(n):
#     if n == 1:
#         return 1
    
#     return n*fact(n-1)
# print(fact(5))

# sum = 0

# def sum_of_even(n):
#     global sum 
#     if n == len(n):
#         return 0




# ============================================================================================================


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     sum = 0
#     while n != 0:
#         d = n % 10
#         sum += d
#         n //= 10
#     print(sum)
    
    
    
    
# Python Code
# # Read input values
# P1, P2, P3, P4 = map(int, input().split())

# # Count how many weeks Chef solved >= 10 problems
# count = 0
# for p in [P1, P2, P3, P4]:
#     if p >= 10:
#         count += 1

# print(count)   


# # sort version
# print(sum(p >= 10 for p in map(int, input().split())))
# a,b=0,1
# print(a,b,end=" ")
# for i in range(6):

#     c=a+b
#     a,b=b,c
#     print(c,end=" ")

# a = "abcd efgh igkl mnop"
# def reversse_string(*s):
#     new = []
#     for i in s[0].split():
#         new.append(i[::-1])
#     return new
# print(reversse_string("abcd efgh igkl mnop"))

""" yeild keyword function"""
# def f1():
#     yield 1
#     yield 2
#     yield 3
# f1()
# print(f1())# output = <generator object f1 at 0x7f8b8c0d4b80>
# print(next(f1()))# output = 1
# print(next(f1()))# output = 1

# # ager me sabko print karna chata hu to loop ka use karunga
# # for i in f1():
# #     print(i)

# #  without loop bhi kar sakta hu
# g = f1()
# print(next(g))# output = 1
# print(next(g))# output = 2
# print(next(g))# output = 3

# # yeild use karne ka fayda ye h ki ye memory me kam jagah leta h or bada data handle kar sakta h
# # jab ki return sara data memory me le leta h or bada data handle nhi kar pata h
# # ek se jyada value return karna h to yeild ka use karte h
# # yeild her bar starting se functio n ko nhi chalata h jb tak next() call nhi karte h
# # yeild function ko generator function bhi bolte h
# # yelid ka use tab karte h jb hume ek se jyada value return karna hota h
# # yeld function me state of function save ho jata h or next call pe wapas se wahi se start hota h jb ki return me function fir se starting se chalta h
# # yeild ka use karne se hum infinite sequence bhi create kar sakte h jb ki return me nhi kar sakte h
# # yeild function pure function ko dobara se run nhi kerta vo next step se chalta h bulki return from starting se chalta h
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# counter = count_up_to(5)
# print(next(counter))  # Output: 1
# print(next(counter))  # Output: 2


# def counteres(n):
#     while n>0:
#         yield n
#         n-=1
# for x in counteres(5):
#     print(x,end=" ")

# x = 10
# def f():
#     print(x)
#     x = 5

# f()
# # UnboundLocalError: local variable 'x' referenced before assignment



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

# def multiply(func):
#     def wrapper(a,b):
#         func(a,b)
#         print (f"multiply of {a} and {b} is ",a*b)
#         print (f"addition of {a} and {b} is ",a+b)
#     return wrapper

# @multiply
# def main(a,b):
#     print("main function")
    
# main(2,3)


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

# def outer():
#        x = 'hello'
#        def inner():
#            print(x)
#        inner()
# outer()

n = "ABC890hdd4iw"
# l = []

# for ch in n:
#     if ch.isdigit():     
#         l.append(ch)

# print(''.join(l)[::-1])  

print(int(''.join(reversed([ch for ch in n if ch.isdigit()]))))