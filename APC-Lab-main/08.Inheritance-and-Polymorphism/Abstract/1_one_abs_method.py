from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        length = 10
        breadth = 5
        print("Area of rectangle =", length * breadth)


obj = Rectangle()
obj.area()