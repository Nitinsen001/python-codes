''' math modules '''
# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(16))
# # it conver value into form of nearest upper value
# print(math.ceil(3.4))# 4
# #  floor are convert nearest value into lower value
# print(math.floor(3.4))# 3
# # find factorial
# print(math.factorial(5))
# # find power
# print(math.pow(2,3))
# # log base 10
# print(math.log(100,10))
# # log base e
# print(math.log(math.e))
# print(math.sin(90))

# print(math.cos(0))
# print(math.tan(45))
# print(math.radians(90))
# print(math.degrees(1.57))
# # it is use to find lcm
# print(math.lcm(12,15))
# # it is use to find gcd(greatest common divisor)
# print(math.gcd(12,15))# 3 jo dono ko devide ker dega

''' random modules '''
# import random
# print(random.random()) # 0.0 to 1.0
# print(random.randint(1,100)) # 1 to 100
# print(random.randrange(1,100,5)) # 1 to 100 with step
# l = ['nitin','rahul','sonu','monu']
# print(random.choice(l))
# random.shuffle(l) # it is use to shuffle the list, shuffle means random arrange
# print(l)
# print(random.sample(range(1,100),5)) # it is use to print 5 random number from 1 to 100

'''how random is work'''
# a='hello'
# # print(id(a))

# a='hello'
# def random(n):
#     r = str(id(a))
    
#     return r[::-1][:n]
#     # return r[:n]
    
# print(random(5))


''' system models'''
import sys
# print(sys.version)  # check version of python
# print(sys.path)     # check path of python
# sys.stdout.writelines("hello") # it is use to print the output
# print(sys.maxsize)  # it is use to check the max size of integer
# print(sys.platform) # it is use to check the platform of python
# print(sys.getsizeof(5)) # it is use to check the size of integer
# print(sys.getsizeof("hello")) # it is use to check the size of string
# print(sys.getsizeof([1,2,3,4,5])) # it is use to check the size of list
# data = sys.stdin.readline()
# sys.stdout.writelines(data)
# sys.stdout.writelines("------->"+data)

''' os module'''
import os
# print(os.name) # it is use to check the name of os
# print(os.getcwd()) # it is use to check the current working directory 
# os.mkdir('nitin') # it is use to create a directory
# os.makedirs('nitin/rahul/sonu') # it is use to create a directory with sub directory
# os.chdir('C:\\Users\\Nitin\\Desktop\\training 5th sem\\nitin') # it is use to change the current working directory
# print(os.getcwd())
# os.rmdir('nitin') # it is use to remove a directory   
# os.removedirs('nitin/rahul/sonu') # it is use to remove a directory with sub directory
# os.rename('test.txt','nitin.txt') # it is use to rename a file
# print(os.listdir()) # it is use to list all files and directories in the current working directory
# print(os.listdir('C:\\Users\\Nitin\\Desktop\\training 5th sem')) # it is use to list all files and directories in the specified directory
# print(os.stat('nitin.txt')) # it is use to check the status of a
# print(os.path.join('C:\\Users\\Nitin\\Desktop\\training 5th sem','nitin.txt')) # it is use to join two paths
# print(os.path.exists('C:\\Users\\Nitin\\Desktop\\training 5th sem\\nitin.txt')) # it is use to check whether the path exists or not
# print(os.path.isfile('C:\\Users\\Nitin\\Desktop\\training 5th sem\\nitin.txt')) # it is use to check whether the path is a file or not
# print(os.path.isdir('C:\\Users\\Nitin\\Desktop\\training 5th
# sem\\nitin.txt')) # it is use to check whether the path is a directory or not
# print(os.path.split('C:\\Users\\Nitin\\Desktop\\training 5th sem\\nitin.txt')) # it is use to split the path into directory and file
# print(os.path.splitext('C:\\Users\\Nitin\\Desktop\\training 5th sem\\nitin.txt')) # it is use to split the path into file name and extension

# print("my current directory id :" + os.getcwd()) # get current working directory

''' datetime module'''
import datetime
# print(datetime.datetime.now()) # it is use to check the current date and time
# print(datetime.datetime.now().year) # it is use to check the current year
# print(datetime.datetime.now().month) # it is use to check the current month
# print(datetime.datetime.now().day) # it is use to check the current day
# print(datetime.datetime.now().hour) # it is use to check the current hour
# print(datetime.datetime.now().minute) # it is use to check the current minute 
# print(datetime.datetime.now().second) # it is use to check the current second
# print(datetime.datetime.now().microsecond) # it is use to check the current microsecond
# print(datetime.datetime.now().date()) # it is use to check the current date
# print(datetime.datetime.now().time()) # it is use to check the current time
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # it is use to format the date and time

''' keyword module'''
import keyword
# print(keyword.kwlist) # it is use to check the list of keywords in python
# print(len(keyword.kwlist)) # it is use to check the number of keywords in python

'''qrcode module'''
import qrcode

qrcode.make('www.linkedin.com/in/nitin-sen-972a7130a').save('nitin.png')
# img = qrcode.make('https://www.youtube.com/@NitinTechy')
# img.save('nitin.png')
# img.show()

''' pillow module'''    
from PIL import Image
# img = Image.open('nitin.png')
# img.show()
# print(img.size) # it is use to check the size of image
# print(img.format) # it is use to check the format of image
# print(img.mode) # it is use to check the mode of image
# img = img.resize((300,300)) # it is use to resize the image
# img.show()
# img = img.rotate(90) # it is use to rotate the image
# img.show()

''' pyinstaller module'''
# isko install karne ke liye command prompt me jana hai or fir likhna hai pip install pyinstaller
# iska use kerke ham apne python file ko exe file me convert kar sakte hai
