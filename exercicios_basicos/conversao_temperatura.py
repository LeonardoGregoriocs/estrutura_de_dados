def conversao_temperatura():
    temperatura_celsius = int(input("Digite a temperatura em Celsius: "))
    return temperatura_celsius

def calculo_de_conversao(temperatura_celsius):
    temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5
    return temperatura_fahrenheit

def imprimi_temperatura_convertida(temperatura_fahrenheit):
    print(temperatura_fahrenheit)

temperatura_celsius = conversao_temperatura()
temperatura_fahrenheit = calculo_de_conversao(temperatura_celsius)
imprimi_temperatura_convertida(temperatura_fahrenheit)