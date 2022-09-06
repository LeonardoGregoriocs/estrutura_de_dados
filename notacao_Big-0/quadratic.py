'''A função quadratic recebe esse nome, justamente porque percorre duas vezes
    o valor de entrada. O(n^2). Geralmente quando queremos percorrer uma matriz
    utilizamos a função quadratic do bigO.'''

lista = [1, 2, 3, 4, 5]

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)