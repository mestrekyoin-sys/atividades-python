'''lista_aluno = []
while True:
    aluno = input('digite o aluno ai mane: ')
    if aluno == 'sair':
        break
    print(aluno)
    lista_aluno.append(aluno.capitalize())
    print(lista_aluno)
#continue TUNTUNTUTNTUTNTUTNTUTNTUTNT
while True:
    numero = int(input('digita um numeor ai nalmoral: '))
    if numero == 0:
        break
    if numero % 2 == 0:
        print(f'wow, isso deu {numero} que impressionantemente, é par doido, taligado do bagui?')
        continue
    print(f"o numero {numero} é impar doudo")'''
#for

'''palavra = 'oi, posso falar?'
for letra in palavra:
    if letra == 'r':
        break
    if letra == 'l':
        continue
    print(letra)'''

#unoiutatr
import random
soma = 0
for dado in range(0,3):
    soma += random.randint(1,6)
    if soma < 6:
        print('falha')
    elif soma >= 6 and soma <=12:
        print('sucesso')
    else:
        print('THE ROOOOOOCKK')
        
# dungeon
iten = [
    'espada', 'poção','escudo','cajado','mapa','armadura','tesouro','nothing','é um bixo doido','poção duvidosa'
]
random.shuffle(iten)
escolha = int(input('escolha de 0 a 9 safado: '))
print(iten[escolha])