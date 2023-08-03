"""

    inheritance

    base class  architure --> can be used to create new class
    inheritance --> is-a relationship
"""

# class Person:
#     pass
#
# class Employee(Person):
#     pass
#
#
# emp = Employee()
# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))

""" properties"""







# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
# class Employee(Person):
#     pass
#
#
# emp = Employee("Ahmed")
# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))
# emp.speak()


""" """

# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def speak(self):
#         print(f"My name is {self.name}")

# class Employee(Person):
#     def __init__(self,name ,email):
#         # you can call parent constructor
#         super().__init__(name)
#         self.email = email
#
#     ## override ?
#     def speak(self):
#         super().speak()
#         print(f"My email is {self.email}")
# emp = Employee("Ahmed", 'name@gmail.com')
# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))
# emp.speak()


""" python support multiple inheritance """


class A:
    pass

class B:
    pass

class Myclass (A, B):
    pass

obj = Myclass()
print(isinstance(obj,B))
print(isinstance(obj,A))



"""

class Test:

    def abc(num1:int):
        pass
        
    def abc(num1:str):
        pass 

"""


class Test:

    def abc(self, num1: int):
        print(num1+10)

    def abc(self,num1: str):
        print(num1+'iti')

t = Test()
t.abc(10)
t.abc('test')




