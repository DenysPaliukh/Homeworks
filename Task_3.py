# Calculator

import math

try:
    value_1 = float(input("Please enter the first number: "))
except ValueError:
    print(float(input("It's not a number. Try again: ")))

try:
    value_2 = float(input("Please enter the second number: "))
except ValueError:
    print(float(input("It's not a number. Try again: ")))

try:
    value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer:")
except ValueError:
    print(input("Wrong operator! Try again: "))

try:
    if value_operator == '1':
        result = value_1 + value_2

    elif value_operator == '2':
        result = value_1 - value_2

    elif value_operator == '3':
        result = value_1 * value_2

    elif value_operator == '4':
        result = value_1 / value_2

except ZeroDivisionError:
    print(input("You can't divide by zero!"))

print(result)


