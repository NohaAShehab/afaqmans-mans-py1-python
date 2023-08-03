"""

    dealing with file
    1-open file
        fileobject=open(filename, mode of openinng)
            mode --> r ==> read
            w===> write
            a ===> append
    2- decide operation
        r ==> fileobject.read(), readlines(), seek()
        w ==> fileobject.write(data) , writelines(iterable) , seek()
    3-closing the file
        fileobject.close()

"""

try:
    fileobject =open("students.txt", "r")
    # TextIOWrapper --> this object refers to the file
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)
    data = fileobject.read() # read file content into one string
    print(data)
    fileobject.seek(1)  # reset file cursor back to the beginning of the file
    data = fileobject.readlines()  # read file content into list line by line
    print(data)
    fileobject.close()









