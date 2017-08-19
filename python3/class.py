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