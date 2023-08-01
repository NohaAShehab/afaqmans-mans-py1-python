

""" tuple

    ---> collection of data from different datatypes
    is immutable datatype-- -> once created cannot be changed
"""

"1- define a tuple"
t =()
myt = tuple()
#
"""2- tuple can hold different data from different datatypes"""
#
students = ("Mohamed Samir", "Tag", ('Moaz', "python"), 1 , 2023, True,
            ["html", 'css', 'js', 'python', 'django', 'postgres'], 'iti', 'iti')
#
""" access tuple elements using index start from 0 """
print(students[1])
print(students[3])
print(students[6][3])
print(students[-1])

#
""" get len of the tuple"""
print(len(students))

"count element occurrence in the tuple "
print(students.count("iti"))

"get index of element in the tuple --> return index of the first occurence of the element"
print(students.index('iti'))
#
""" check if element exists in a tuple --> in operator """
print("iti" in students)
#
""" loop over the tuple elements """
for item in students:
    print(item)

# """ tuple is immutable datatype """
#

""" concat 2 tuples """

basic_course = ("math", "physics")
skill_courses= ('python', 'databases')
coursetuple = basic_course  + skill_courses

""" min , max --> tuple """

print(min((4,5,6,2323,345,35)))

""" empty tuples are falsy values """
#
""" cast string to tuple and viseversa"""
#
name='noha'
#
name =tuple(name)
print(name)
#
""" convert tuple to string  --> tuple elements must be string """
message = ("I", "love", "python")
message = '_'.join(message)
print(message)

"""cast list to tuple ? """
myl =[4,5,6,True]
myl= tuple(myl)
print(myl)

""" tuple of one element"""
students_info= ('ahmed',)
print(students_info, type(students_info))