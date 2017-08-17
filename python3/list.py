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