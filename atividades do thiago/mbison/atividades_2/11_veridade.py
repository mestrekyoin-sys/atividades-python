idade = int(input("Digite sua idade: "))

renda_mensal = float(input("Digite sua renda mensal: "))

if idade > 21 and renda_mensal > 2000:
    print("Você está elegível para receber o empréstimo.")
else:
    print("Desculpe, você não atende aos critérios para receber o empréstimo.")