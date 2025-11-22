# data = {'a': 1, 'b': 2, 'c': 3}
# new={('a',10,30),('b',20,50),('c',30,60)}
# for k , i,c in new:
#     print(k,i,c)


# data = {'a':68,'b':3993}
# data.setdefault('xyz',90)
# print(data)


# data.update({'a':100})
# # print(data)

'''
DICTIONARY COMPPRATION
'''
# keys = {"a","b","c","a"}
# # values = {11,223,44}
# # data={k:v for k in keys for v in values}
# # print(data) # output will be wrong because it will take all values for each key

# # generate value auto
# data1={k:ord(k) for k in keys}
# print(data1)


# data={(chr(x-1),chr(x),x):x for x in range(65,71)}
# print(data)

 
'methods of dict'
# data = {'a':32,'b':44}
# print(data.fromkeys('a',99))
# print(data)


# data = {'a':32,'b':44}
# print(data.fromkeys('a'))
# print(data)

# data = {'a':32,'b':44}
# print(data.fromkeys(('a','b'),(2,3)))
# print(data)

# data = {'a':32,'b':44}
# print(data.fromkeys(('a','b'),(2,3)))
# print(data)

# data = {'a':32,'b':44}
# print(data.items())

# data = {'a':32,'b':44}
# new = dict([('a',21),('b',33)])
# print(new)

'zip function'
'respective index ke sath combine ho jayega'
keys = ['nitin','age']
values = [3,19]
print(list(zip(keys,values)))
print(dict(zip(keys,values)))
print(set(zip(keys,values)))


# new = [('a',33),('b',44),('c',55)]

# for i in new:
#     print(i[0])
    

# new = [('a',33),('b',44),('c',55)]
# for i,j in new:
#     print(i,"---->",j)
    
    
# new = [('a',33),('b',44),('c',55)]
# for i,j in new:
#     print(i,"---->",j)


# data = {'a':234,'b':35,'c':43}
# # for i,j in data.items():
# #     print(i,"------",j)
# # data.update({'a': 33})
# # print(data)

# print(data.update({'name':'nitin'}))
# print(data)


# data = {chr(x):y for x in range(65,69) for y in range(1,4)}
# print(data)


# data = {chr(k):k for k in range(65,70) }
# print(data)

# keys = ['a','b','c','d']
# values = [10,20,30,40,50]
# data = {keys[k]:values[v] for k in range(len(keys)) for v in range(len(values)) if k==v}
# or 
# data = {keys[i]:values[i] for i in range(len(keys)) }
# print(data)


