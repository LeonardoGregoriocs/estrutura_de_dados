import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inseri_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def exclui_primeiro_elemento(self):
        self.primeiro = self.primeiro.proximo


    # def pesquisar(self, valor):
    #     import pdb;pdb.set_trace()
    #     atual = self.primeiro
    #     while atual != None:
    #         if atual == valor:
    #             return atual
    #         else:
    #             atual = atual.proximo

lista = ListaEncadeada()
lista.inseri_inicio(1)
lista.inseri_inicio(2)
lista.inseri_inicio(3)
lista.inseri_inicio(4)
lista.inseri_inicio(5)
print("Lista completa")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir primeiro item")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir mais um elemento")
lista.mostrar()

lista.inseri_inicio(4)
print("\nLista após adicionar mais um primeiro item")
lista.mostrar()

#Endereço na memória do primeiro item da lista.
# print(lista.primeiro)
