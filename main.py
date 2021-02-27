# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Tuple can be of different data types


'''
Creating a Tuple
'''

# tuple = ()
# tuple = ('cat', [4,3,2,1], (1,2,3))
# tuple = 4321, 1234
# tuple = 'hello',
# tuple = ('hello',)
# print(tuple)


'''
Access Tuple Elements
'''

tuple = (1234, 4321, 'hello')
# print(tuple[0])
# print(tuple[-2])


'''
Slicing Tuples in Python
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')

# print(fruits[:1])
# print(fruits[2:5])
# print(fruits[:-2])
# print(fruits[:2])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])


'''
Changing a Tuple
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')
# fruits[0] = 'pear'
# Tuple cannot be changed. Totally Immutable.

'''
Deleting a Tuple
'''

# fruits = ('orange', 'apple', 'pear', 'grapes', 'banana')

# del fruits[0]
# print(fruits)
# Item within tuple cannot be deleted or altered.

# del fruits
# print(fruits)
# Name of Tuple can be deleted as a whole but not individual contents of tuple.

'''
Tuple Methods
'''

# print(dir(list))
# print(dir(tuple))

# fruits = ('orange', 'orange', 'apple', 'pear', 'grapes', 'banana')

# print(fruits.count('orange'))
# print(fruits.index('apple'))