from cmath import pi
from operator import index
from re import A, X
from typing import runtime_checkable


mystring1 = 'Hello'
# mystring1[0] = 'H'
# print(mystring1)

# print(len(mystring1))

# name = 'Parkson'
# print(name.upper())

# name = 'Parkson'
# name = name.upper()
# print(name)

# myname = 'Parkson Chen'
# print(list(myname))

# print('i have a dream {}'.format(1))
# print('{}, {}, {}, {}'.format(1, 'haha', '22', pi))
# print('{3}, {1}, {2}, {0}'.format(1, 'haha', '22', pi))

# myname = 'parkson'
# age = 40
# print(f'my name is {myname}, age is {age}')

# myname = 'parkson'
# myname = 'P' + myname[1:]
# print(myname)

# mylist = [1, 4, 9]
# mylist[0] = 8
# print(mylist)

# mylist = ['a', 'b', 'c', 'd']
# mylist.reverse()
# mylist = mylist[::-1]

# mylist = ['a', '2', 's', 'r']
# lost_element = mylist.pop()
# print(f'{mylist}, {lost_element}')

# a = 12
# b = a
# b = 15
# print(a)
# print(b)


# x = [1, 3, 5, 6, 7]
# y = x
# y[0] = 12
# print(x)
# print(y)

# x = [1, 3, 5, 6, 7]
# y = x.copy()
# y[0] = 12
# print(x)
# print(y)

# person = {'x': {'y' : [0, 1, 7]}}
# print(person['x']['y'][2])

# mytuple = 'parkson', 40, 'rich'
# print(mytuple)

# names, age, statement = mytuple
# print(names, age, statement)

# x = 5
# y = 20

# temp = x
# x = y
# y = temp

# print(x, y)
# print(x)
# print(y)

# x, y = y, x
# print(x, y)

# myString = "a, h , e , H"
# print(myString == myString.lower())

# if 2 or (10 / 0):
#     print('2是truthy value, 為true, 不受(10/0)這個無意義運算的影響')

# if (10 / 0) or 2:
#     print('10除以0沒意義, 壞掉')

# k  = True

# if k == True:
#     print('k is true')

# # 好一點的寫法
# if k:
#     print('k is true')

# if (5 > 3) and []:
#     print('不會執行')
# else:
#     print('empty list is falsy value')

# for variable in iterable object:
#     do something

# for i in 'hello world':
#     print(i)

# myList = [1, 3, 5, 7, 9]

# for i in myList:
#     if i > 5:
#         print(i)

# myList = [(3, 4), (5, 9), (10, 11)]
# for a, b in myList:
#     print(a + b)

# myDict = {"name":"Parkson", "age":40}
# for name, age in myDict.items():
#     print(f'name is {name}, age is {age}')

# counter = 0

# for i in '1234':
#     for j in 'abcd':
#         print(i, j)
#         counter += 1
# print(f'count total {counter}')

# for i in 'abcd':
#     pass
# print('haha')


# print('before for loops')

# for i in '12345':
#     for j in 'abcdefg':
#         if j == 'b':
#             break
#         print(i, j)
#     print(i, j)

# print('after for loop')

# for i in 'abcdef':
#     if i == 'c':
#         continue
#         print('nothing')
#     print(i)

# print(range(10))

# for i in range(5):
#     print(i)

# counter = 0
# for letter in 'how are you  today?':
#     if counter < 10:
#         print(letter)
#         counter += 1

# for item in enumerate('how are you today?'):
#     print(item)

# for counter, char in enumerate('how are you today?'):
#     if counter < 10:
#         print(char)

mylist1 = [1, 2]
mylist2 = ['a', 'b', 'c']
mylist3 = ['A', 'B', 'C', 'D']

for i in zip(mylist1, mylist2, mylist3):
    print(i)