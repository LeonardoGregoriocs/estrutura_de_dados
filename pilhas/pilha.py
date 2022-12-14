import numpy as np

class Pilhas:
    def __init__(self, capacidade) -> None:
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            print(self.__valores[self.__topo])
        else:
            return -1

pilha = Pilhas(5)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.ver_topo()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.ver_topo()