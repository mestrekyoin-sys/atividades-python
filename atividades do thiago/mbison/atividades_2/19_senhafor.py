senha = input('digite sua senha com 8 coisa e uma coisa maiuscula e um numero ai: ')

temnum = False
temmaius = False

if len(senha) < 8:
    print('quantidade de caracteres negada')
else:
      for car in senha:
        if car.isupper(): 
            temmaius = True
        if car.isdigit():
            temnum = True
if not temmaius:
    print('nananananinanao')
elif not temnum:
    print('ta faltando numero')
else:
    print('senha massa')