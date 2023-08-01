
""" string is immutable datatype ? ==> once created cannot be changed """
""" define string"""
name = "mohamed nasser"

"""access string parts using index --> start from zero"""
print(name[6])

"""get len of the string """
print(len(name))

""" count chars in the string ? """
print(name.count('s'))

"""get index of char in the string --> the first occurrence of the char in the string """
print(name.index('a'))


""" perform operation on the string ? """
""" format """
print(name.capitalize())  # retrun new string  ---> first char is capital

print(name.upper())
print(name.lower())
print(name.title())

""" replace string """
message = 'i love iti'  # replace i ---> I
print(message.replace('i', 'I'))

"""format string ? """
no_stds = 25
coursename= 'python'
""" concat ---> all the concat parts must be strings"""
# temp_message= 'we have ' + str(no_stds) + " in " + coursename +" course."
# print(temp_message)
""" using format fun ? """
# tmpsting = "we have  {0}  students in {1} course"
# print(tmpsting.format(no_stds, coursename))
# print(tmpsting.format(coursename, no_stds))

tmpsting = "we have {totalstudents}  students in {iticourse} course"
# keyword argument in formatting the string
print(tmpsting.format(totalstudents=no_stds, iticourse=coursename))
print(tmpsting.format( iticourse=coursename,totalstudents=no_stds))

'f-format string ---> format string according to existing variables'
name ='noha'
work = 'iti'
year = 2019
message = f"my name is {name}, I works at {work}, since {year}"
print(message)

"""accept string from user ---> input """
# name = input("please enter name: ")  # always returns with string
# print(name, type(name))

""" examine string content """

userintput  = input("please enter value : ")
print(userintput.isdigit()) # return True if the string contains numeric value
print(userintput.isalpha()) # return True i the string consists only from alphabets (a-z)
print(userintput.isspace()) # return true if the string consists only from spaces

""" slicing the string ? """
iti = 'information technology institute'
print(iti[4])
print(iti[4:])
print(iti[3:7])
print(iti[::])
print(iti[::-1])


""" ---> strip the string """
message= "           nice to meet you           "
print(len(message))
# print(message.strip())  # strip white spaces from the beginning and the end of the string
# print(message.lstrip())
# print(message.rstrip())

print(message.strip("u &"))  # strip any of the given chars from the beginning and the end of the string
# print(message.lstrip())
# print(message.rstrip())

""" string interpolation"""
fname= 'noha'
mid = 'abdelhady'
lname='shehab'
fullname = fname + mid +  mid + lname
print(fullname)
fullname = fname + mid*2 + lname
print(fullname)

mynum = 10+6j
mynum2=complex(5,7)

print(min(45,5,6,6))
print(max(4,5,6,44,100))
print(round(44.5))
print(round(66,9))


print("o" in 'noha')

""" iterate over the string """
for c in 'mohamed':
    print(f"c= {c}")


