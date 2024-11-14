class MyNumber:
    def _iter_ (self):
        self.x = 1
        return self
    
    def _next_(self):
        a = self.x
        self.x += 1
        return a
    
myclass = MyNumber()
myiter = iter(myclass) 

print(next(myiter))
print(next(myiter))
print(next(myiter))
