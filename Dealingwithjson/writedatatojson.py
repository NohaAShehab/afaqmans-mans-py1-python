import  json
from read_data_from_json import  readdata
# first you need to read the json content to a list
old_data = readdata()  # list of dict
## append dict ---> to the read list
element4={"id": 4, "name": "test"}
old_data.append(element4)


# convert list of dicts to a string
data = json.dumps(old_data)
# open file with mode write

# save data


try:
    fileobject =open("users.json", "w")
    # TextIOWrapper --> this object refers to the file
except Exception as e:
    print(e)
    exit()
else:
    print(fileobject)
    fileobject.write(data)
    fileobject.close()
