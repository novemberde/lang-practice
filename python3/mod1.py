def sum(a,b):
    return a+b

class Math:
    PI = 3.141592
    
    def solv(self, r):
        return self.PI * (r**2)  # ** is square
    

# this is executed when imported
# print(sum(1,2))

if __name__ == "__main__":
    print(sum(1,2))
    