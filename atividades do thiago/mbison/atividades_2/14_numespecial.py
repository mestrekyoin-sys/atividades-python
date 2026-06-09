num = int(input('digite um sumero para saber se é divisivel por 3 e por 5: '))

if num % 5 == 0:
    print('O número é divisívelpor 5.')
elif num % 3 == 0:
    print('o numro é divisivel por 3')
else:
    print('O número não é divisível por 3 e nem por 5.')