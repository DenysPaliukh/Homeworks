#################################### 1
import string

# my_list = ["one", "two", "three", "four", "five"]

# new_list = []


# def reverse_str(my_list):
#    for i in range(0, len(my_list)):
#        return new_list.append(my_list[i])if i % 2 != 0 else new_list.append(my_list[i][::-1])

# print(new_list)

##################################### 2

# my_list = ["aone", "two", "three", "afour", "five"]

# new_list = []


# def start_a(my_list):

#    for i in range(0, len(my_list)):
#        if my_list[i][0:].startswith("a"):
#            return new_list.append(my_list[i])

# print(new_list)

#################################### 3

# my_list = ["aone", "twoa", "three", "afour", "fivea"]

# new_list = []


# def all_a(my_list):

#    for i in range(0, len(my_list)):
#        if "a" in my_list[i]:
#            return new_list.append(my_list[i])

# print(new_list)

#################################### 4

# my_list = [1, 2, 3, '11', '22', 33]

# new_list = []


# def all_str(my_list):
#    for i in my_list:
#        if type(i) is str:
#            return new_list.append(i)

# print(new_list)

################################### 5

# my_str = "uutjghfyrhhhhhhdnbcbbbbb"

# new_list = []


# def single_time(my_str):
#    for i in my_str:
#        if my_str.count(i) == 1:
#            return new_list.append(i)


# print(new_list)

################################# 6

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
# new_list = []

# def inter(my_str_1, my_str_2):

#    new_list = list(set(my_str_1).intersection(set(my_str_2)))

#    return new_list

# print(new_list)

############################### 7

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"

# new_list = []


# def inter(my_str_1, my_str_2):
#    for i in set(my_str_1).intersection(set(my_str_2)):
#        if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
#            return new_list.append(i)

#    print(new_list)


############################### 8
import random
import string

names = ["Jane", "Jack", "John", "Iris", "Tommy"]
domains = ["com", "net", "io", "ua", "us"]


def create_email(names, domains):
    letters = string.ascii_lowercase
    numbers = random.randint(100, 999)
    email = ''.join(
        (random.choice(names), numbers, "@", (random.choice(letters) in range(5, 7)), ".", random.choice(domains)))

    return email

    print(email)
