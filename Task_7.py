import re

################################### 1

# value = input()

# my_list = str(list[value])

# x = my_list.count("0")

# print(x)

################################## 2

# value = 1005000000

# value_1 = str(value)

# result = 0

# new_str = value_1[::-1]

# for i in new_str:

#    if i == "0":
#        result += 1
#    else:
#        break

# print(result)

#################################### 3

# my_list_1 = [1, 2, 3, 4, 5]

# my_list_2 = ['A', 'B', 'C', 'D', 'E', 'F']

# my_result = my_list_1[1::2]

# for i in my_list_2[1::2]:
#    my_result.append(i)

# print(my_result)

####################################### 4

# my_list = [1, 2, 3, 4]

# new_list = my_list[1:]

# new_list.append(my_list[0])

# print(new_list)

##################################### 5

# my_list = [1, 2, 3, 4]

# new_list = str(my_list[0])

# my_list.pop(0)

# print(id(my_list))

# my_list.extend(new_list)

# print(id(my_list))

# print(my_list)

###################################### 6
#import re

#my_str = "43 більше ніж 34, але менше ніж 56"

#pattern = '[0-9]+'
#my_list = list(re.findall(pattern, my_str))

#new_list = []
#for i in my_list:
#    new_list.append(int(i))

#result = sum(new_list)
#print(result)

####################################### 7

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]

# result = 0

# for i in range(1, len(my_list) - 1):

#    if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#        result += 1

# print(result)

######################################## 8

# my_list = [1, 2, 3, '11', '22', 33]

# new_list = []

# for i in my_list:
#    if type(i) is str:
#        new_list.append(i)

# print(new_list)

##################################### 9

#my_str = "uutjghfyrhhhhhhdnbcbbbbb"
#new_list = []

#for i in my_str:
#    if my_str.count(i) == 1:
#        new_list.append(i)

#print(new_list)


##################################### 10

#my_str_1 = "aaaasdf1"
#my_str_2 = "asdfff2"

#new_list = list(set(my_str_1).intersection(set(my_str_2)))

#print(new_list)

###################################### 11

#my_str_1 = "aaaasdf1"
#my_str_2 = "asdfff2"

#new_list = []

#for i in set(my_str_1).intersection(set(my_str_2)):
#    if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
#        new_list.append(i)

#print(new_list)


