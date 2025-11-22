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
enter the no: 7
0 
1 1 
2 2 2 
3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 5 
6 6 6 6 6 6 6 

"""
# n = int(input("enter the no: "))
# for i in range(n):
#     for j in range(i+1):
#         print(i,end=" ")
#     print()
        

# n = int(input("enter the no: "))
# for i in range(n):
#     for j in range(n):
#         print(i,end=" ")
#         i+1
#     print()
    
'''
1
1 0 
1 0 1
1 0 1 0
1 0 1 0 1
'''

# n=int(input("enter the no : "))
# a=0
# b=1
# for i in range(n):
#     for j in range(i+1):
#         if  j!=0 and j%2!=0 :
#          print(a,end = " ")
#         else:
#           print(b,end = " ")
#     print()

# # or

# n=int(input("enter the no : "))
# a=0
# b=1
# for i in range(n):
#     for j in range(i+1):
#         if  i==0 and i+j != 0 :
#          print(b,end = " ")
#         else:
#           print(a,end = " ")
#     print()
    
    
'''
enter the no : 5
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1


'''    
# n=int(input("enter the no : "))
# for i in range(n):
#     for j in range(i+1):
#         if  i == 0 or i == j or i%2==0 and j<1  or i + j == n-1  or i == n-1 and  j%2==0    :
#          print("1",end = " ")
#         else:
#           print("0",end = " ")
#     print()

'''

    * 
   * *
  * * *
 * * * *
'''

# n=5

# for i in range(n):
    
#    print((" "*(n-i))+("* "*i))





#  for pascal equestion 
# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     val = 1
#     for j in range(i + 1):
#         print(val, end="   ")
#         val = val * (i - j)//(j-1)
#     print()


'''
        1   
      1   1   
    1   2   1   
  1   3   3   1   
1   4   6   4   1  

'''


# n = 5
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     val = 1
#     for j in range(i + 1):
#         print(val, end="   ")
#         val = val * (i - j) // (j + 1)
#     print()


'''
1 
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
'''
# n=int(input("enter a no."))
# for i in range(n):
#     for j in range(i+1):
#       print(i+1,end=" ")
#     print()

'''
    *       *     
  *   *   *   *   
*       *       *

'''
# n=9
# for i in range(n//3):
#     for j in range(n):
#         if i+j==n//4 or j-i==n//4 or i+j == n-n//3 or j-i==n-n//3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        
        
        
# data = [
#   [1,2,3,4,5],
#   [10,9,8,7,6],
#   [11,12,13,14,15],
#   [20,19,18,17,16],
#   [21,22,23,24,25]
  
# ]

# #  or 
# output = []
# n = int(input("enter the no :"))
# for i in range(n):
#   l=[]
#   for j in range(n):
#     l.append(int(input()))
#   output.append(l)
    
# print(output)


# outpute = []
# itr = len(data)
# for i in range(itr):
#     if i % 2 == 0:
#         for j in range(len(data[i])):
#             outpute.append(data[i][j])
#     else:
#         for j in range(len(data[i])-1, -1, -1):  
#             outpute.append(data[i][j])

# print(outpute)

# outpute = []
# itr = len(data)
# for i in range(0,itr,2):
#     for j in range(0,len(data[i])):
#         outpute.append(data[i][j])
    
#     if i < itr - 1:
#         for k in range(0,len(data[i])):
#             outpute.append(data[i+1][len(data[i])-k-1])
            
#     else : 
#          continue
# print(outpute)
    

# arr = [2, 7, 11, 15]
# l = []
# for i in range(len(arr)):
#   for j in range(i + 1, len(arr)): 
#     if arr[i] + arr[j] == 9:
#       l.append((i, j))  
# print(l)



# data = [
#   [1,2,3,4,5],
#   [6,7,8,9,10],
#   [11,12,13,14,15],
#   [16,17,18,19,20],
#   [21,22,23,24,25],
# ]


# outpute = []
# itr = len(data)
# for i in range(len(data)):
#   if i<1:
#      for j in range(0,itr):
#        outpute.append(data[i][j])
#   elif i>0 and j == itr -1:
#      for j in range(0,itr):
#        outpute.append(data[i][j])
    
# print(outpute)

# row = len(data)
# col=len(data[0])
# layers=(min(row,col)+1)//2

# for i in range(layers):
#   top,bottem=i+1,row-i-1,
#   left,right=i,col-i
#   for i in range(left,right):
#     print(data[left][i],end=" ")#good
#   for i in range(top,bottem+1):
#     print(data[i][right-1],end=" ")
#   for i in range(right-2,left-1 ,-1):
#     print(data[right-1][i],end=" ")# good
#   for i in range(bottem-1,top-1,-1):
#     print(data[i][top-1],end=' ')

# training code

# # ............SPIRAL METRIX.............

# data=[ [1,2,3,4,5],
#       [6,7,8,9,10],
#       [11,12,13,14,15],
#       [16,17,18,19,20],
#       [21,22,23,24,25] ] 

# # Calculate no row and col.....

# rows=len(data)
# col=(len(data[0]))

# layers=(min(rows,col)+1)//2
# for i in range(layers):
    
#     # Calculate Top ,Bottom, Left,Right
#     top,bottom=i+1,rows-i-1
#     left,right=i,col-i


#     # left to right:------
#     for i in range(left,right):
#         print(data[left][i],end=' ')

#     # top to bottom:-------
#     for i in range(top,bottom+1):
#       print(data[i][right-1],end=' ')


#     # right to left:------
#     for i in range(right-2,left-1,-1):
#        print(data[right-1][i],end=' ') 

#   #  bottom to top:-------
#     for i in range(bottom-1,top-1,-1):
#        print(data[i][left],end=' ')

# data=121
# new=0
# while data>0:
#   last = data%10
#   new=new*10+last
#   data//=10
# print(new)


# def reverse_string(s):
#     print(s[::-1])
# reverse_string("ineuron")

# data = "ineuron"
# # data.split()
# # print(data[::-1])
# # or 
# print(data[::-1])          

# a="c++"
# print(a[:1:1]+"p"+a[2:])


# data="hello world"
# # print(data[6:len(data)]+" "+data[:5])
# # or by loop  
# n=" "
# for i in data.split():
#   n=i+" "+n
# print(n)

# data=["abc","def","ghi"]
# output=[]
# l=data[::-1]
# for i in l:
  
#   output.append(i[::-1])
# print(output)
# for i in range(len(data)-1,-1,-1):
#   output.append(data[i][::-1])
# print(output)

# data=[1,2,3]
# l=[[]]
# for i in range(len(data)):
#   l.append([data[i]])
#   for j in range(i+1,len(data)):
#    l.append( [data[i]]+[data[j]])
  
# print(l)
  
  
  
# n = 5

# for i in range(n):          # rows 0 → 4
#     for j in range(n):      # cols 0 → 4
#         if j == n - 1 - i:  # diagonal condition
#             print("*", end="")
#         else:
#             print(" ", end="") 
#     print()
