import pathlib
from pathlib import Path

############################################ 1
#path = Path("domains.txt")


#def domains(path):
#    with open(path, 'r') as my_file:
#        data_str = ''.join(my_file.read())
#        my_str = data_str.replace(".", "")
#        my_list = my_str.split("\n")

#    return my_list


#result = domains(path)
#print(result)

############################################# 2

# path = Path("names.txt")
# name_list = []


# def names(path):
#    with open(path, "r") as my_file:
#        data_list = my_file.readlines()
#        for name in data_list:
#            name_list.append(name.split("\t")[1])

#    return name_list


# print(names(path))

############################################# 3

# path = Path("authors.txt")
# new_list = []


# def dict_authors(path):
#    with open(path, "r") as my_file:
#        data_list = my_file.readlines()
#        for data in data_list:
#            if data and "-" in data:
#                new_list.append({"date": data.split(" - ")[0]})
#    return new_list


# print(dict_authors(path))
