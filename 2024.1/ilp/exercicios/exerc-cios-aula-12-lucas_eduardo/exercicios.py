# 1. Escreva um programa para ler e armazenar valores em uma matriz de
# tamanho m por n. A quantidade de linhas e colunas deve ser definida
# pelo usuário e a matriz deve ser inicializada com valor 0 em todas as
# posições. O programa deverá solicitar ao usuário um valor inteiro
# positivo para armazenar em cada uma das posições da matriz. Caso o
# usuário digite um valor negativo, esse valor deverá ser dobrado e
# tornado positivo e em seguida inserido na respectiva posição. Ao final,
# exiba os valores da matriz resultante. Considere que os valores de m=2
# e n=3 e as entradas conforme exemplo:
# Entrada: 1 -2 5 Saída: 1 4 5
# 3 4 -4 3 4 8

# Definindo o número de linhas e colunas
# linhas = int(input("Digite a quantidade de linhas da matriz: "))
# colunas = int(input("Digite a quantidade de colunas da matriz: "))

# matriz_NxM = []
# for i in range(linhas):
#     linha = []
#     for j in range(colunas):
#         valor = 0
#         linha += [valor]
#     matriz_NxM += [linha]

# for x in range(linhas):
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x}, {y}): "))
#         if valor < 0 :
#             valor = (-valor) * 2
#             linha += [valor]
#         else:
#             linha += [valor]
#     matriz_NxM += [linha]

# # Exibindo a matriz
# for linha in matriz_NxM:
#     print(linha)

# 2. Escreva um programa para ler e armazenar valores em duas matrizes (matriz1
# e matriz2) de tamanho m por n. A quantidade de linhas e colunas deve ser
# definida pelo usuário, bem como os valores de cada matriz. O Programa
# deverá comparar os valores de cada posição e criar uma nova matriz inserindo
# o valor 1, caso o valor matriz1 seja maior que o matriz2, inserir o valor 2 caso
# o valor de matriz2 seja maior que o de matriz1, ou zero caso contrário. Ao final
# exiba os valores das 3 matrizes.
# matriz1 = [ matriz2 = [ matriz_resultado = [
# [1, 5, 7], [3, 2, 9], [2, 1, 2],
# [8, 3, 9], [8, 3, 1], [0, 0, 1],
# [4, 6, 2] [1, 8, 7], [1, 2, 2],
#         ]         ]           ]

# linhas = int(input("Digite a quantidade de linhas da matriz: "))
# colunas = int(input("Digite a quantidade de colunas da matriz: "))

# matriz_1_NxM = []
# for x in range(linhas):
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x}, {y}) da 1ª matriz: "))
#         linha += [valor]
#     matriz_1_NxM += [linha]

# matriz_2_NxM = []
# for x in range(linhas):
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x}, {y}) da 2ª matriz: "))
#         linha += [valor]
#     matriz_2_NxM += [linha]

# matriz_3_NxM = []
# for x in range(linhas): # Número de linhas
#     valor = 0
#     linha = []
#     for y in range(colunas): # Número de colunas
#         if matriz_1_NxM[x][y] > matriz_2_NxM[x][y]:
#             valor = matriz_1_NxM[x][y]
#             linha += [valor]
#         elif matriz_1_NxM[x][y] < matriz_2_NxM[x][y]:
#             valor = matriz_2_NxM[x][y]
#             linha += [valor]
#         else:
#             valor = 0
#             linha += [valor]
#     matriz_3_NxM += [linha]

# # Exibindo as matrizes
# print("Primeira matriz: ")
# for linha in matriz_1_NxM:
#     print(linha)
# print("Segunda matriz: ")
# for linha in matriz_2_NxM:
#     print(linha)
# print("Terceira matriz: ")
# for linha in matriz_3_NxM:
#     print(linha)


# 3. Escreva um programa para realizar uma operação aritmética (+, -,
# /, *, %) entre os valores de duas matrizes de tamanho m por n.
# A quantidade de linhas e colunas deve ser definida pelo usuário,
# bem como os valores de cada matriz. O programa deverá
# apresentar um menu com as opções de operações e realiza-las até
# que o usuário digite o valor 0 como operação. Ao finalizar as
# operações o programa deverá exibir a matriz resultado e retornar
# para o menu inicial. Ao encerrar o programa, deverá ser exibida
# uma mensagem de encerramento ao usuário.

# linhas = int(input("Digite a quantidade de linhas da matriz: "))
# colunas = int(input("Digite a quantidade de colunas da matriz: "))

# matriz_1_NxM = []
# for x in range(linhas):
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x}, {y}) da 1ª matriz: "))
#         linha += [valor]
#     matriz_1_NxM += [linha]

# matriz_2_NxM = []
# for x in range(linhas):
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x}, {y}) da 2ª matriz: "))
#         linha += [valor]
#     matriz_2_NxM += [linha]

# print("Tabela de operações: \n0. Finalizar operações\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Resto da divisão")
# matriz_3_NxM = []
# for x in range(linhas): # Número de linhas
#     linha = []
#     for y in range(colunas): # Número de colunas
#         valor = 0
#         operacao = int(input(f"Operação desejada para a posição ({x}, {y}) da 3ª matriz: "))
#         if operacao == 0:
#             valor = ""
#             linha += valor
#             break
#         elif operacao == 1:
#             valor = matriz_1_NxM[x][y] + matriz_2_NxM[x][y]
#             linha += [valor]
#         elif operacao == 2:
#             valor = matriz_1_NxM[x][y] - matriz_2_NxM[x][y]
#             linha += [valor]
#         elif operacao == 3:
#             soma = 0
#             for z in range(linhas):
#                 valor += matriz_1_NxM[x][z] * matriz_2_NxM[z][y]
#             linha += [valor]
#         elif operacao == 4:
#             soma = 0
#             for z in range(linhas):
#                 valor += round(matriz_1_NxM[x][z] / matriz_2_NxM[z][y], 2)
#             linha += [valor]
#         elif operacao == 5:
#             if ((matriz_1_NxM[x][y] % matriz_2_NxM[x][y]) == 0):        
#                 valor = round(matriz_1_NxM[x][y] % matriz_2_NxM[x][y], 2)
#             else:
#                 valor = matriz_1_NxM[x][y] % matriz_2_NxM[x][y]
#             linha += [valor]
#     matriz_3_NxM += [linha]

# # Exibindo as matrizes
# print("Primeira matriz: ")
# for linha in matriz_1_NxM:
#     print(linha)
# print("Segunda matriz: ")
# for linha in matriz_2_NxM:
#     print(linha)
# print("Terceira matriz: ")
# for linha in matriz_3_NxM:
#     print(linha)