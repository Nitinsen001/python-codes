# feactures of oops
# therory
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
# example of oops
''' class : A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. Classes help in organizing code and promoting reusability.'''
# class Animal:
    # def __init__(self, name, species):
    #     self.name = name
    #     self.species = species

    # def make_sound(self):
    #     raise NotImplementedError("Subclasses must implement this method")
    
    
    
# method jo h vo self ke sath likhte h or function ko without self ke use hota h     

# class car:
#     color = "red"
#     model = 2020
#     def start_engine(self):
#         return "Vroom! Vroom!"
#     def run(self):
#         return "The car is running."
#     def stop(self):
#         return "The car has stopped."

# # we create a object of car class

# thar = car()

# print("my thar is having ",thar.color,"color")  # Accessing attribute
# # I WANT TO CHANGE THE COLOR OF THAR CAR
# thar.color = "Z-BLACK"
# print("my thar is having ",thar.color,"color")  # Accessing attribute

# spresso = car()
# # spresso ka colo channge nhi hua h kyuki mene thar ka color change kiya h spresso ka nhi
# print("my spresso is having ",spresso.color,"color")  # Accessing attribute

# """ we can access the class variables by class name also it mean classs name.variable name 
# if we change the value by class name it will change for all the objects of that class
# if there is no variable insite the class it will take from class variable"""

# print("car class color is ",car.color)  # Accessing attribute by class name
# car.color = "black"
# print("after changing car class color is ",car.color)  # Accessing attribute by class name
# print("my spresso is having ",spresso.color,"color")  # Accessing attribute

# "crrate a new variable insite the class by object name classname.variable "
# car.top_speed = 200
# print("car top speed is ",car.top_speed)  # Accessing attribute by class name
# print("spresso top speed is ",spresso.top_speed)  # Accessing attribute by




# class mobile:
#     brand = "Samsung"
#     model = "Galaxy S25 ultra"
#     color = "Phantom Black"
#     storage = "512GB"
#     proccessor = "Snapdragon 8 Gen 3"
#     ram = "12GB"
#     battery = "7000mAh"
#     price = "150000INR"
#     def make_call(self, number):
#         return f"Calling {number}..."
#     def send_message(self, number, message):
#         return f"Sending message to {number}: {message}"
# # we create a object of mobile class
# my_phone = mobile()
# print("My phone brand is", my_phone.brand)  # Accessing attribute
# print(my_phone.make_call("123-456-7890"))  # Calling method
# print(my_phone.send_message("123-456-7890", "Hello! phone uthaiye na!"))  # Calling method


''' New code '''
''' practice problem 1 : there is a real world scenario. You have to create the attributes and method to it. 
Take the example of your college.'''
# class College:
#     name = "jawaharlal institute of technology Borawan "
#     location = "Borawan, Madhya Pradesh"
#     established_year = 1995
#     courses_offered = ["Computer Science", "Mechanical Engineering", "Civil Engineering", "Electrical Engineering"]
#     principal = "Dr. Atul upadhyay"
    
#     def get_college_info(self,):
#         return f"{self.name}, located in {self.location}, was established in {self.established_year}."
    
#     def list_courses(self):
#         return f"Courses offered: {', '.join(self.courses_offered)}"
    
#     def get_principal_name(self):
#         return f"The principal of the college is {self.principal}."
# # creating an object of College class
# my_college = College()
# print(my_college.get_college_info())
# print(my_college.list_courses())    
# print(my_college.get_principal_name())

# # now abb update the values by using instance variable
# my_college.name = "JIT Borawan"
# print(my_college.get_college_info())






''' practice problem 2 : there is a real world scenario. You have to create the attributes and method to it.        
Take the example of a library.'''
# class Library:
#     name = "City Central Library"
#     location = "Downtown"
#     established_year = 1980
#     books_available = ["1984 by George Orwell", "To Kill a Mockingbird by Harper Lee", "The Great Gatsby by F. Scott Fitzgerald"]
#     librarian = "Ms. Jane Smith"
    
