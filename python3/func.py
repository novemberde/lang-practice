# * make tuple in this case
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_many(1,2,3,4,5))  # 15


def sum_mul(type, *args):
    
    if type == "sum":
        result = 0
        
        for i in args:
            result += i
    elif type == "mul":
        result = 1
        
        for i in args:
            result *= i
            
    return result
    
    
print(sum_mul("sum",1,2,3,4,5))  # 15
print(sum_mul("mul",1,2,3,4,5))  # 120

def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(1, 2))    # (3, 2)

def init_value_func(a=10):
    return a
    
print(init_value_func(4))   # 4
print(init_value_func())    # 10

# def init_value_attention(a, b=10, c):   # this occur error. default argument must be located on last.
#     return a + b
print("abc" "def" "g")      # abcdefg
print("abc"+"def"+"g")      # abcdefg
print("abc","def","g")      # abc def g

# input()   # enable to get value immediately

# write file
f = open("test.txt", "w")
f.write("Je m'appelle kh.")
f.close()

# read file
f = open("test.txt", "r")
fileString = f.read()
print(fileString)   # Je m'appelle kh.
f.close()

f = open("test.txt", "r")
line = f.readline()
print(line)         # Je m'appelle kh.
f.close()

f = open("test.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)     # Je m'appelle kh.
f.close()

# Don't need to close 
with open("test.txt", "r") as f:
    print(f.read()) # Je m'appelle kh.