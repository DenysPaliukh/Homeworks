# Calculator

import math


def calc():
    value_1 = "Число_1"
    value_2 = "Число_2"

    try:
        value_1 = float(input("Please enter the first number: "))
    except ValueError:
        print("It's not a number. Try again! ")
        quit()
    try:
        value_2 = float(input("Please enter the second number: "))
    except ValueError:
        print("It's not a number. Try again! ")
        quit()

    value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer:")

    if value_operator == '1':
        result = value_1 + value_2

    elif value_operator == '2':
        result = value_1 - value_2

    elif value_operator == '3':
        result = value_1 * value_2

    elif value_operator == '4':
        result = value_1 / value_2

    else:
        result = "You can't choose other operators, only \n1 '+'\n2 '-'\n3 '*'\n4 '/'"

    print(result)


calc()
while True:
    flag = input("Continue?: \n 1 'Yes' \n 2 'No'")

    if flag == '1':
        calc()

    else:
        break
