idade = int(input('qual sua idade? \n'))
assi = input('voce é assinante? sim ou não \n')

if idade >= 18:
    print('acesso liberado')
elif idade >= 16 and assi == 'sim':
    print('acesso liberado')
else:
    print('acesso negado')