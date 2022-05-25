print('\n********** Python Calculator **********')

print('\nSelect the number to required operation:')

operation = input('\n1 - Sum \n2 - Subtraction \n3 - Multiplication \n4 - Division \n\nChoose: ')

if operation == '1':
    num1 = int(input('\nChoose the first number: '))
    num2 = int(input('Choose the second number: '))
    num3 = num1 + num2
    print('\nThe result of sum is %s\n' %(num3))
elif operation == '2':
    num1 = int(input('\nChoose the first number: '))
    num2 = int(input('Choose the second number: '))
    num3 = num1 - num2
    print('\nThe result of subtraction is %s\n' %(num3))
elif operation == '3':
    num1 = int(input('\nChoose the first number: '))
    num2 = int(input('Choose the second number: '))
    num3 = num1 * num2
    print('\nThe result of multiplication is %s\n' %(num3))
elif operation == '4':
    num1 = int(input('\nChoose the first number: '))
    num2 = int(input('Choose the second number: '))
    num3 = num1 / num2
    print('\nThe result of division is %s\n' %(num3))
else:
    print('\nErro! Invalid operation! Choose the number between 1 - 4\n')