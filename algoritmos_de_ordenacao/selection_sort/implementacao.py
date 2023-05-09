def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp

    return vetor

vetor_desordenado = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
vetor_ordenado = selection_sort(vetor_desordenado)
print(vetor_ordenado)