#     def get_library_info(self):
#         return f"{self.name}, located in {self.location}, was established in {self.established_year}."
    
#     def list_books(self):
#         return f"Books available: {', '.join(self.books_available)}"
    
#     def get_librarian_name(self):
#         return f"The librarian of the library is {self.librarian}."
    
# # creating an object of Library class
# my_library = Library()
# print(my_library.get_library_info())


''' instance variable update values directaly in class'''
# class Library:
#     name = "City Central Library"
#     location = "Downtown"
#     established_year = 1980
#     books_available = ["Machine learning", "IPS", "Data science"]
#     librarian = "Ms. Jane Smith"
    
#     def get_library_info(self):
#         return f"{self.name}, located in {self.location}, was established in {self.established_year}."
    
#     def list_books(self):
#         return f"Books available: {', '.join(self.books_available)}"
    
#     def get_librarian_name(self):
#         return f"The librarian of the library is {self.librarian}."
#     def add_book(self, book_name):
#         self.books_available.append(book_name)
#         return f'Book "{book_name}" added to the library.'
# # creating an object of Library class

# my_library = Library()
# print(my_library.list_books())
# print(my_library.add_book("Python Programming"))
# print(my_library.get_library_info())
# my_library.name = "Downtown Public Library"
# print(my_library.get_library_info())

""" inside the class outside the method we can create the variable"""
# class sample:
#     a = 10
#     b = 20
#     def display(self):
#         print("inside the method",self.a,self.b)
# obj = sample()
# print("outside the method",obj.a,obj.b)
# print(sample.a,sample.b)
# #  creating new variable outside the method inside the class

''' if there is no '''

# sample.new_data = "value added"
# print("new data is ",sample.new_data)
# print("new data by object is ",obj.new_data)



''' inside the method'''
# class c1:
#     a=10
#     def m1(self):
#         print(c1.a)
#         c1.b =20
#         print("inside the method",self.a,c1)
#         ''' update the outside variabels inside the method'''
#         c1.a+= 100
#         print(c1.a)
#         print(c1.b)
# obj = c1()
# obj.m1()

''' class attribute ko me method ke through bhi acces ker sakta hu but unme self ke throw modify nhi ker sakte actual vale ko  kyuki object to object value change hoti h lekin class attribute same rehta h sabhi object ke liye'''

# class c1:
#     a=10
#     def m1(self):
#         ''' ham yha mere class variable ko instance me conver ker rhe h '''
#         self.a+=100
#         print("inside the method",self.a)
        
# obj = c1()
# obj.m1()



''' classmethod decorater'''
# class c1:
#     a=10
#     @classmethod
#     def m1(cls):
#         cls.a+=100
#         print("inside the class method",cls.a)
#         ''' declare a class variable'''
#         cls.myvar={"name" : "nitin","cgpa" : 7.43}
#         print(cls.myvar["name"])
#         print(c1.myvar["name"])
#         print(obj.myvar["name"])
# obj = c1()
# obj.m1()

'''' now create a decorater to increase a value and it apply on classmethod '''

# def increase_value(func):
#     def wrapper(cls):
#         cls.a = func(cls.a)
#         return cls
#     return wrapper

# def increase(n):
#     return n + 1

# @increase_value(increase)
# class c1:
#     a = 20

#     @classmethod
#     def m1(cls):
#         print(cls.a)

# obj = c1()
# obj.m1()  # Output: 21

'''new one '''

# class increas:
#     a = 90
#     @classmethod
#     def m1(cls):
        
#         print(cls.a)
# @increas
# def idnc(cls):
#     cls.a += 1
#     print(cls.a)
# obj = increas()
# obj.m1()

''' using static method decorater'''
# class c1:
#     a=10
#     @staticmethod
#     def m1(): 
#         print("inside the static method",c1.a)
# obj = c1()
# obj.m1()

