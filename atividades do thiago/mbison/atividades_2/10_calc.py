num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opera = input('Digite a operação desejada (soma, subtração, multiplicação, divisão): \n')

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1/num2

if opera == 'soma':
    print(f'O resultado da soma é: {soma}')
elif opera == 'subtração':
    print(f'O resultado da subtração é: {subtracao}')
elif opera == 'multiplicação':
    print(f'O resultado da multiplicação é: {multiplicacao}')
elif opera == 'divisão':
    if divisao != 0:
        print(f'O resultado da divisão é: {divisao}')
    else:
        print('Erro: Divisão por zero não é possivel.')
else:
    print('Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão.')