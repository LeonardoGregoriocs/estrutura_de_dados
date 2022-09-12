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

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos -1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -=1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila está vazia")
            return

        valor = self.valores[self.numero_elementos -1]
        self.numero_elementos -= 1
        return valor

    def ver_primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

    def ver_fila_completa(self):
        return self.valores

fila = FilaCircular(5)
fila_vazia = fila.ver_primeiro()
print("Fila está vazia:", fila_vazia)

fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
fila.enfileirar(40)
fila.enfileirar(20)

print(f"Fila: {fila.ver_fila_completa()}")

fila.desenfileirar()
fila.enfileirar(24)

primeiro_valor = fila.ver_primeiro()
print(f"O primeiro valor é {primeiro_valor}")

print(f"Fila: {fila.ver_fila_completa()}")
