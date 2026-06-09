numero = int('Digite um numero inteiro: ')
numero1 = int('Digite outro numero inteiro: ')
numero2 = int('Digite outro numero inteiro: ')

if numero > numero1 and numero > numero2:
    print(f'{numero} é o maior número.')
elif numero1 > numero and numero1 > numero2:
    print(f'{numero1} é o maior número.')
else:
    print(f'{numero2} é o maior número.')