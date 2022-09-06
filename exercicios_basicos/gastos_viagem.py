def entrada_dados():
    tempo_gasto = int(input("Digite o tempo da viagem: "))
    velocidade = int(input("Digite a velocidade: "))

    return tempo_gasto, velocidade

def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcula_quantidade_de_litros(distancia):
    qnt_litros = distancia/12
    return qnt_litros

def apresenta_valor(quantidade_litros):
    print(f"Quantidade de litros gastos na viagem: {qnt_litros:.2f}")

tempo, velocidade = entrada_dados()
distancia = calcular_distancia(tempo, velocidade)
qnt_litros = calcula_quantidade_de_litros(distancia)
apresenta_valor(qnt_litros)