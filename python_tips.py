
# # list comprehension ?

""" generate list numbers from 1 to 10"""

# myl = []
# for i in range(1,11):
#     myl.append(i)

# myl = list(range(1, 11))
# print(myl)

""" list comprehesion """
#
# myl = [num for num in range(1,11)]
# print(myl)


# myl = [num for num in range(1,11) if num%2!=0]
# print(myl)

"""swap  ? """

# num1 = 10
# num2 = "iti"
# print(num1, num2)
# num1,num2 = num2, num1
# print(num1, num2)


""" lambda expression ---> anonymous functions"""


# def sumnum(num1, num2):
#     return  num1+num2
#
# res = lambda num1, num2: num1+num2
# print(res(3,4))



grades = [10 , 21 ,33 ,55 ,90, 23, 100]


## map ? divide all the elements of list

# new_grades = map(lambda x:x/2, grades)
# print(new_grades) # map object
# print(list(new_grades))

## filer odd grades
new_grades = filter(lambda x:x%2!=0, grades)
print(new_grades) # filter object
print(list(new_grades))

