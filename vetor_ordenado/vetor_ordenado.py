import numpy as np

class VetorOrdenado():
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Posição: {i} ||  Número: {self.valores[i]}')

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print("Capacidade máxima atingida")
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1

    def excluir(self, valor):
        posicao_encontrada = self.pesquisar(valor)
        if posicao_encontrada == -1:
            return -1
        else:
            for i in range(posicao_encontrada, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorOrdenado(10)

vetor.inserir(6)
vetor.inserir(4)
vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(1)
vetor.inserir(8)
vetor.inserir(9)

vetor.imprime()
print()

pesquisa_1 = vetor.pesquisar(5)
print(f'A posição do Nº 5 é {pesquisa_1}')

pesquisa_2 = vetor.pesquisar(9)
print(f'A posição do Nº 9 é {pesquisa_2}')

pesquisa_3 = vetor.pesquisar(2)
print(f'A posição do Nº 2 é {pesquisa_3}')
print()

vetor.excluir(5)
vetor.imprime()