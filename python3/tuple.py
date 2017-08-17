# list is using [], but tuple is using ()
# list can create, delete and modify values, but tuple cannot modify values that are already declared.

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1);
print(t2);
print(t3);
print(t4);
print(t5);
# ()
# (1,)
# (1, 2, 3)
# (1, 2, 3)
# ('a', 'b', ('ab', 'cd'))