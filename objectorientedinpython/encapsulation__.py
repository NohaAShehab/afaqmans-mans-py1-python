# """limit data accessability
# """
# # class Employee:
# #     "define property related to the class "
# #     count = 0  ## property related to the class not the object
# #
# #     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
# #         # # instance variables ? --> its value depends on the caller instance
# #         self.name =name
# #         self.email = email
# #         self.salary=salary
# #         # Employee.count +=1
# #         self.__class__.count +=1
# #         self.id= self.__class__.count
# #
# #
# #     def printEmpData(self, message=''):
# #         print(f"name={self.name}, email={self.email}, {message}")
# #
# #
# # emp = Employee('ahmed','ahmed@gmail',333)
# # print(emp.email)
# # emp.email = 'updated'
#
# """
#     access modifiers
#     public  ---> can access it using the object anywhere
#     protected ---> can access it in the class or any derived class
#     private  ---> can access it only in the class
#
#
#     ### No access modifier --->
#
#     any variable  [a-z]* ---> public
#     any variable  _* ---> protected
#     any variable  __ ---> private
#
#
# """
#
# # class Employee:
# #     "define property related to the class "
# #     count = 0  ## property related to the class not the object
# #
# #     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
# #         self.name =name
# #         self._email = email
# #         self.__salary=salary
# #         self.id= self.__class__.count
# #
# #
# #     def printEmpData(self, message=''):
# #         print(f"name={self.name}, email={self._email}, {message}")
# #
# #
# # emp = Employee('ahmed','ahmed@gmail',333)
# # print(emp.name)
# # print(emp._email) # can be accessed
# # emp._email = "updated"
# # # print(emp.__salary)  #'Employee' object has no attribute '__salary'
# # print(emp._Employee__salary)
# #
# # print(emp.__dict__)
# # # {'name': 'ahmed', '_email': 'updated', '_Employee__salary': 333, 'id': 0}
#
# """ setter and getter """
#
# # class Employee:
# #     "define property related to the class "
# #     count = 0  ## property related to the class not the object
# #
# #     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
# #         self.name =name
# #         self._email = email
# #         self.__salary=salary
# #         self.id= self.__class__.count
# #
# #     def setsalary(self, salary):
# #         ##setter ==> validate inputs
# #         if isinstance(salary, int )or isinstance(salary, float):
# #             self.__salary = salary
# #         else:
# #             raise TypeError("Salary should be int or float")
# #     def getSalary(self):
# #         return self.__salary *.8
# #
# #     def printEmpData(self, message=''):
# #         print(f"name={self.name}, email={self._email}, {message}")
# #
# #
# # emp = Employee('ahmed','ahmed@gmail',"333")
# # print(emp.getSalary())
# #
# # # emp.setsalary("100000")
# # # print(emp.getSalary())
# #
# #
#
#
#
#
#
# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         self.name =name
#         self._email = email
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#         self.id= self.__class__.count
#
#     def setsalary(self, salary):
#         ##setter ==> validate inputs
#         if isinstance(salary, int )or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#     def getSalary(self):
#         return self.__salary *.8
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self._email}, {message}")
#
#
# emp = Employee('ahmed','ahmed@gmail',"333")
# print(emp.getSalary())
#
# # emp.setsalary("100000")
# # print(emp.getSalary())


###
"""limit data accessability
"""
# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         # # instance variables ? --> its value depends on the caller instance
#         self.name =name
#         self.email = email
#         self.salary=salary
#         # Employee.count +=1
#         self.__class__.count +=1
#         self.id= self.__class__.count
#
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self.email}, {message}")
#
#
# emp = Employee('ahmed','ahmed@gmail',333)
# print(emp.email)
# emp.email = 'updated'

"""
    access modifiers 
    public  ---> can access it using the object anywhere 
    protected ---> can access it in the class or any derived class 
    private  ---> can access it only in the class 


    ### No access modifier ---> 

    any variable  [a-z]* ---> public 
    any variable  _* ---> protected
    any variable  __ ---> private  


"""

# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         self.name =name
#         self._email = email
#         self.__salary=salary
#         self.id= self.__class__.count
#
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self._email}, {message}")
#
#
# emp = Employee('ahmed','ahmed@gmail',333)
# print(emp.name)
# print(emp._email) # can be accessed
# emp._email = "updated"
# # print(emp.__salary)  #'Employee' object has no attribute '__salary'
# print(emp._Employee__salary)
#
# print(emp.__dict__)
# # {'name': 'ahmed', '_email': 'updated', '_Employee__salary': 333, 'id': 0}

""" setter and getter """


# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         self.name =name
#         self._email = email
#         self.__salary=salary
#         self.id= self.__class__.count
#
#     def setsalary(self, salary):
#         ##setter ==> validate inputs
#         if isinstance(salary, int )or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#     def getSalary(self):
#         return self.__salary *.8
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self._email}, {message}")
#
#
# emp = Employee('ahmed','ahmed@gmail',"333")
# print(emp.getSalary())
#
# # emp.setsalary("100000")
# # print(emp.getSalary())
#
#
""""""
#
# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         self.name = name
#         self._email = email
#         self.setsalary(salary)
#         self.id = self.__class__.count
#
#     def setsalary(self, salary):
#         ##setter ==> validate inputs
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#
#     def getSalary(self):
#         return self.__salary * .8
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self._email}, {message}")


# emp = Employee('ahmed', 'ahmed@gmail', "333")
# print(emp.getSalary())

# emp.setsalary("100000")
# print(emp.getSalary())


""" property decorator """



# class Employee:
#     "define property related to the class "
#     count = 0  ## property related to the class not the object
#
#     def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
#         self.name = name
#         self._email = email
#         self.setsalary(salary)
#         self.id = self.__class__.count
#
#
#     def setsalary(self, salary):
#         ##setter ==> validate inputs
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#
#     @property
#     def salary(self):
#         return self.__salary * .8
#
#     @salary.setter
#     def salary(self, salary):
#         ##setter ==> validate inputs
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise TypeError("Salary should be int or float")
#
#     def printEmpData(self, message=''):
#         print(f"name={self.name}, email={self._email}, {message}")
#
#
#
# emp = Employee("Ahmed", "eee", 1000000)



class Employee:
    "define property related to the class "
    count = 0  ## property related to the class not the object

    def __init__(self, name, email, salary=1000):  # self refers to object address in the memory
        self.name = name
        self._email = email
        self.salary = salary  # call property setter
        self.id = self.__class__.count


    @property
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, salary):
        ##setter ==> validate inputs
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise TypeError("Salary should be int or float")

    def printEmpData(self, message=''):
        print(f"name={self.name}, email={self._email}, {message}")



emp = Employee("Ahmed", "eee", 1000000)
print("------------------")