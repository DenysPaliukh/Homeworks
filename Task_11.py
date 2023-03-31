import os
import pathlib
############################################## 1

filename = "../Homeworks"
dir_list = []
file_list = []
dict_files = {}
file_list_1 = []
dir_list_1 = []




def dir_func(filename):
    files_list = os.listdir(filename)
    for file in files_list:
        if os.path.isdir(file):
            dir_list.append(file)
        else:
            file_list.append(file)

    dict_files = {"filenames": file_list_1.append(file_list), "dirnames": dir_list_1.append(dir_list)}
    return dict_files


print(dir_func(filename))

############################################# 2
#key = False
#new_dict = {}


#def sorting_dict(dict_files, key):
#    files_list = os.listdir()
#    for file in files_list:
#        if os.path.isdir(file):
#            dir_list.append(file)
#        else:
#            file_list.append(file)

#        if key is False:
#            file_list.sort(reverse=True)
#            dir_list.sort(reverse=True)
#            dict_files = {"filenames": file_list, "dirnames": dir_list}

#    return dict_files


#print(sorting_dict(dict_files, key))
