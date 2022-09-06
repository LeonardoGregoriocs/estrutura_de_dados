'''Para calcularmos o big-O de um programa que tem mais código, precisamos quebrar
    ele em algumas pedaços menores.
    soma do Big-O -> O(1) + O(5) + O(n) + O(n) + O(3)
    total = O(9) + O(2n) -> O(n)
'''

lista = [1, 2, 3, 4, 5]

def combination(n):
    # O(1) -> Constant
    print(n[0])

    # O(5) -> Constant
    for i in range(5):
        print(i)

    # O(n) -> Linear
    for i in n:
        print(i)

    # O(n) -> Linear
    for i in n:
        print(i)

    # O(3)
    print('Python')
    print('Python')
    print('Python')