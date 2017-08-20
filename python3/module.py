import mod1

print(mod1.sum(1,2))    # 3


# from [MODULE_NAME] import [MODULE_FUNCTION]
from mod1 import sum
print(sum(3,4)) # 7

# if __name__ == "__main__"
# please check last line of mod1.py 


from mod1 import Math
print(Math().solv(2))   # 12.566368


# sys module
import sys
print(sys.path) # ['/home/ubuntu/workspace/python3', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']


