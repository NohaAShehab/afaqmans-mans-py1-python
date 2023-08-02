

""" syntax error
    ===> parser ===part of interpreter --> detect error -->
    Must be fixed
"""


# """ logical error  ---> developer  """
#
# def sumnum(num1, num2):
#     res = num1 * num2  # debugging
#     print(res)
#
# """how unit test for code """
#
# # sumnum(2,2)  # 4
# # sumnum(10 , 4)

""" runtime error """
# print("----------------")
# print(name)  #NameError: name 'name' is not defined

""" runtime exception --> unexpected action caused the application to stop """

# num = int(input("-- please enter number ----"))
#
# print(num)   #ValueError: invalid literal for int() with base 10: '444ffff'
#

# print(4/0)  #ZeroDivisionError

""" 
    script ---> 
    try:
        lines of code 
    except:
        do this when problem 


"""
# print("---------- Hello world --------")
# try:
#     print(name)
# except:
#     print("--- problem happend ")
#
# print("-------- end of block --------------")

##################################################

# try:
#     # print(6/0)
#     # print(name)
#     num1= int(input("please enter num"))
#     num2= int(input("please enter num"))
#     res  = num1/num2
#
# except Exception as e :
#     print(f"--- problem happend {e} ")
#
# print("-------- end of block --------------")


#########################3

# try:
#     # print(6/0)
#     # print(name)
#     num1= int(input("please enter num"))
#     num2= int(input("please enter num"))
#     res  = num1/num2
#
# except ValueError as e :
#     print(f"--- problem happend {e} ")
#     print("------------- not  valid inputs so we will reset the values ")
#     num1 = 0
#     num2 = 0
#     res = 0
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 0
# print("-------- end of block --------------")
#
#
# print(res)


""" ---- else block ---> executed once ? ---> there is no problem """


# try:
#     # print(6/0)
#     # print(name)
#     num1= int(input("please enter num"))
#     num2= int(input("please enter num"))
#     res  = num1/num2
#
# except ValueError as e :
#     print(f"--- problem happend {e} ")
#     print("------------- not  valid inputs so we will reset the values ")
#     num1 = 0
#     num2 = 0
# except ZeroDivisionError as ze:
#     print(ze)
# else: # optional
#     print(f"---- {res}")
#


""" finally block -=--> this block executed always  """

# try:
#     # print(6/0)
#     # print(name)
#     num1 = int(input("please enter num"))
#     num2 = int(input("please enter num"))
#     res = num1 / num2
#
# except ValueError as e:
#     print(f"--- problem happend {e} ")
#     print("------------- not  valid inputs so we will reset the values ")
#     num1 = 0
#     num2 = 0
# except ZeroDivisionError as ze:
#     print(ze)
# else:  # optional
#     print(f"---- {res}")
# finally:
#     print("------- we reached the end ------------------------")
#
# print("------------------------------------------")



############################ float
#
# def askforfloat(message):
#     try:
#         num = float(input(message))
#     except:
#         # return  askforfloat(message)
#         return  False
#
#     else:
#         return  num
#     finally:
#         ### terminate process even if the function return before termination
#         print("------- operation finished")
#
#     print("#######################------- operation finished#########################")
#
#
# r= askforfloat("please enter raduis")
# print(r)

""" check float ---> string >"""


def askforfloat(message):
    num = input(message)
    ## float ---> zero or one dot , --> rest of the chars ---> digits
    newnum=list(num)
    no_of_dots = num.count(".")
    if no_of_dots in (0,1) and newnum[-1]!='.' :
        if '.' in newnum:
            newnum.remove('.')
        for item in newnum:
            if not item.isdigit():
                return False
        else:
            return float(num)
    return  False


res=askforfloat("please enter raduis ")
print(res)


