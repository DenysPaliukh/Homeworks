
value = input()

print(value[2])

###########################################

value = input()

print(value[-2])

###########################################

value = input()

print(value[0:5])

###########################################

value = input()

print(value[:-2:1])

###########################################

value = input()

print(value[1::2])

###########################################

value = input()

print(value[::2])

###########################################

value = input()

print(value[::-1])

############################################

value = input()

print(value[::-2])

############################################

value = input()

print(len(value))

############################################

string = "Word Word Word Word Word"

result = string.count("Word")

print(result)

###########################################

s = input()

ch = input()

for letter in s:
    if letter == ch in s:
        print(letter)

######### Индийский код

value = input()

x = len(value)

y = value[1:x-1:]

z = y.replace("h", "H")

print(value[0]+z+value[:x-1:x])
