
from iti_helper import  askforInt
def divnums():
    num1 = askforInt("please enter num1 : ")
    num2 = askforInt("please enter num2 : ")
    if num2==0:
        raise ZeroDivisionError("cannot divide by zero ---")
    print(f"num1={num1},num2={num2}")
    res = num1/num2
    return  res


print(divnums())