while True:
    a = float(input('Digite o valor do lado "a": '))
    b = float(input('Digite o valor do lado "b": '))
    c = float(input('Digite o valor do lado "c": '))

    # Verifica se é um triângulo reto (a² = b² + c²)
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print('Os lados fornecidos formam um triângulo reto.')
    elif a <= 0 or b <= 0 or c <= 0:
        print('Os lados devem ser maior que zero. Por favor, tente novamente.')
    else:
        print('Os lados fornecidos não formam um triângulo reto.')