a = [1,2,3,4]
while a:
    print(a.pop())
    
#   4   3   2   1


if []:
    print("True")
else:
    print("False")
# False


if [1,2]:
    print("True")
else:
    print("False")
# True

# all type of value for example integer, it is also object.
print(type(3))  # <class 'int'>

a = 3
b = 3
print(a is b)   # True. Compare referenced address
print(a == b)   # True. Compare Value


import sys

print(sys.getrefcount(3))   # 57
print(sys.getrefcount(a))   # 57
c = 3
print(sys.getrefcount(3))   # 58
# 3 object is referenced if it is declared.


# a lot of technique to declare variables
a,b = ('python', 'life')
print(a, b) # python life
(a, b) = 'python', 'life'
print(a, b) # python life

[a, b] = ['python', 'life']
print(a, b) # python life

a = b = 'python'
print(a, b) # python python

a = 3
b = 5
a,b = b,a
print(a, b) # 5, 3

del(a)
del(b)

print(sys.getrefcount(3))   # 56

a = [1, 2, 3]
b = a
del a[0]
print(b)    # [2, 3]    # call by reference

a = [1, 2, 3]
b = a[:]
del a[0]
print(b)    # [1, 2, 3]
print(b is a)   # False

from copy import copy

a = [1, 2, 3]
b = copy(a)
del a[0]
print(b)    # [1, 2, 3]
print(b is a)   # False