def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        marcado = vetor[i]

        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado

    return vetor

vetor_desordenado = [15, 34, 8, 3]
vetor_ordenado = insertion_sort(vetor_desordenado)
print(vetor_ordenado)