#  we cant access the class variable directaly inside the static method we have to use class name to access the class variable
# class c2:
#     a=50
#     @staticmethod
#     def m2():
#         c2.a+=50
#         print("inside the static method",c2.a)
# obj2 = c2()
# obj2.m2()


'''new one'''
# class c1:
#     a = 10
#     def m1(self):
#         print("inside the instance method",self.a)
# class c2:
#     def m2(self):
#         print("inside the instance method of c2",c1.m1())
# obj2 = c2()
# obj2.m2()




'''encapsulation'''
""" definationn: encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit or class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. This is typically achieved by making attributes private (using a leading underscore) and providing public methods to access and modify those attributes. Encapsulation helps in maintaining the integrity of the data and promotes modularity in code design. """
# class c1:
#     _data = "hello nitin"# partially private variable
#     def m1(self):
#         return self._data# accessing partially private variable by method
# obj = c1()
# print(obj.m1())
# print(obj._data) # ye access ho jayega but ye sahi practice nhi h
# # # making fully private variable
# class c2:
#     __data = "hello world" # fully private variable
#     def m2(self):
#         return self.__data# accessing fully private variable by method
# obj2 = c2()
# print(obj2.m2())# accessing fully private variable by method
# # print(obj2.__data) # ye access nhi hoga error aayega kyuki ye fully private variable h


'''  use of getter and setter method to access private variable'''
# class c1:
#     __data = "hello nitin"# fully private variable
#     def get_data(self):# getter method to access private variable
#         return self.__data
#     def set_data(self, value):# setter method to modify private variable
#         self.__data = value
# obj = c1()
# print(obj.get_data())# accessing private variable by getter method
# obj.set_data("hello world")# modifying private variable by setter method


# class c2:
#     __data = "hello world" # fully private variable
#     def getter(self):
#         return self.__data# accessing fully private variable by method
#     def __display(self):
#         return "this is a private method"
#     def setter(self, value):
#         self.__data = value# modifying fully private variable by method
#         return self.__data
# obj2 = c2()
# print(obj2.getter())# accessing fully private variable by method
# # print(obj2.__display()) # ye access nhi hoga error aayega kyuki ye fully private method h
# print(obj2.setter("new value"))# modifying fully private variable by method
''' now i want to access the private method'''
# print(obj2._c2__display())# accessing fully private method by name mangling

# class c1:
#     def m1(self):
#         print("inside the method")
#     def __display(self):
#         print("this is a private method")
#     def getter(self):
#         return self.__display()
# obj = c1()
# print(obj.getter())# accessing private method by public method


''' use accessmodifier to access private variable and method'''
# class c1:
#     __data = "hello nitin"# fully private variable
#     def __display(self):
#         return "this is a private method"

#     def access_private(self):
#         return self.__data, self.__display()  
# obj = c1()
# print(obj.access_private())# accessing private variable and method by public method




''' theory self is instance of the class it is used to access the attributes and methods of the class in python
it is the first parameter of the instance method it is used to refer to the current object of the class
it is used to differentiate between instance variables and local variables when they have the same name
it is used to access the class variables and methods from within the class
it is used to pass the current object as an argument to other methods within the class
it is used to return the current object from a method
it is used to access the instance variables and methods from outside the class using the object of the
class '''

'''1. declaring and accessing and modifiying instance variable using self keyword
2.self is used to call the method of your class'''


''' abstraction'''
''' Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. It helps in reducing complexity and increases efficiency by allowing the user to focus on interactions at a higher level. In object-oriented programming, abstraction is achieved through abstract classes and interfaces, which define a blueprint for other classes without providing a complete implementation. This allows for better code organization, easier maintenance, and improved scalability. '''
# from abc import ABC, abstractmethod
# class car(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def stop_engine(self):

