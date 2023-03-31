import os
############################################## 1

filename = "../Homeworks"
dir_list = []
file_list = []
dict_files = {}

files_list = os.listdir(filename)
for file in files_list:
    if os.path.isdir(file):
        dir_list.append(file)
    else:
        file_list.append(file)


def dir_func(files_list):
    dict_files = {"filenames": file_list, "dirnames": dir_list}

    return dict_files


print(dir_func(file_list))


############################################# 2

def dir_sorting(files_list, key=False):
    for file in files_list:
        files_list.sort(reverse=False)

    return files_list


print(dir_sorting(files_list, key=False))

############################################# 3

name = input("введите имя папки/файла: ")


def dict_renew(dict_files, name):
    if '.' in name:
        file_list.append(name)
    else:
        dir_list.append(name)

    dict_files = {"filenames": file_list, "dirnames": dir_list}

    return dict_files


print(dict_renew(dict_files, name))
