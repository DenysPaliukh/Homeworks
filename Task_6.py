
my_list = [12, 24, 1323, 234, 987, 9832, 1, 234]

for x in my_list:
    if x > 100:
        print(x)

###################################################

my_list = [12, 24, 1323, 234, 987, 9832, 1, 234]

my_results = []

for x in my_list:
    if x > 100:
        my_results.append(x)
print(my_results)

###################################################

my_list = [1, 2, 3, 4, 5]

my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-1] + my_list[-2])

print(my_list)



