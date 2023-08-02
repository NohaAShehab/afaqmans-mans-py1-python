
""" lexical scoping
    identify where the variable can be accessed and modified
"""
""" any variable defined in the python module 
---> has scope --> global scope  ---> can be accessed anywhere in the script 
    modify --> read  
    
    what we will happen we need to access it from inside the function 
    read value from inside the function ----> ok 
"""
# course = 'python' # variable --> has scope global scope ?
# print(course)
# course="Introduction to python"
#
#
# def printCourse():
#     print(f"--- from inside the function course ={course}")
#
# printCourse()

"""-------------------------- local scope -----------------"""
# course = 'python'
# def modifycourse():
#     """ when you define variable inside a function
#         this variable --> has scope --> local scope
#         --> the variable exists only during the duration of function work
#     """
#     course = 'Django'  # local scope ---> can be accessed only inside the function
#     print(course)
# modifycourse()
# print(f"course = {course}")
#
""" modify global variable from inside the function """
# course = 'python'
# def modifycourse():
#     global course
#     course = 'Django'  # local scope ---> can be accessed only inside the function
#     print(course)
# modifycourse()
# print(f"course = {course}")

""" ------------------------ function inside a function ---------------- """

# def myfunction():
#     name = "Ahmed"  # local variable for myfunction
#     def printname():
#         print(f"from inside the function : {name}")
#
#     printname()
#
# myfunction()


# def myfunction():
#     name = "Ahmed"  # local variable for myfunction
#     def modifyname():
#         name= input("please enter name : ")  # create new local variable for the function
#         # modify name
#         print(f"new name = {name}")
#
#     modifyname()
#     print(name)
#
# myfunction()

"""=============================="""

def myfunction():
    name = "Ahmed"  # local variable for myfunction
    def modifyname():
        nonlocal name  # please use the local variable of the parent function
        name= input("please enter name : ")
        # modify name
        print(f"new name = {name}")

    modifyname()
    print(name)

myfunction()
