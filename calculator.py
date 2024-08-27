def calculator(sign, first_number, second_number):
    if sign == '+':
        return first_number + second_number
    elif sign == '-':
        return first_number - second_number
    elif sign == '*':
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number
print(calculator(input("Enter sign> "), int(input("Enter first number> ")), int(input("enter second number> "))))
