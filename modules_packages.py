

""" any .py file --> python module ---> you can import it in another module ? """

# def askforInt(message):
#     while True:
#         num =  input(message)
#         if num.isdigit():
#             return  int(num)
#
#         print("---- please enter valid number-------")

""" import the function askforInt from iti_helper ? """
#
# import iti_helper # import all module content here
# def calculator():
#     num1 = iti_helper.askforInt('please enter num1: ')
#     num2 = iti_helper.askforInt("please enter num2: ")
#     res =num1  + num2
#     print(res)
#
#
# calculator()
#
#
# ""
# iti_helper.sayhello()

""" import part of the module"""


# from iti_helper import  sayhello
#
# sayhello()


""" alias the imports """

# import  iti_helper as myhelper
# myhelper.sayhello()


# from iti_helper import  sayhello as hello
# hello()


"""import module from package """
# import  summertraining.iti
#
# summertraining.iti.saywelcom()
#
# import  summertraining.iti as myiti
#
# myiti.saywelcom()


"""import part of the module from package """

# from summertraining.iti import saywelcom
# saywelcom()
#


""" ---- package with __init__ file """

# import  st  # content in the __init__ will be called
#
# st.saybye()

# import  st.validatemodule
# st.validatemodule.validatenum(10)

# from st.validatemodule import  validatenum
# validatenum(100)



from st import  validatenum
print(validatenum(200))