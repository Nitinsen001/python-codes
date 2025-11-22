''' we have same magic method names as inbuilt methods but we are changing their functionality 
like __init__ , __str__ , __add__ etc
its used to give special functionality to our objects 
like when we print an object it gives the memory location but if we want to print some specific
information about the object we can use __str__ method to achieve that

'''

''' use of __init__ method
it is a constructor method which is called when we create an object of the class
it is used to initialize the instance variables of the class
it mean ksisi bhi application ko start kerte hi kuchh time lagta like loding iss time pe constructor kaam krta h kuchh file jo constructor me define h wo load ho jati h ya download hoti h'''

# class c1:
#     def __init__(self):
#         print("hello , i am constructor")
# obj=c1()

# class Student:
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno

#     def display(self):
#         return f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}"
    
# student1 = Student("nitin", 19, 45)# here we are passing the arguments to the constructor by use of class object
# print(student1.display())



''' use distructor method __del__
it is called when the object is destroyed or deleted'''
# class c1:
#     data = "hello"
#     def m1(self,a):
#         print("inside the method",a)
#     def __del__(self):
#         print("destructor called , object is being destroyed")
# obj=c1()
# print(obj.data)
# del obj.data # deleting the data attribute of the object
# print("after deleting data attribute")
# print(obj.data)# error aayega kyuki data attribute delete ho chuka h
# print(obj.m1(10))
# del obj.a # deleting the a attribute of the object but the instance method m1 is still there
# del obj # deleting the object
# print("after deleting the object")
# print(obj.data) # error aayega kyuki object delete ho chuka h




# class c:
#     def m1(self):
#         return "hello nitin"
#     def m2(self,a):
#         del self.a
#     def display(self):
#         print("inside display method",self.a)
# obj = c()
# obj.a = 10
# print("before deleting a",obj.a)
# obj.m2(obj.a)
# obj.display()# it will give error kyuki a delete ho chuka h


# class c2:
#     def __init__(self):
#         print("private data")
#     def __init__(self):
#         print("constructor called")
    
# o = c2()# output: constructor called



''' use of __str__ method '''
''' it is used to give a string representation of the object
when we print the object it will call the __str__ method and return the string representation of the object'''
# class c3:
#     def __init__(self,name,age):      
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
# obj = c3("nitin",19)

# print(obj) # it will call the __str__ method and return the string representation of the object

''' getattr() and setattr() magic methods '''
class c1:
    data =90
obj = c1()
print(getattr(obj,'data')) # it will return the value of the attribute data
setattr(obj,'data',100) # it will set the value of the attribute data to