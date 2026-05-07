number1 = input('Enter the number: ')
num1 = int(number1)

sign = input('Enter the operator (+, -, *, /): ')

number2 = input('Enter the number: ')
num2 = int(number2)

if sign == '+':
    print("Your result is", num1 + num2)
elif sign == '-':
    print("Your result is", num1 - num2)
elif sign == '*':
    print("Your result is", num1 * num2)
elif sign == '/':
    if num2 != 0:
        print("Your result is", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Please enter +, -, * or /")
    