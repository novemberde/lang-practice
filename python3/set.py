# It does not allow duplicate value.
# Unordered


s1 = set([1,2,3])
print(s1)   # {1, 2, 3}

s2 = set("hellllllo")
print(s2)   # {'h', 'e', 'l', 'o'}
print(list(s1)) # [1, 2, 3]
print(tuple(s1))# (1, 2, 3)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)              # {4, 5, 6}
print(s1.intersection(s2))  # {4, 5, 6}
print(s1 | s2)              # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))         # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 - s2)              # {1, 2, 3}
print(s1.difference(s2))    # {1, 2, 3}

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)                   # {1, 2, 3, 4, 5, 6}
s1.remove(2)
print(s1)                   # {1, 3, 4, 5, 6}