nome = input('Digite o nome do usuário: ')
senha = input('Digite a senha do usuário: ')

if nome == 'admin' and senha == '1234' or nome == 'convidado' and senha == 'visitante':
    print('Acesso concedido!')
else:
    print('Acesso negado!')