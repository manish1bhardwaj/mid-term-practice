#buit in for classes
class task:
    def __init__(self,val):
        self.val = val
    def get(self):
        return self.val
    def set(self,v):
        self.val = v

obj1 = task(20)
obj2 = task(30)
obj1.val = 100
print(obj1.get())


# -------------------------------------------------------------------------------------------------------------------------

#syntax 
class Parent:
    pass
    