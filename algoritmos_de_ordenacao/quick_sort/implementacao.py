def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        quick_sort(vetor, inicio, posicao - 1)
        quick_sort(vetor, posicao + 1, final)
    return vetor

vetor_desordenado = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
vetor_ordenado = quick_sort(vetor_desordenado, 0, len(vetor_desordenado) - 1)
print(vetor_ordenado)