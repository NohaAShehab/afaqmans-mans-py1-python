

info = ["noha",31, "iti", "engineering"]

# unlabeled data ? --->
"""dict ? --> create label for the data key:value pair 

    dict  , comma seperated key:value 
    doesn't allow key duplication
"""



info = {

}

info= {"name":"noha", "age":31, "work":"iti","study":"engineering"}



""" 1- get len of the dict ? """
print(len(info))

""" access elements of dict --> using key"""
print(info["name"])


""" update dict elements"""
info["name"] = "Noha Shehab"  # updated exisiting key ,,, update value
print(info)
info["city"] = "Mansoura"  # add new key:value pair
print(info)


""" remove element from dict """

popped_value=info.pop("city")
print(popped_value)

""" check if element exists in the dict ? """
print(31 in info)  # false --> in operator -- > check if value exists in the dict keys

""" loop over the dict """
# for val in info:  # get keys
#     print(val)

for val in info:  # get keys
    print(f"{val}, {info[val]}")

""" get dict keys , values """
keys = info.keys()  # dict_keys
print(keys) # can be casted to list

values  = info.values()
print(values) # # can be casted to list

items = info.items()
print(items)  #dict_items
items = list(items)
print(items)

""" concat 2 dicts ? """

d1 = {'name':"Ahmed"}
d2 = {"track":"python", "name":"Ali"}
# d3 = d1 + d2
# print(d3)  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

""" update dict content """
d1.update(d2)
print(d1)


""" === clear , del """

d1.clear()