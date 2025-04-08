###1 Escreva um programa que imprima na tela os seguintes valores:
#2 4 6 8 10 12 ...

# for x in range(1,13):
#     if x % 2 == 0:
#         print(x, end=", ")


###2 Escreva um programa que solicite do usuário um valor positivo e
#imprima todos os números inteiros de 1 até o número digitado pelo
#usuário. Ao término, informe que o programa foi encerrado.

# n = int(input("Digite um número positivo: "))
# for x in range(1,n+1):
#     print(x, end=", ")
# print("\n Programa encerrado.")


###3 Escreva um programa que solicite do usuário dois valores positivos
#e imprima todos os números inteiros dentro desse intervalo. O
#algoritmo deve armazenar cada valor em duas variáveis diferentes
#(v_ini e v_fim). Ao término, informe que o programa foi encerrado.

# v_ini = int(input("Digite o início do intervalo: "))
# v_fim = int(input("Digite o fim do intervalo: "))

# for x in range(v_ini, v_fim+1):
#     print(x, end=", ")
# print("\n Programa encerrado.")


###4 Escreva um programa que solicite do usuário dois valores positivos e imprima
#todos os números inteiros dentro desse intervalo excluindo-se o valor inicial do
#intervalo e o valor final. Ao término, informe que o programa foi encerrado.

# v_ini = int(input("Digite o início do intervalo: "))
# v_fim = int(input("Digite o fim do intervalo: "))

# for x in range(v_ini+1, v_fim):
#     print(x, end=", ")
# print("\n Programa encerrado.")


###5 Escreva um programa que solicite do usuário dois valores positivos. Em
#seguida, imprima todos os números primos contidos dentro desse intervalo e o
#somatório desses números primos. Ao término, informe que o programa foi
#encerrado.

# v_ini = int(input("Digite o início do intervalo: "))
# v_fim = int(input("Digite o fim do intervalo: "))
# soma = 0

# for x in range(v_ini, v_fim+1):
#     if (x != 1):
#         if (x % x == 0 and x % 1 == x):  
#             print(x, end=", ")
#             soma = soma + x
#         if (x % 5 != 0):
#             if (x == 2):
#                 soma = soma + x
#                 print(x, end=", ")
#             elif (x == 3):
#                 soma = soma + x
#                 print(x, end=", ") 
#             elif (x % 2 != 0 and x % 3 != 0):
#                 soma = soma + x
#                 print(x, end=", ")

# print("\n Somatória dos números primos = ", soma)
# print("Fim do programa")


###6 Escreva um programa que converta uma faixa de temperaturas de Celsius para
#Fahrenheit. O programa deve pedir ao usuário para digitar o valor inicial, o
#valor final e o incremento. Em seguida, deve imprimir cada valor em Celsius e
#sua conversão correspondente para Fahrenheit. Ex: 25, 35 e 5 à 25°C =
#77.0°F; 30°C = 86.0°F; 35°C = 95.0°F
# v_ini = int(input("Digite o início do intervalo: "))
# v_fim = int(input("Digite o fim do intervalo: "))
# v_incremento = int(input("Digite o valor do incremento: "))

# for x in range(v_ini, v_fim+1, v_incremento):
#     print(f"{x}°C = {x * 9/5 + 32}°F")