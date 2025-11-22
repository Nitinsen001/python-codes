# n = int(input("enter the no: "))
# for i in range(n):
#     for j in range(n):
#         if i ==j or j == 0 or i == n-1 or j== 4 or i +  j == n-1 or i == 0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n = 5
# for i in range(n):
#     for  j in range(n):
#         if i == 0 or  (j == 0 and i<n-1) or j + i == n-1 or i-j == 3-n//2 or j - i == 3-n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
enter the no: 5
* * * * * 
*       *
  *   *
*       *
* * * * *

'''
# n = int(input("enter the no: "))
# for  i in range(n):
#     for j in range(n):
#         if i == 0  or i == n-1 or (i - j == n%2 and i <n-2) or (i+j == n//2+1 and j < 2)  or (i+j == n and j > 2) or (i+j == n+2 and i>2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")  
            
#     print()



"""
enter a no : 5
  * * *   
*       *
* * * * *
*       *
*       *
"""

# n=int(input("enter a no : "))
# for i in range(n):
#   for j in  range(n):
#     if j==0 and i>0  or i==0 and j>0 and j<n-1 or j==n-1 and i>0 or i==n//2 and j>0 and j<n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


'''

* * * *     
*       *   
*         *
*       *
* * * *
*       *
*         *
*       *
* * * *

'''

# h = int(input("enter the no: "))
# b = h//2+2
# for i in range(h+1):
#     for j in range(b):
#         if j== 0 or  i == 0 and j<=b//2 or j-i==b//2 or i == h//2 and j < b//2+1 or i+j == b+1 and j>b//2 or i == h and j <= b//2 or i-j == h-b-1 and j >b//2 or i == h-1 and j == h//2 :
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
    
'''
enter the no: 6
  * * *     
*
*
*
*
  * * *  

'''
    
# n = int(input("enter the no: "))
# for i in range(n):
#     for j in range(n):
#         if (j == 0 and i > 0 and i<n-1) or( j > 0 and j< n-2 and i == 0) or (i == n-1 and j > 0 and j < n-2) :
#             print("*",end=" ")  
#         else:
#             print(" ",end=" ")
#     print()


'''

* * * *
*       *
*       *
*       *
*       *
*       *
* * * *


'''

# n = int(input("enter a no:"))

# for i in range(n):
#   for j in range(n):
#     if j==0 or i == 0 and j < n//2 or j == n//2 and i>0 and i<n-1 or i==n-1 and j < n//2 :
#       print("*",end=" ")
#     else:
#       print(" ",end=' ')
#   print()

'''
* * * * * 
*
*
* * * * * 
*
*
* * * * * 

'''
# n = int(input("enter a no:"))

# for i in range(n):
#   for j in range(n):
#     if j == 0 or i == 0 and j <= n//2+1 or i==n//2 and j <= n//2+1 or i==n-1 and j <= n//2+1 :      print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

'''

* * * * * 
*
*
* * * * * 
*
*
* 


'''
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 or i == 0 and j <= n//2+1 or i==n//2 and j <= n//2+1 :      print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

'''
  * * * *
*         *
*         *
*
*       * * *
*       *   *
  * * *     *


