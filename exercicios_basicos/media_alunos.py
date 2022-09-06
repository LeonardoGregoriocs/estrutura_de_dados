alunos = {}

for i in range(1, 4):
    nome = input("Digite seu nome: ")
    nota = int(input("Digite sua nota: "))
    alunos[nome] = nota

soma_notas = 0
for valor in alunos.values():
    soma_notas += valor

media = soma_notas / 3
print(media)