from timeit import timeit

#O(n) -> Pois podemos passar tanto um número por parametro ou direto no range.
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]

    return str(lista)

#0(1)
def lista2():
    return range(1000)

print(timeit(lista1()))
print(timeit(str(lista2())))