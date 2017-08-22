a = "python-ppp"

print(a.find('y'))  # 1
print(a.count('p')) # 4
print(a.index("p")) # 0
print(a.find("p"))  # 0 this is different from 'index'. because index occur error if certain texts are not exist. but find not occur error
print(a.join("111"))# 1python-ppp1python-ppp1
print(a.upper())    # PYTHON-PPP
print("HI".lower()) # hi
print(" hi ".lstrip()) # "hi "
print(" hi ".rstrip()) # " hi"
print(" hi ".strip()) # "hi"
print("Life is so cool".replace("so", "really"))  # Life is really cool
print("Life is so cool".split(" ")) # ['Life', 'is', 'so', 'cool']


# Advanced string format
print("hello {0}".format("world"))  # hello world  # it is possible to put an integer or any.
print("{0}, {1}, {2}".format(1,2,3))# 1, 2, 3
print("{0}, {2}".format(1,2,3))# 1, 3
print("{a}, {b}".format(a=1, c=2, b=3)) # 1, 3
print("{0:<10}".format("hi")) # "hi        "  # align left
print("{0:>10}".format("hi")) # "        hi"  # align right
print("{0:^10}".format("hi")) # "    hi    "  # align center
print("{0:=^10}".format("hi")) # "====hi===="  # fill blanks
print("{0:0.4f}".format(3.12341234)) # 3.1234
print("{0:10.4f}".format(3.12341234)) # "    3.1234"
print("{{ and }}".format()) # { and }
