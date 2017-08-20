print(abs(-3))  # 3

print(all([1,2,3])) # True
print(all([1,0,3])) # False

print(any([1,2,3])) # True
print(any([1,0,0])) # True
print(any([0,0,0])) # False

print(chr(97))  # a

# show all function or variables on [1,2]
print(dir([1,2]))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
# 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(divmod(7,3))  # 2, 1

# enumerate
for i, name in enumerate(["a", "b"]):   # return with index
    print(i, name)
    # 0 a
    # 1 b

# eval(expression as string)
print(eval("1 + 2 + 3"))    # 6
print(eval("divmod(7,3)"))  # 2, 1

def positive(num):
    return num>0

print(list(filter(positive, [-1,0,1,2,3]))) # [1, 2, 3]

print(list(filter(lambda x: x>0, [-1,0,1,2,3]))) # [1, 2, 3]



print(hex(234)) # 0xea


# get Reference address
a=12312
print(id(12312))    # 139928124207024
print(id(a))        # 139928124207024

print(int("123"))   # 123
# pinrt(int("hihi"))    # raise exception


class Person: pass
class Me(Person): pass

print(isinstance(Person(), Me)) # False
print(isinstance(Me(), Person)) # True

