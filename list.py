# count the 1 and 5 in the list
# l = [1,5,3,5,7,1,1]
# count5=0
# count1=0
# for i in l:
#     if i==1 :
#         count1+=1
#     if i==5 :
#         count5+=1
# print(count1)
# print(count5)


# l1=[1,2,5,7,8,9,10,11]
# l2=[]

# for i in range(len(l1)-1):
#     if l1[i+1]==l1[i]+1:
#        l2.append([l1[i], l1[i+1]])
#     elif l1[i+1]!=l1[i]+1 and l1[i+2]!=l1[i+1]+1:
#         l2.append([l1[i+1]])   
# print(l2)




# l1=[7,3,4,9,2]      
# # buble sorted
# for i in range(len(l1)-1):
#     for j in range(len(l1)-1-i):
#         if l1[j]>l1[j+1]:
#             l1[j],l1[j+1]=l1[j+1],l1[j] 
# print(l1)


# l9=[17,70,50]
# for i in range(len(l9)-1):
#     for j in range(len(l9)-1-i):
        
#        if l9[j]>l9[j+1]:
#            l9[j],l9[j+1]=l9[j+1],l9[j]
# slargest=l9[-2]
    
# print(slargest)



# l9=[1,2,3,4,7,5,9,7,44,6,7,8,]
# new=[]
# result=[]

# for i in range(len(l9)):
#     if l9[i-1]+1==l9[i]:
#         new.append(l9[i])
#     else:
#         result.append(new)
#         new=[l9[i]]
# result.append(new)
# result.pop(0)
# print(result)




# data1='abcdihefgo'
# l9=[]
# for i in data1:
#     l9.append(ord(i))
# new=[]
# result=[]

# for i in range(len(l9)):
#     if l9[i-1]+1==l9[i]:
#         new.append(chr(l9[i]))
#     else:
#         result.append(new)
#         new=[chr(l9[i])]
# result.append(new)
# result.pop(0)
# print(result)

# a=[]

# for i in result:
    
#     b=''
#     for j in i:
#         b+=j
#     a.append(b)
# print(a)
    
    
# l = [1,1,1,13,3,3,2,5,5,5]
# n=[]

# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count==1:
#         n.append(i)
# print(n)
# print(sum(n))




# import time
# start_time = time.time()
# l = [5,0,7,0,3,0,0,8]

# for i in l:

#     if i==0:
#         l.append(i)
#         l.pop(l.index(i))
# print(l)

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")


# l1=[2,0,4,0,3,0,]
# l2=[]
# l3=[]

# for i in l1:
#     if i !=0:
#         l2.append(i)
#     if i == 0:
#         l3.append(i)
# print(l2+l3)



# l4=[2,4,3,6,5]
# l5=[4,7,9,5,2]
# l6=[]
# for i in l4:
#     count=0
#     for j in l5:
        
#         if i == j:
#             count+=1
#     if count==1:
#         l6.append(i)
# print(l6)

# l7=[[3,4,6],[5,7,8],[9,0,1]]
# l8=[]
# for i in l7:
#     for j in i:
#         l8.append(j)
# print(l8)

# l9 = [1,2,3,3,4]
 
# for i in range(len(l9)):
#     for j in range(len(l9)-i):
        
#        if l9[j]>l9[j+1]:
#            l9[j],l9[j+1]=l9[j+1],l9[j]
# print(l9)


data = [(x*y) for x in range(1,11) for y in range(1,3) if x % 2 == 0]
print(data)

