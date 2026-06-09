idade = int(input("qual a idade: "))

if idade <= 12:
    print('criança')
elif idade >= 13 and idade <= 17:
    print('adolescente')
elif idade >= 18 and idade <= 59:
    print('adulto')
elif idade >= 60:
    print('idoso')