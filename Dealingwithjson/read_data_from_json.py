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

def readdata():
    import  json

    try:
        fileobject =open("users.json", "r")
        # TextIOWrapper --> this object refers to the file
    except Exception as e:
        print(e)
        exit()
    else:
        print(fileobject)
        data = fileobject.read() # read file content into one string
        ## convert string to list of dict
        print(data)
        objects_list = json.loads(data)
        print(objects_list, type(objects_list))
        fileobject.close()
        return objects_list
