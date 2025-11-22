
# data=[1,2,3,4,5]
# l=[]
# for i in data:
#     print(i**2)
#     if i % 2==0:
#         l.append(i)
# print("even no is : ",l)

# data = "wellcome to JIT"
# for i in data:
#     if i == ' ':
#         print()
#     else:
#         print(i,end=" ")
        

# data=(1,2,3,4,5)
# for i in data:
#     print(i**2)

# data={2,2,3,4,5}
# for i in   data:
#     print(i**2)

# data={"name":"babubhai","age":24}
# for i in data:
    
#     print(i,data[i])

# n = int(input("Enter the number : "))
# for i in range(1,11):
#     print(i*n)

# size = int(input    ("Enter the size of list : ")  )
# for i in range(1,size+1):
#     if i%2 == 0:
#         print(i)
        
# for n in range(1, 11):
#     if n > 1:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 break
#         else:
#             print(n)

""" 
*
* *
* * *
* * * *
"""
# for i in range(4):
#     for j in  range(i+1):
#         print("*",end=" ")
#     print()
    
    
"""   
* * * * 
* * * 
* *
*"""
# for i in range(4):
#      for j in range(4-i):
#          print("*",end=" ")
#      print()

"""
   @
  @ @
 @ @ @
@ @ @ @ 

"""
# for  i in range(4):
#     for j in range(i+1):
#         print(" "+"@",end=" ")
#     print()


"""
*
* *
*   *
* * * *

"""
# for i in range(4):
#     for j in range(i+1):
#         if j==0 or j==i or i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    

"""
* * * * 
*     * 
*     *
* * * *
"""

# # dynamic
# row = int(input("Enter the number of rows: "))
# colom = int(input("Enter the number of columns: "))
# for i in range(row):
#     for j in range(colom):
#         if i == 0 or i == row - 1 or j == 0 or j == colom - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# dynamic

# row = int(int(input("Enter the row : ")))        
# colom = int(int(input("Enter the row : ")))        
# for i in range(row):
#     for j in range(colom):
#         if i == row or i == row-1 or j == colom or j == colom-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        
    
    
"""
*
* *
*   *
* * * *

    #   dynamic
"""
# row = int(input("Enter the number of rows: "))
# for i in range(row):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == row - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

"""
* * * * *
* *   * *
*   *   *
* *   * *
* * * * *
"""

# row = int(input("Enter the number of rows: "))
# colom = int(input("Enter the number of columns: "))
# for i in range(row):
#     for j in range(colom):
#         if i == 0 or i == row - 1 or j == 0 or j == colom - 1 or i == j or j == colom - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
 
 
 
# # dynamic
# row = int(input("Enter the number of rows: "))
# colom = int(input("Enter the number of columns: "))
# for i in range(row):
#     for j in range(colom):
#         if i == 0 or i == row - 1 or j == 0 or j == colom - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
 
 
"""
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
""" 

# n=int(input ("Enter the number : "))
# if n%2==0:
#     n=n+1
# for i in range(n):
#     for j in  range(n):
#         if i+j == n//2 or j-i == n//2 or i-j == n//2 or i+j == (n-1)+(n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

"""
          * 
        * * * 
      * * * * *
    * * * * * * *
  * * * * * * * * *

# """
# n = int(input("enter the no."))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in  range(i+1):
#         print("*",end=" ")
#     for m in  range(i):
#         print("*",end=" ")
#     print()
# n = int(input("enter the no."))
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in  range(i+1):
#         print("*",end=" ")
#     for m in  range(i):
#         print("*",end=" ")
#     print()



# n = int(input("enter the no."))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in  range(n-i):
#         print("*",end=" ")
#     for m in  range(n-i-1):
#         print("*",end=" ")
#     print()

# n = int(input("enter a no."))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(0,n+1):
#     print("*",end=" ")
# print()
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()


# n = int(input("enter the no."))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in  range(i+1):
#         print("*",end=" ")                                                                             
#     for m in  range(i):
#         print("*",end=" ")
#     print()



'''
* 
* * 
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

# for i in range(4):
#     for j in  range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(5):
#   print("*",end = " ")
# print()
# for i in range(4):
#      for j in range(4-i):
#          print("*",end=" ")
#      print()


