from cmath import pi
from operator import index
from re import A, X


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

person = {'x': {'y' : [0, 1, 7]}}
print(person['x']['y'][2])