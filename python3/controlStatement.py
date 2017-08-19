a = 1
if a:
    print("True")
else:
    print("False")
# True



if 0: print("True")
else: print("False")
    
if "":  print("True")
else:   print("False")
    
if []:  print("True")
else:   print("False")
    
if ():  print("True")
else:   print("False")
    
if {}:  print("True")
else:   print("False")
# False False False False False

# Operator
# >=, >, <, <=, ==, !=, in, not in

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter Number: """

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
    
#     # Escape from while
#     if number == 5: break
#     elif number == 6: continue

test_list = [1,2,3,4]

for i in test_list:
    print(i)
# 1 2 3 4

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# 3 7 11

for i in range(10):
    print(i)
# 0 ~ 9

for i in range(2, 4):
    print(i)
# 2 3


a = [1,2,3,4,5]
for i in range(len(a)):
    print(i)
# 0 1 2 3 4


print("Print one line to next print.", end=" ")
print("hi")
# Print one line to next print. hi


# List includ For
result = [x*y for x in range(1, 3)
                for y in range(4, 7)]
print(result)   # [4, 5, 6, 8, 10, 12]