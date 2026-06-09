nota1 = 1
nota2 = 2
nota3 = 3
nota4 = 4

peso1 = float(input('digite peso 1: '))
peso2 = float(input('digite peso 2: '))
peso3 = float(input('digite peso 3: '))
peso4 = float(input('digite peso 4: '))

calc = (nota1*peso1+nota2*peso2+nota3*peso3+nota4*peso4)/(nota1+nota2+nota3+nota4)

print(f'a media ponderada disso ai é: {calc}')