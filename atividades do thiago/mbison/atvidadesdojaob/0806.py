lista = []
dicionario = {'gambiarra': 'solução', 'treta': 'confusção'}

verduras = dict(goiaba = 'fruta', abobora = 'legume', feijão = 'grao')

capitais = {'Brasil': 'Brasilia', 'Russia': 'Moscou', 'Italia': 'Roma'}

print(capitais['Brasil'])
                                                                                                                                                                                 
capitais ['China'] = 'Xangai'
capitais ['China'] = 'Pequim'

print(capitais)

del capitais['Italia']

print(capitais.get('india'))

paises = capitais.keys()
cidades = capitais.values()

print(paises)

for pais in capitais:
    print('bem vindo a', pais)
for pais, cidade in capitais.items():
    print(cidade,'é capital de', pais)

npc = {'nome': 'ferreiro', 'fala': 'precisa de arma ou escudo?', 'itens': { 'espada': 100, 'escudo': 80 }}
