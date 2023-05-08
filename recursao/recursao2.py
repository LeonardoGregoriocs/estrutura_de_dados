def soma1(n1):
    soma = 0
    for i in range(n1 + 1):
        soma += i
    return soma

teste = soma1(5)
print(teste)

def soma2(n2):
    if n2 == 0:
        return 0
    return n2 + soma2(n2 - 1)

teste1 = soma2(5)
print(teste1)

# Nem sempre utilizar recursão é o mais rápido para processamento.
