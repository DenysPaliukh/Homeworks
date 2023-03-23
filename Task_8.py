
################################################ 1

my_list = ["one", "two", "three", "four", "five"]

new_list = []

for i in range(0, len(my_list)):
    if i % 2 != 0:
        new_list.append(my_list[i])

    else:
        new_list.append(my_list[i][::-1])

print(new_list)

##################################################### 2

#my_list = ["aone", "two", "three", "afour", "five"]

#new_list = []

#for i in range(0, len(my_list)):
#    if my_list[i][0:].startswith("a"):
#        new_list.append(my_list[i])

#print(new_list)

##################################################### 3

#my_list = ["aone", "twoa", "three", "afour", "fivea"]

#new_list = []

#for i in range(0, len(my_list)):
#    if "a" in my_list[i]:
#        new_list.append(my_list[i])

#print(new_list)

###################################################### 4

#my_list = [{"name": "Johny", "age": 15}, {"name": "Jane", "age": 25}, {"name": "Jack", "age": 45}]

#name_list = []

#len_name_list = []

#average_list = []

#oldest_one = 0

#for age in my_list:
#    if oldest_one < age["age"]:
#        oldest_one = age["age"]

#for age in my_list:
#    if age["age"] == oldest_one:
#        name_list.append(age["name"])

#print(name_list)

#max_name = max(my_list[0]["name"], my_list[1]["name"], my_list[2]["name"])

#len_name_list.append(max_name)

#print(len_name_list)

#average_list.extend([my_list[0]["age"], my_list[1]["age"], my_list[2]["age"]])

#av_age = sum(average_list) / len(average_list)

#print(av_age)

############################################ 5

#my_dict_1 = {1: 1, 2: 2}
#my_dict_2 = {11: 11, 2: 22}

#my_dict_1_keys = list(my_dict_1.keys())
#my_dict_2_keys = list(my_dict_2.keys())

#my_dict_1_keys.extend(my_dict_2_keys)

#print(my_dict_1_keys)

#diff = (my_dict_1.keys() - my_dict_2.keys())

#new_list = list(diff)

#print(new_list)

#new_dict = {key: my_dict_1[key] for key in new_list} # честно подсмотрено и украдено

#print(new_dict)

#new_dict_2 = my_dict_1.copy()  # это тоже честно украдено. до конца не понятно, буду разбираться

#for key in my_dict_2:
#    if key in new_dict_2:
#        if key in new_dict_2:
#            new_dict_2[key] = [new_dict_2[key], my_dict_2[key]]
#        else:
#            new_dict_2[key] = my_dict_2[key]

#print(new_dict_2)
