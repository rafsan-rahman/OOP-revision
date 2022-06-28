from abc import ABC

class abstract(ABC):
    def sum(self,a,b):
        pass
    def mul(self,a,b):
        pass

class calc1(abstract):
    def __init__(self):
        print("initializing from calc1")
    
    def sum(self,a,b):
        return a+b

class calc2(calc1):
    def __init__(self):
        print("initializing from calc2")
        super().__init__()
    def mul(self,a,b):
        return a*b
    
if __name__ == "__main__":

    obj = calc2()
    print(obj.mul(2,3))
    print(obj.sum(5,4))
        
    
