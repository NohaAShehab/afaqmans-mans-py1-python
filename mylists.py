

""" list

    ---> collection of data from different datatypes
"""

"1- define a list"
l =[]
myl = list()

"""2- list can hold different data from different datatypes"""

students = ["Mohamed Samir", "Tag", 'Moaz', "python", 1 , 2023, True,
            ["html", 'css', 'js', 'python', 'django', 'postgres'], 'iti', 'iti']

""" access list elements using index start from 0 """
print(students[1])
print(students[3])
print(students[7][3])
print(students[-1])
""" list --> mutable datatype --> update content of the list  --> at existing index"""
print(students)
students[2]='updated'
print(students)
# students[100]= 'any value'  #list assignment index out of range

""" get len of the list"""
print(len(students))

"count element occurrence in the list "
print(students.count("iti"))

"get index of element in the list --> return index of the first occurence of the element"
print(students.index('iti'))

""" check if element exists in a list --> in operator """
print("iti" in students)

""" loop over the list elements """
for item in students:
    print(item)

""" list is mutable datatype """

""" append element to the list"""
students.append("omar") # add element to the end of the list
print(students)

""" insert element in the list"""
students.insert(6, 'Ali')
print(students)

students.insert(100 , 'inserted value')  # insert element at the end of the list

""" remove element from the list """


"""1- pop the element """
print(students)
popped_val=students.pop()  # return with the popped value --> return with the last element in the list
# print(students)
print(popped_val)

""" pop element at certain index ? """

popped_element = students.pop(6)
print(popped_element)

"""remove the element from the list ? """
students.remove("iti")  # remove first occurrence of the element
print(students)

""" concat 2 list """

basic_course = ["math", "physics"]
skill_courses= ['python', 'databases']
courselist = basic_course  + skill_courses

""" extend a list """

basic_course.extend(skill_courses)
print(basic_course)

""" sorting list elements  ---> depends ? ==> comparison ===> elements must be from the same type"""

# names = ["ahmed", "mohamed", 'Ali', "Zeyad"]
# names.sort()## sort the same object  ---> ascending
# print(names)

names = ["ahmed", "mohamed", 'Ali', "Zeyad"]
names.sort(reverse=True)## sort the same object  ---> ascending
print(names)


""" reverse a list"""
students.reverse()
print(students)

""" min , max --> list """

print(min([4,5,6,2323,345,35]))

""" empty lists are falsy values """

""" cast string to list and viseversa"""

name='noha'

name =list(name)
print(name)

""" convert list to string  --> list elements must be string """
message = ["I", "love", "python"]
message = '_'.join(message)
print(message)