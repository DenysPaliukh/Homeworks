#################################### 1

#my_list = ["one", "two", "three", "four", "five"]

#new_list = []


#def reverse_str(kkk):
#    for i in range(0, len(my_list)):
#        if i % 2 != 0:
#            new_list.append(my_list[i])
#        else:
#            new_list.append(my_list[i][::-1])
#    return my_list


#result = reverse_str(my_list)

#print(result)

##################################### 2

# my_list = ["aone", "two", "three", "afour", "five"]

# new_list = []


# def start_a(kkk):
#    for i in range(0, len(my_list)):
#        if my_list[i][0:].startswith("a"):
#            new_list.append(my_list[i])
#    return new_list


# result = start_a(my_list)

# print(result)

#################################### 3

# my_list = ["aone", "twoa", "three", "afour", "fivea"]

# new_list = []


# def all_a(kkk):
#    for i in range(0, len(my_list)):
#        if "a" in my_list[i]:
#            new_list.append(my_list[i])
#    return new_list


# result = all_a(new_list)

# print(result)

#################################### 4

# my_list = [1, 2, 3, '11', '22', 33]

# new_list = []


# def all_str(kkk):
#    for i in my_list:
#        if type(i) is str:
#            new_list.append(i)
#    return new_list


# result = all_str(new_list)

# print(result)

################################### 5

# my_str = "uutjghfyrhhhhhhdnbcbbbbb"

# new_list = []


# def single_time(kkk):
#    for i in my_str:
#        if my_str.count(i) == 1:
#            new_list.append(i)
#    return new_list


# result = single_time(new_list)


# print(result)

################################# 6

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
# new_list = []


# def inter(iii, kkk):
#    new_list = list(set(my_str_1).intersection(set(my_str_2)))

#    return new_list


# result = inter(my_str_1, my_str_2)

# print(result)

############################### 7

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"

# new_list = []


# def inter(iii, kkk):
#    for i in set(my_str_1).intersection(set(my_str_2)):
#        if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
#            new_list.append(i)
#    return new_list


# result = inter(my_str_1, my_str_2)

# print(new_list)


############################### 8
# import random
# import string

# names = ["Jane", "Jack", "John", "Iris", "Tommy"]
# domains = ["com", "net", "io", "ua", "us"]


# def create_email(n, d):
#    letters = ''.join(random.choices(string.ascii_lowercase, k=7))
#    numbers = str(random.randint(100, 999))
#    email = ''.join(
#        (random.choice(names), numbers, "@", letters, ".", random.choice(domains)))

#    return email


# result = create_email(names, domains)

# print(result)
