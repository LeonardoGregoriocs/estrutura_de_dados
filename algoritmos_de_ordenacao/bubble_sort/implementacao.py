def bubble_sort(vetor):
    tamanho_vetor = len(vetor)

    for i in range(tamanho_vetor):
        for j in range(0, tamanho_vetor - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

vetor_desordenado = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
vetor_ordenado = bubble_sort(vetor_desordenado)
print(vetor_ordenado)