#         pass
# class Tesla(car):
#     def start_engine(self):# yha pe start_engine method ka implementation kerna jarruri h kyuki mene car class me abstract method banaya h to vha jo banaya h uska implementation jaruri h h yha pe verna error aayega same for stop_engine method me bhi 
#         return "Tesla engine started silently.,brmmm...brmmm..."
#     def stop_engine(self):
#         return "Tesla engine stopped.,click...click..."

# my_tesla = Tesla()
# print(my_tesla.start_engine())



''' inheritance'''
''' Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a subclass or derived class) to inherit attributes and methods from an existing class (called a superclass or base class). This promotes code reusability and establishes a hierarchical relationship between classes. The subclass can extend or modify the functionality of the superclass by adding new attributes or methods, or by overriding existing ones. Inheritance helps in creating a more organized and modular code structure, making it easier to maintain and understand. '''

'''What is Inheritance? (Definition)

Inheritance is an object-oriented programming (OOP) concept in which one class (child/subclass) acquires the properties and behaviors (variables and methods) of another class (parent/superclass).
It helps with code reuse, reducing duplication, and building hierarchical relationships.'''


'''① Single Inheritance

 A child class inherits from only one parent class.'''
 
#  # Parent class
# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# # Child class (inherits from Animal)
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# obj = Dog()
# obj.sound()
# obj.bark()

'''② Multilevel Inheritance 
    A class inherits from a derived class, forming a chain of inheritance.'''
# Parent class
# class Vehicle:
#     def start(self):
#         print("Vehicle started")        
# # Intermediate class (inherits from Vehicle)
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
# # Child class (inherits from Car)
# class SportsCar(Car):
    
#     def turbo_boost(self):
#         print("Sports car is boosting with turbo")  
# obj = SportsCar()
# obj.start()
# obj.drive()
# obj.turbo_boost()
'''③ Hierarchical Inheritance 
    Multiple child classes inherit from a single parent class.'''
# Parent class
# class Shape:
#     def area(self):
#         print("Calculating area")
# # Child class 1 (inherits from Shape)
# class Circle(Shape):
#     def area(self):
#         print("Area of Circle")
# # Child class 2 (inherits from Shape)
# class Square(Shape):
#     def area(self):
#         print("Area of Square")
# obj1 = Circle()
# obj2 = Square()

# obj1.area()
# obj2.area()
'''④ Multiple Inheritance 
    A class inherits from more than one parent class.'''
# Parent class 1
# class grandfather:
#     def badepapa(self):
#         print("badepapa say mere bachcheeeeeee!!!!!!!!!!")
# # Parent class 2
# class perent:
#     def papa(self):
#         print("papa say mere bachcheeeeeee!!!!!!!!!!")
# # Child class (inherits from Flyer and Swimmer)
# class pota(grandfather, perent):
#     def quack(self):
#         print("ha papa and badepapa !!!!!!!!!!!!!!!!!!!")
        
# obj = pota()
# obj.badepapa()
# obj.papa()
# obj.quack()


'''HYBRID OR CROSS INHERITANCE
    A combination of two or more types of inheritance.'''
# Parent class
# class A:
#     def PAPA(self):
#         print("PAPA from class A")
# # Intermediate class (inherits from A)
# class B(A):
#     def BETA(self):
#         print("DADA from class B")
# # Child class (inherits from B)
# class C(B):
#     def BETA2(self):
#         print("DADA2 from class C")
# # CHILS CLASS B AND C IS INHERITED 
# class D(B, C):
#     def BACHA(self):
#         print("BACHA from class D")
# obj = D()
# obj.PAPA()



# class c0:
#     data=900
# class c1(c0):
#     data = 23
#     def m1(self):
#         print("i am m1")
# class c2:
#     data = 34
#     student = "nitin"
#     def m2(self):
#         print("i am m2")
#         super().m1()
# class c3(c2, c1):# ager me c1 ko pehle likhta hu to super class nhi chalega error hoga iss liye c2 ko pehle likha h
#     pass
# obj = c3()
# print(obj.data)  # it will print 23 due to method resolution order
# obj.m2()  # it will print "i am m2" and then "i am m1"


