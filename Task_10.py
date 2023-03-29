import pathlib
from pathlib import Path

#a = open("authors.txt", "x")

############################################ 1
# path = Path("domains.txt")
# filename = path


# def domains(kkk):
#    with open(filename, 'r') as my_file:
#        data_str = ''.join(my_file.read())
#        my_str = data_str.replace(".", "")
#        my_list = my_str.split("\n")

#    return my_list


# result = domains(path)
# print(result)

############################################# 2

# path = Path("names.txt")
# filename = path
# name_list = []


# def names(kkk):
#    with open(filename, "r") as my_file:
#        data_list = my_file.readlines()
#        for name in data_list:
#            name_list.append(name.split("\t")[1])

#    return name_list


# result = names(name_list)
# print(result)


############################################# 3

path = Path("authors.txt")
filename = path
new_list = []


def dict_authors(kkk):
    with open(filename, "r") as my_file:
        data_list = my_file.readlines()
        for data in data_list:
            if data and "-" in data:
                new_list.append({"date": data.split(" - ")[0]})

    return new_list


result = dict_authors(new_list)
print(result)
