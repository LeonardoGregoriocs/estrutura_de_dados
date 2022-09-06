from timeit import timeit

#Nessa função, o número de passos é de acordo com o parametros N, ou seja, se for passado o numero 100, terá 100 passos.
# O(n)
def soma1(n):
    soma = 0
    operacao = 0
    for i in range(n + 1):
        operacao += 1
        soma += i
    print(operacao)
    return str(soma)

#Já nessa função temos 3 passos, independente do número que passarmos por parametros.
# O(3) -> Multiplicação, adição e divisão.
def soma2(n):
    return str((n * (n + 1)) / 2)

print(f"Soma1: {timeit(soma1(10000))}")
print(f"Soma2: {timeit(soma2(10000))}")