''' in the casse of constructor we cant use return function kyuki constructor kabhi bhi return hold nhi kerta h wo hamesha object return karta h ''' 
        





'''Polymorphism'''

''' in the case of ppython language we cant achive polymorphism directly but we can achive it by method overriding and method overloading  '''



''' Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). The most common use of polymorphism is through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass. This allows for dynamic method resolution at runtime, enabling flexibility and the ability to extend code without modifying existing functionality. Polymorphism enhances code readability and maintainability by allowing the same operation to behave differently based on the object it is acting upon. '''

''' its the ability of a function or method to operate in different ways based on the object it is acting upon '''

# class c1:
#     def m1(self,a):
#         print(a)
#     def m1(self,a,b):
#         print(a+b)
# obj = c1()
# obj.m1(10,20) # it will print 30

# class c1:
#     def m1(self,a,b=0,c=0):
#         if b == 0 and c == 0:
#             print(a)
#         elif c == 0:
#             print(a+b)
#         else:
#             print(a+b+c)
# obj = c1()
# obj.m1(10) # it will print 10
# obj.m1(10,20) # it will print 30
# obj.m1(10,20,30) # it will print 60


''' unpacking '''
# data = (10,20)
# for a,b in [data]:
#     print(a,b)


'''or  seccond solutionn for unpacking'''
# data=(10,20)
# n=""
# for i in data:
#     n+=str(i)+" "
# a,b = map(int,n.split())
# print(a,b) 
    


# class c1:
#     def m1(self,a):
#         print(a)
# class c2:
#     def m1(self,a,b):
#         print(a+b)
# def call(class_name,*args):
#     obj = class_name()
#     length = len(args)
#     if length == 1:
#         obj.m1(args[0])
#     elif length == 2:
#         obj.m1(args[0],args[1])
# call(c1,10) # it will print 10
# call(c2,10,20) # it will print 30
    
    
    
''' method overloading '''
# class c1:
#     def m1(self,a,b):
#         self.a=a
#         self.b=b
# obj1=c1(20,30)
# obj2=c1(50,60)
# print(obj1+obj2)# it will give error kyuki humne + operator ko overload nhi kiya h ab hum + operator ko overload kerenge taaki hum do object ko add ker sakein

''' but ham upper vali chijj logic se ker sakte h without operator overloading '''
# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self_o1,self_o2):
#         n1,n2=self_o1.a + self_o2.a, self_o1.b + self_o2.b
#         return f"added values are {n1} and {n2}"
#         # return n1+n2
# obj1=c1(20,30)
# obj2=c1(50,60)
# print(obj1 + obj2) # it will print added values are 70 and 90
''' y sirf jab 2 object honge tab chalega ham print(obj1+obj2+obj3) nhi ker sakte kyuki humne 2 object ke liye hi add method banaya h '''
# #  or directally call the method
# print(obj1.__add__(obj2,obj3         )) 
# """ ager hamare pass 2 object se jyada h to ham is tarah se ker sakte h"""
# print(obj1.__add__(obj2)) # it will print added values are 70 and 90

''' same for multification operator '''
# class c1:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __mul__(self_o1,self_o2):
#         n1,n2=self_o1.a * self_o2.a, self_o1.b * self_o2.b
#         return f"multified values are {n1} and {n2}"
#         # return n1*n2 # 180 as a result ayega yha kyuki humne dono object ke a and b ko multify kiya h
# obj1=c1(2,3)
# obj2=c1(5,6)
# print(obj1 * obj2) # it will print multified values are 10 and 18
# #  or directally call the method
# print(obj1.__mul__(obj2)) # it will print multified values are 10 and 18