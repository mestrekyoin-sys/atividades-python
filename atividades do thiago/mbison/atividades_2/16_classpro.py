cate = input('digite a categoria do produto [A, B ou C]: ')
prec = float(input('digite o preço desse produto: '))

if cate == 'A'and prec > 100:
    print('seu produto é premium')
elif cate == 'B' and prec > 200:
    print('seu produto é premium')
else:
    print('seu produto nao é premium')
