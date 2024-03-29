def shell_sort(vetor):
    intervalo = len(vetor) // 2

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
                vetor[j] = temp
        intervalo //= 2

    return vetor

vetor_desordenado = [15, 34, 8, 3]
vetor_ordenado = shell_sort(vetor_desordenado)
print(vetor_ordenado)