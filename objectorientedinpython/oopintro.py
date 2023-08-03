
# emp1= {
#     "id":1,
#     "name":'Ahmed',
#     "salary":1000
# }
#
# emp2= {
#     "empid":2,
#     "name":'Ali',
#     "salary":1000
# }
# name='ahmed'
# name.split()
""" create your own datatype --> id , name, salary ===> class """
""" datatypes  ---> classes """


"1- to define class "
# class Employee:
#     pass
#
#
# emp = Employee()  # take new object from the class
# print(emp)
#
# """ loosely dynamically typed lang.
# you can assign properties and values to the objects in the runtume"""
#
# emp.name='ahmed'
# emp.salary = 33333
#
# emp2 = Employee() # create empty object
# emp2.fname='Ali'
# emp2.net_sal=4455


"""customize object creation ? """
""" object ---> data, can functionality"""
# class Employee:
#     "to customize object creation "
#     def __init__(self):  # self refers to object address in the memory
#         print(f"---this function will be called while creating the object\n {self}")
#         self.name ='ahmed'
#         self.email = 'ahmed@gmail.com'
#
#
# emp = Employee()  # take new object from the class
# print(emp)
# emp2= Employee()
# print(emp2)
# emp2.name = 'Ali'





# class Employee:
#     "to customize object creation "
#     def __init__(self, name, email):  # self refers to object address in the memory
#         self.name =name
#         self.email = email
#
#
#
#
# emp = Employee("ahmed", 'ali')  # take new object from the class
# print(emp)
# emp2= Employee("Mohamed", "test")
# print(emp2.name)
# emp2.name = 'Ali'
# emp2.salary = 10000




"""
    object from class hold data and functionlity 
"""

#
# class Employee:
#     "to customize object creation "
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         # # instance variables ? --> its value depends on the caller instance
#         self.name =name
#         self.email = email
#         self.salary=salary
#
#     # instance method ? ===> its behaviour depends on the caller instance
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self.email}, {message}")
#
#
#
#
# emp = Employee("ahmed", 'ali')  # take new object from the class
# print(emp)
# emp.printEmpData('this confirmation that the data is correct')
# emp2= Employee("Mohamed", "test")
# print(emp2.name)
# emp2.name = 'Ali'
# emp2.salary = 10000
# emp2.printEmpData("----")

""" -------------------------------------------------------"""

#
# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#     ### this the class variable
#     ## can be accessed via class itself
#
#     # shared property between all instnace
#     "to customize object creation "
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         # # instance variables ? --> its value depends on the caller instance
#         self.name =name
#         self.email = email
#         self.salary=salary
#         # Employee.count +=1
#         self.__class__.count +=1
#         self.id= self.__class__.count
#
#     # instance method ? ===> its behaviour depends on the caller instance
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self.email}, {message}")
#
#
#
#
# emp = Employee("ahmed", 'ali')  # take new object from the class
# emp2= Employee("Mohamed", "test")
# print(Employee.count)
# print(emp2.__class__.count)
# Employee.nationality = 'Egyptian'


"""class method  --> object factory """



# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     # shared property between all instnace
#     "to customize object creation "
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         # # instance variables ? --> its value depends on the caller instance
#         self.name =name
#         self.email = email
#         self.salary=salary
#         # Employee.count +=1
#         self.__class__.count +=1
#         self.id= self.__class__.count
#
#     # instance method ? ===> its behaviour depends on the caller instance
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self.email}, {message}")
#
#
#     """ class method represent behaviour related to the class"""
#
#     @classmethod
#     def get_no_of_employees(cls): #
#         print(cls)  # cls ---> represent the class itself
#         return cls.count
#
#     @classmethod # object factory
#     def create_default_object(cls):
#         return cls('default', 'default',1000)
#
#
#
#
# emp = Employee("ahmed", 'ali')  # take new object from the class
# emp2= Employee("Mohamed", "test")
# print(Employee.count)
# print(emp2.__class__.count)
# Employee.nationality = 'Egyptian'
#
# print(Employee.get_no_of_employees())
# emp3 = Employee.create_default_object()
#


""" static methods """
class Employee:
    "define property related to the class "
    count = 0  ## property related to the class not the object

    def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
        # # instance variables ? --> its value depends on the caller instance
        self.name =name
        self.email = email
        self.salary=salary
        # Employee.count +=1
        self.__class__.count +=1
        self.id= self.__class__.count


    def printEmpData(self, message=''):
        print(f"name={self.name}, email={self.email}, {message}")



    @classmethod
    def get_no_of_employees(cls): #
        print(cls)  # cls ---> represent the class itself
        return cls.count

    @classmethod # object factory
    def create_default_object(cls):
        return cls('default', 'default',1000)

    # def cal_net_salary(salary):  # any regular method in the class ,
    #     # first argument represent object address , even if you didn't mention it.
    #     print(salary)
    #     return salary * .8

    @staticmethod  # this helper function not related to object or the class
    def cal_net_salary(salary):
        print(salary)
        return salary * .8

emp = Employee("ahmed", 'ali')  # take new object from the class

def cal_net_salary(salary):
    return salary*.8

# print(cal_net_salary(emp.salary))

print(Employee.cal_net_salary(emp.salary))
print(emp.cal_net_salary(emp.salary))




""" OOP principles ? 



    -> inheritance
    -> polymorphism
    -> encapsulation
    -> abstraction 



"""
