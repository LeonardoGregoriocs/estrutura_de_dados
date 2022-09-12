from mimetypes import init
import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia")
            return

        if self.final == self.capacidade -1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila já está vazia")
            return

        temp = self.valores[self.inicio]
        self.inicio +=1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        self.numero_elementos -=1
        return temp

    def ver_primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

    def ver_fila_completa(self):
        return self.valores

fila = FilaCircular(5)
fila_vazia = fila.ver_primeiro()
print("Fila está vazia:", fila_vazia)

fila.enfileirar(1)
elemento1 = fila.ver_primeiro()
print(f"O número {elemento1} está no inicio!")

fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

fila.desenfileirar()
fila.desenfileirar()

fila.enfileirar(6)
fila.enfileirar(7)

fila_completa = fila.ver_fila_completa()
print(f"Fila completo = {fila_completa}")

print(fila.inicio)
print(fila.final)