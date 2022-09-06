import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i]}')

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao_encontrada = self.pesquisar(valor)
        if posicao_encontrada == -1:
            return -1
        else:
            for i in range(posicao_encontrada, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(5)
vetor.imprime()
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)
vetor.imprime()

numero_pesquisado = vetor.pesquisar(10)
print(f'Posição: {numero_pesquisado}')

exclui_numero = vetor.excluir(2)

vetor.imprime()
