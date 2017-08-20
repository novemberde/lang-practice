try:
    # TODO: write code...
    print()
except Exception as e:
    print()
    # raise e
    
try:
    print()
except Exception as e:
    # raise e
    print()
else:
    # TODO: write code...
    print()

try:
    print()
except Exception as e:
    # raise e
    print()
else:
    print()
finally:
    print()


try:
    a = []
    print(a[3])
except Exception as e:
    print(e)    # list index out of range
else:
    print("This is printed if there's no exception")
finally:
    print("This is always printed")

try:
    f = open("Not exist file", "r")
except FileNotFoundError as e:
    pass
