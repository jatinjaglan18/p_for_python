#OOPS
class Person:
    var = 2     #class Variable
    def __init__(self,name, age):       #Constructor
        self.name = name
        self.age = age

    def fn(self):                        #Instance Method
        return self.name, self.age
    
    @classmethod
    def v(cls,s):
        return s.split()

    @staticmethod
    def a(val):
        print('Hello ' + val)

p1 = Person('Jatin', 20)
print(p1.__dict__)
