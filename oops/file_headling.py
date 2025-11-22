'''
file headling
* read mode - "r" - default mode , file pointer is at the beginning of the file , if file is not present it will give error
* write mode - "w" - file pointer is at the beginning of the file , if file is not present it will create a new file
* append mode - "a" - file pointer is at the end of the file , if file is not present it will create a new file
* read and write mode - "r+" - file pointer is at the beginning of the file , if file is not present it will give error
* write and read mode - "w+" - file pointer is at the beginning of the file , if file is not present it will create a new file
* append and read mode - "a+" - file pointer is at the end of the file , if file is not present it will create a new file
* binary mode - "b" - it is used to read and write binary files like images , videos , etc.
'''
# # opening a file in write mode
# f = open("sample.txt", "w")
# # writing data to the file
# f.write("Hello, this is a sample file.\n")
# f.write("This file is created using Python.\n")
# # closing the file
# f.close()
# # opening the file in read mode
# f = open("sample.txt", "r")

''' use with statement to open a file'''
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
# # # reading data from the file
# # data = f.read()
# # print(data)


# '''use write mode to write data to the file'''
# ''' if the file are not present it will create a new file'''
# with open("sample.txt", "w") as f:
#     f.write("This is a new line added to the file.\n")
#     f.write("Writing data to the file using write mode.\n")
# # # opening the file in read mode to verify the data
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)


# ''' use append mode to append data to the file'''
# with open("sample.txt", "a") as f:
#     f.write("This line is appended to the file.\n")
#     f.write("Appending data to the file using append mode.\n")
# # # opening the file in read mode to verify the data
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# ''' use xclusive creation mode to create a new file'''

# with open("newfile.txt", "x") as f:
#     f.write("This file is created using exclusive creation mode.\n")
#     f.write("If the file already exists, it will give an error.\n")
# # # opening the file in read mode to verify the data
# with open("newfile.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# ''' use of seek() method
# it is used to change the file pointer position'''
# with open("sample.txt", "r") as f:
#     print("Current file pointer position:", f.tell())# here  tell() method is used to get the current file pointer position
#     data = f.read(20)# reading first 20 characters from the file
#     print("Data read:", data)# printing the data read from the file
#     print("File pointer position after reading 20 characters:", f.tell())# printing the file pointer position after reading 20 characters
#     f.seek(0)  # moving the file pointer to the beginning
#     print("File pointer position after seek(0):", f.tell())# printing the file pointer position after seek(0)
#     data = f.read()# reading the entire file again
#     print("Data read after seek:", data)# printing the data read from the file after seek
    
    
# ''' use of readline() method'''
# with open("sample.txt", "r") as f:
#     line1 = f.readline()# reading first line from the file
#     print("First line:", line1)# printing the first line
#     line2 = f.readline()# reading second line from the file
#     print("Second line:", line2)# printing the second line
    
# ''' use of readlines() method'''
# with open("sample.txt", "r") as f:
#     lines = f.readlines()# reading all lines from the file
#     print("All lines:", lines)# printing all lines as a list
#     for line in lines:
#         print("Line:", line.strip())# printing each line after stripping the newline character
        
        
''' writelines() method'''
# with open("sample.txt", "a") as f:
#     lines_to_add = ["This is the first line to add.\n", "This is the second line to add.\n"]
#     f.writelines(lines_to_add)# writing multiple lines to the file
# # # opening the file in read mode to verify the data
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)

''' writable() method
# it is used to check whether the file is opened in writable mode or not'''
# with open("sample.txt", "a") as f:
#     print("Is the file writable?", f.writable())# it will return True as the file is opened in append mode
# with open("sample.txt", "r") as f:
#     print("Is the file writable?", f.writable())# it will return False as the file is opened in read mode
    
    
''' use a+ mode to read and append data to the file'''
# with open("sample.txt", "a+") as f:
#     f.write("hyy my name is nitin.\n")
#     f.write("y line bhi append ker rha hu.\n")
#     f.seek(0)
#     data = f.read()
#     # print(data)
#     f.close()
#     print(data)

''' if i want to delete this file use the os module'''
# import os
# os.remove("sample.txt")# it will delete the file named sample.txt

''' now read data in row wise'''
# with open("newfile.txt", "a+") as f:
#     f.write("adding new line at the start of the file.\n")
#     f.write("adding new line at the start of the file2.\n")
#     f.write("adding new line at the start of the file3.\n")
#     f.seek(0)
#     data = f.readlines()
#     for row in data:
#         print(row)


''' now csv files'''
import csv
data = [["Name", "Age", "City"],
        ["Nitin", 19, "khargone"],
        ["chinu", 20, "maheshwar"],   
        ["jatin", 18, "satwada"]]
# writing to csv file
with open("sample.csv", "w") as f:
    writer = csv.writer(f)# creating a csv writer object
    writer.writerows(data)# writing multiple rows to the csv file
# reading from csv file
with open("sample.csv", "r") as f:
    reader = csv.reader(f)# creating a csv reader object
    for row in reader:
        print(row) 


''' __name__ and __main__ '''
data = "my name is nitin"

if __name__ == "__main__": # this block will only execute if this file is run directly
    print(data)