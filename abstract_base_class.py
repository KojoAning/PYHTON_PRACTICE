# if you want to mendatorly define some methods in a class that inherites from some other class we can just do this

from abc import ABC,abstractmethod
class Shape(ABC): # THIS STEP IS CRUTIAL [ class _name_(ABC):]
    @abstractmethod # we can't make objects from abstract class .
    def printarea(self):
        return 0




class Rectangle(Shape):
        type ="rectangle"
        sides = 4
        def __init__(self):
            self.lenght = 6
            self.breath = 7
        def printarea(self): # if we don't define it it's gonna give error
            return self.lenght*self.breath


rect = Rectangle()
print(rect.printarea())