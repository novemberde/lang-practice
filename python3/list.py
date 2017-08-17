odd = [1,3,5,7,9]

print(odd[0]) # 1
print(odd[-1])# 9

a = [1,2,3, ["a", "b", "c"]]

print(a[3][0])# a
print(a[-1][0])# a


print(a[0:2]) # [1, 2]
print("12345"[0:2]) # 12

print(a[:3])  # [1,2,3]
print("12345"[:2]) # 12

print(a[3:])  # [['a', 'b', 'c']]
print("12345"[2:]) # 345

print([1,2,3] + [4,5,6]) # [1, 2, 3, 4, 5, 6]
print([1,2,3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(str(1) + "hi") # 1hi # Attention! cannot concat int and string. should convert an integer to string.

b = [1,2,3]
b[1] = 3
print(b)  # [1, 3, 3]

b = [1, 2, 3]
b[1: 2] = [5, 5]
print(b)  # [1, 5, 5, 3]

c = [1,2,3,4,5]
c[1:3] = []
print(c) # [1, 4, 5]

d = [1, 2, 3, 4, 5]
del d[1]
print(d)  # [1, 3, 4, 5] # "del" can be used for all kind of situation to delete object in python

e = [1, 2]
e.append(3)
print(e)  # [1 ,2 ,3]

f = [5,3,2,4,1]
f.sort()
print(f)  # [1, 2, 3, 4, 5]
f.reverse()
print(f)  # [5, 4, 3, 2, 1]
print(f.index(3)) # 2

g = [1, 2]
g.insert(1, 6)
print(g)  # [1, 6, 2]

h = [1, 2, 3, 1, 2, 3]
h.remove(2)
print(h)  # [1, 3, 1, 2, 3] # remove first 2

k = [1, 2, 3]
print(k.pop())  # 3
print(k)  # [1, 2]

k = [1, 2, 3]
print(k.pop(1))  # 2
print(k)  # [1, 3]

l = [1, 2, 3, 1, 1]
print(l.count(1)) # 3

m = [1, 2]
m.extend([3, 4, 5])  # this is same as using "+"
print(m)  # [1, 2, 3, 4, 5]
