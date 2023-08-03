"""

    dealing with file
    1-open file
        fileobject=open(filename, mode of openinng)
            mode --> r ==> read
            w===> write 0---> when you open file with write mode> if the file doesn't exists
            python will try to create it ?
            if file exists > python open file for writing starting from the beginning of file
            --->remove old content
            a ===> append
    2- decide operation
        r ==> fileobject.read(), readlines(), seek()
        w ==> fileobject.write(data) , writelines(iterable) , seek()
    3-closing the file
        fileobject.close()

"""

try:
    fileobject =open("mycv.txt", "w")
    # TextIOWrapper --> this object refers to the file
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)

    # fileobject.write("hello world\n")
    # fileobject.write("we need a break\n")
    # fileobject.write("python is easy\n")
    fileobject.write('########################################\n')
    fileobject.writelines(["line1\n", 'line2\n', "test\n"])

    fileobject.close()
