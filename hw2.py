import math

number1 = input('Enter the First Number \n')
if number1.isalpha() or number1 == '':
    print('You should enter just a number!')
    exit()

print('--------------')
print('1. + \n2. - \n3. * \n4. / \n5. ^\n6. % ')

operation = input('Enter the opertaion: \n')
number2 = input('Enter the Second Number \n')

if operation == '1' or operation == '+':
    result = float(number1) + float(number2)
    print(f'The result is {result}')

if operation == 2 or operation == '-':
    result = float(number1) - float(number2)
    print(f'The result is {result}')

if operation == 3 or operation == '*':
    result = float(number1) * float(number2)
    print(f'The result is {result}')

if operation == 4 or operation == '/':
    result = float(number1) / float(number2)
    print(f'The result is {result}')

if operation == 5 or operation == '^':
    result = float(number1) ^ float(number2)
    print(f'The result is {result}')

if operation == 6 or operation == '%':
    result = float(number1) % float(number2)
    print(f'The result is {result}')

print('-----------------------')
op = input('1. Floor\n2. Ceil\n3. Round\n4. Integer\n5. Exit\n ')

if op == '1':
    print(f'The Final result is {math.floor(result)}')
elif op == '2':
    print(f'The Final result is {math.ceil(result)}')
elif op == '3':
    print(f'The Final result is {math.round(result)}')
elif op == '4':
    print(f'The Final result is {int(result)}')
elif op == '5':
    exit()
