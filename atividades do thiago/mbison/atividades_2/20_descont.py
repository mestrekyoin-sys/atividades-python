idade = int(input('qual sua idade? \n'))
assi = input('voce é estudante? sim ou não \n')

if idade < 18 or idade > 65:
    print('desconto liberado')
else:
    print('desconto negado')