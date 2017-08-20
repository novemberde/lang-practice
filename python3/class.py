class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))    # 3
print(cal1.adder(5))    # 8
print(cal2.adder(3))    # 3
print(cal2.adder(7))    # 10


# Empty Class
class Simple:
    pass


# Variable
class Service:
    text = "Hello world"

service = Service()
print(service.text) # Hello world

class Service2:
    def __init__(self, name):
        self.name = name

service2=Service2("hi")
print(service2.name)    # hi


############ 
# inherit
class Car:
    def __init__(self, sun_roof):
        self.sun_roof = sun_roof
    def drive(self):
        print("Drive")
        
class Sonata(Car):
    name = "sonata"

sonata=Sonata("Sun roof")

sonata.drive()
print(sonata.name, sonata.sun_roof)
# Drive
# sonata Sun roof
############


#############
# Overriding
class Genesis(Car):
    def drive(self):
        print("Genesis Drive")
genesis=Genesis("SunRoof")
genesis.drive() # Genesis Drive
#############

#############
# Operator overloading
class Pride(Car):
    def __add__(self, other):
        self.drive()
        other.drive()
    def __sub__(self, other):
        return
    def __mul__(self, other):
        return
    def __truediv__(self, other):
        return

pride = Pride("SunRoof")
pride + genesis
# Drive
# Genesis Drive
#############
