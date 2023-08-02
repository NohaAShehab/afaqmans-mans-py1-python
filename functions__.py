"""

    special variable

    -->  refer to block of code --> execution when I call it.
"""

"""
    def funtioname(set of arguments):
        function body 
        return 
        return  value 
        
"""
"""you must define the function before calling it ."""
"""------------ function with known number arguments -------------------"""
""" ------------------------ function with mandatory arguments """
# """
#     sayhello()
#     def sayhello():
#         pass
# """
# def sayhello():
#     print("---- hello world ----")
#
#
# # to call the function
# sayhello()
#
# r= sayhello()
# print(r)
""" """

# def sayhello():
#     print("---- hello world ----")
#     return
#
#
# # to call the function
# sayhello()
# r= sayhello()
# print(r)

""" function ---> apply lines on specific data , customization function behaviour"""


def sayWelcome(username):
    print(f"welcome {username}")


# sayWelcome("Ahmed")
# sayWelcome()  #TypeError: sayWelcome() missing 1 required positional argument: 'username'
# sayWelcome("Ahmed", 'Ali', "test")  #TypeError: sayWelcome() takes 1 positional argument but 3 were given

""" function accept arguments and return with data """
# def sumnum(num1, num2):
#     res = num1+ num2
#     print(res)
#     return res
#
# total = sumnum(10,20)
# print(total)


# res = sumnum("10", "20")
# print(f"res= {res}")

# res = sumnum("10", 20)  # TypeError: can only concatenate str (not "int") to str
#
# print(f"res= {res}")

""" restrict type of the arguments """
# def sumnum(num1, num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     res = num1+ num2
#     print(res)
#     return res


# sumnum(10, "20")
#
# sumnum("ahmed", "ali")

# def sumnum(num1:int, num2:int):   # do things --> just way of documentation for code
#     res = num1+ num2
#     print(res)
#     return res
#
# myres = sumnum(10,20)
# myres = sumnum("ahmed","ali")
# myres = sumnum("20", 20)

""" validate datatypes of variable inside the function """

"""
    isinstance(variable, datatype) --> returns with True if variable matches the given datatype
"""


# print(isinstance('iti',str))
# print(isinstance("10", int))

# def sumnum(num1: int, num2: int):  # do things --> just way of documentation for code
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#         return res
#     print("---- not valid parameters")
#
#
# myres = sumnum(10, 20)
# myres = sumnum("ahmed", "ali")
# myres = sumnum("20", 20)

""" function with optional arguments  ---> default values ?  """

# def sumnum(num1=10, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1+ num2
#     print(res)
#     return res
#
# myres = sumnum(10,20)
#
# myres = sumnum(23)
#
# myres = sumnum()


# def sumnum(num1, num2=1010):
#     print(f"num1={num1}, num2={num2}")
#     res = num1+ num2
#     print(res)
#     return res
#
# myres = sumnum(10,20)
#
# myres = sumnum(23)
#
# myres = sumnum()


"""------- functions with variable number of arguments -----------"""
#
# print('Ahmed', "ali", "mohamed")
# print()
# print(3,45,5,44,555,5,5,5)


# def askforstudents(* students): # *---> *arges  }} * --> zero or more ((regex))
#     print(students)  # tuple
#
#
# askforstudents()
# askforstudents("Ahmed")
# askforstudents("Ahmed", "ali", "Mohamed")


#
# print("Ahmed", "Ali", "Mohamed", sep='__||__')
# print("hello", end=' ')
# print("world")
#
# """
# """


""" ----------> """


def introduceyourself(**info):  # function accept zero or more keyword argument
    print(info) # dictionary


introduceyourself(name='Noha', works_at='iti')
introduceyourself()
introduceyourself(fname='sara',lname='Nasef', city='Mansoura')






