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
        if self.primeiro == None:
            self.imprime_texto()
            return None

        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def exclui_primeiro_elemento(self):
        if self.primeiro == None:
            self.imprime_texto()
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisa(self, valor):
        if self.primeiro == None:
            self.imprime_texto()
            return None

        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return "Elemento não encontrado"
            else:
                atual = atual.proximo
        return atual.valor

    def excluir_posição(self, valor):
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual

    def imprime_texto(self):
        print('A lista está vazia!')


# Instaciar um objeto da classe Lista Encadeada
lista = ListaEncadeada()
lista.inseri_inicio(1)
lista.inseri_inicio(2)
lista.inseri_inicio(3)
lista.inseri_inicio(4)
lista.inseri_inicio(5)
print("Lista completa")
lista.mostrar()

# Exlui elementos um por um
lista.exclui_primeiro_elemento()
print("\nLista após excluir primeiro item")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir mais um elemento")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir mais um elemento")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir mais um elemento")
lista.mostrar()

lista.exclui_primeiro_elemento()
print("\nLista após excluir mais um elemento")
lista.mostrar()

#Endereço na memória do primeiro item da lista.
print(lista.primeiro)

# Pesquisa um elemento
pesquisa = lista.pesquisa(2)
if pesquisa:
    print(f'Encontrado: {pesquisa}')
else:
    print('Não encontrado')

# Excluir uma posição da lista
lista.excluir_posição(3)
