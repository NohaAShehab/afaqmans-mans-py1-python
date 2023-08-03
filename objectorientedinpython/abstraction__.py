
from abc import ABC, abstractmethod

""" to create abstract class 
    ABC ---> Abstract base class 
"""

class Shape(ABC):
    """ each abstract class must contains at least one abstract method """
    @abstractmethod
    def cal_area(self):
        pass


# s = Shape() #TypeError: Can't instantiate abstract class Shape with abstract method cal_area


class Rectangle(Shape):
    def __init__(self, width= 10, height =10):
        self.width =width
        self.height = height
    def cal_area(self):
        print(f"--- area = {self.width * self.height}")

e= Rectangle()
e.cal_area()

""" 
     all classes in python ---> implicitly inherits from basic class
     object 

"""

name ='test'
print(name.isspace())