'''
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if  j == 0 and i>0 and i<n-1 or i==0 and j>0 and j<=n//2+1 or j==n-2 and i>0 and i<n//2 or i == n//2+1 and j>n//2 or i==n-1 and j>0 and j<=n//2  or i == n-2 and j>n//2 and j<n-2 or j == n-1 and i>n//2+1 :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""

*       *
*       *
*       *
* * * * *
*       *
*       *
*       *

"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 or j==n//2+1 or i==n//2 and j<n//2+1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
* * * * *
    *
    *
    *
* * * * *
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if i == 0 or i == n-1 or j ==n//2:
#       print("*",end=" " )
#     else:
#       print(" ",end=" ")
#   print()


"""
* * * * * * * * * 
        *
        *
        *
        *
*       *
*       *
*       *
  * * *
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if i == 0 or j == n//2 and i<n-1 or j==0 and i>=n//2+1 and i<n-1 or i == n-1 and j > 0 and j <n//2 :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
*       *
*     *
*   *
* *
*   *
*     *
*       *


"""

# n = int(input("enter a no:"))

# for i in range(n):
#   for j in range(n):
#     if j == 0 or i+j==n//2+1 or i - j == n//2-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
*
*
*
*
*
*
* * * * *
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 or i==n-1 and j<n-2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

""" 
*         *     
* *     * *
*  *   *  *
*    *    *
*         *
*         *
*         *

"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j==0 or j == n-1 or i==j and i<=n//2 or j==n-i-1 and i<n//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
"""
enter a no:7
*           * 
* *         * 
*   *       * 
*     *     * 
*       *   * 
*         * * 
*           * 
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j==0 or j == n-1 or i==j:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


"""
enter a no:7
  * * *       
*       *
*       *
*       *
*       *
*       *
  * * *
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 and i>0 and i<n-1 or i==0 and j>0 and j<=n//2 or j==n//2+1 and i > 0 and i<n-1 or i==n-1 and j>0 and j < n//2+1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


"""
* * *
*     *
*     *
* * *
*
*
*
"""
# n = int(input("enter a no:"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 or i==0 and j<n//2 or j==n//2 and i>0 and i<n//2 or i ==n//2 and j<n//2 :
#       print("*",end=" ")
#     else:
#       print(" ",end=" " )
#   print()

"""
  * * *       
*       *
*       *
*       *
* *     *
*   *   *
  * * * 
        *    
"""


"""
enter a no :7
  * * *       
*       *
* *     *
*   *   *
*     * *
*       *
  * * *   *

"""
# n = int(input("enter a no :"))
# for i in range(n):
#   for j in range(n):
#     if j == 0 and i>0 and i <n-1 or i == 0 and j>0 and j<=n//2 or j==n//2+1 and i>0 and i<n-1 or i-j+1==n//2-1 or i == n-1 and j>0 and j<=n//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
enter a no :7
* * * *       
*       *
*       *
* * * *
* *
*   *
*     *
"""
# n=int(input("enter a no :"))
# for i in range(n):
#   for j in range(n):
#     if j==0 or i == 0 and j<=n//2 or i==n//2 and j<=n//2 or j == n//2+1 and i>0 and i<n//2 or i-j==n//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
  * * *
*
*
  * *
      *
      *
* * *
"""
# n= int(input("enter a no : "))
# for i in range(n):
#   for j in range(n):
#     if i ==0 and j>0 and j <=n//2 or j==0 and i>0 and i<n//2 or i ==n//2 and j>0 and j<n//2 or j==n//2 and i>n//2 and i<n-1 or i==n-1 and j<n//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
* * * * *
    *
    *
    *
    *

"""
# n = int(input("enter a noo:"))
# for i in range(n):
#   for j in range(n):
#     if i==0 or j==n//2:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
enter the no :7
*         *   
*         *
*         *
*         *
*         *
*         *
  * * * *

"""
# n = int(input("enter the no :"))
# for i in range(n):
#   for j in range(n):
#     if j==0 and i<n-1 or j==n//2+2 and i<n-1 or i == n-1 and j>0 and j<=n//2+1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *

# """
# n = int(input("enter the no :"))
# for i in range(n):
#   for j in range(n):
#     if i==j or i==n-j:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
  
""""""  
  
  
  
  
"""
enter the no :7
*           * 
  *       *
    *   *
      *
    *   *
  *       *
*           *

"""  

# n = int(input("enter the no :"))
# for i in range(n):
#   for j in range(n):
#     if i==j or j==n-i-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


'''
*       *
*       *
*   *   *
* *   * *
*       *

'''
# n = int(input("enter the no :"))
# for i in range(n):
#   for j in range(n):
#     if j==0 or i==n-j-1 and i>=n//2 or i==j and i>=n//2 or j==n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

"""
enter a no : 7
*           * 
  *       *
    *   *
      *
      *
      *
      *

"""
# n=int(input("enter a no : "))
# for i in range(n):
#   for j in range(n):
#     if i==j and i<=n//2 or j==n//2 and i>n//2 or i+j==n-1 and i < n//2  :
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


"""
* * * * * *
        *
      *
    *
  *
* * * * * *

"""

# n = int(input("enter the no : "))
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1 or j==n-i-1 and i>0 and i<n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()



'''

* * * * * * * * * *
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
* * * * * * * * * *

'''
# for i in range(11):
#    for j in range(11):
#      if i==j or i == 0 or j==0 or i == 10 or j==10 or :
#        print("*",end=" ")
#      else:
#        print(" ",end=" ")
#    print()

# nums=[9,1,4,7,3,-1,0,5,8,-1,6]
    
# output = []
# if len(nums)==0:
#     print(0)
# n = min(nums)
# output.append(n)
# for i in output:
#   for j in nums:
# e    if i+1 == j:
#       if j not in output:
#         output.append(j)
# print(len(output))


nums=[3,2,2,3]
outpute=[]

n = int(input("enter a no: "))
for i in range(len(nums)-1):
  if n == nums[i]:
    del nums[i]
print(nums)
  
        