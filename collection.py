# list
# list=['farooq','zaheer','khan']
# for x in list:
#     print(x)

#tuple
# tuple = ("apples", "banana", "cherry")
# tuple[1] = "blackcurrant"
# # The values will remain the same:
# print(tuple)


#set
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

#Dictionaries

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

#named tuple
# from collections import namedtuple
# a=namedtuple('courses','name,tech,time')
# s=a('data science','python','12:00')
# print(s)

# deque
# from collections import deque
# a=['1','2','3','4','5']
# a1=deque(a)
# a1.append('6')
# print(a1)
# a1.appendleft('0')
# print(a1)

#Chainmap
# from collections import ChainMap
# FullName = {1:'Farooq',2:'Zaheer'}
# age = {3:'22'}
# full_info=ChainMap(FullName,age)
# print(full_info)

#counter

# from collections import Counter
# a=[1,1,1,1,2,2,2,2,3,3,3,4,4]
# c=Counter(a)
# print(c) 

#OrderedDict
# from collections import OrderedDict
# od=OrderedDict()
# od[1]='a'
# od[2]='b'
# od[3]='c'
# od[4]='d'
# print(od)
