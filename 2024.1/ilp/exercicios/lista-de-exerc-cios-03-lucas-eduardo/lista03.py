# 1. Escreva um algoritmo que imprima na tela do usuário os números inteiros de 1 até 100
# (em ordem crescente).

# for x in range(1, 101):
#     print(x)


# 2. Escreva um algoritmo que imprima na tela do usuário os números inteiros de 1 até 100
# (em ordem decrescente).

# for x in range(100, 0, -1):
#     print(x)


# 3. Escreva um algoritmo que solicite ao usuário dois valores para determinação de um
# intervalo. Ao final o algoritmo deverá imprimir todos os números desse intervalo e o
# somatório deles.

# v1 = int(input("Início do intervalo: "))
# v2 = int(input("Fim do intervalo: "))

# soma = 0

# for x in range(v1, v2+1):
#     print(x, end=", ")
#     soma = soma + x

# print(f"somatória do intervalo = {soma}.")


# 4. Escreva um algoritmo que solicite do usuário 10 números e ao final imprima na tela o
# somatório desses números.

# print("Digite 10 valores!")
# soma = 0
# for x in range(1, 11):
#     n = int(input("N valor: "))
#     soma = soma + n

# print(f"Somátoria dos números é de {soma}.")


# 5. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores menores que 10.

# print("Digite 5 valores!")
# soma = 0
# for x in range (1, 6):
#     n = int(input("N valor: "))
#     if (n < 10):
#         soma = soma + n
# print(f"Somátoria dos números menores que dez é de {soma}.")


# 6. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores maiores ou igual a 10 e menor do que 20.

# print("Digite 5 valores!")
# soma = 0
# for x in range (1, 6):
#     n = int(input("N valor: "))
#     if (20 > n > 10):
#         soma = soma + n
# print(f"Somátoria dos números maiores que dez e menores qu vinte é de {soma}.")


# 7. Escreva um algoritmo que solicite do usuário 5 valores e afinal apresente na tela o
# somatório dos valores pares que foram digitados.

# print("Digite 5 valores!")
# soma = 0
# for x in range (1, 6):
#     n = int(input("N valor: "))
#     if (n % 2 == 0):
#         soma = soma + n
# print(f"Somátoria dos números pares é de {soma}.")


# 8. Escreva um algoritmo que solicite do usuário um número correspondente à quantidade
# de valores que o usuário fornecerá para o algoritmo. Ao final, o algoritmo deverá infor-
# mar quantos números pares foram digitados.

# n = int(input("Quantidade de valores: "))
# pares = 0

# for x in range(n):
#     valor = int(input("N valor: "))
#     if(valor % 2 == 0):
#         pares = pares + 1

# print(f"{pares} número pares foram digitados.")

# 9. Escreva um algoritmo que solicite do usuário 10 valores. O algoritmo deverá calcular
# a soma da sequência de valores pares e dos valores ímpares, ou seja, somar o 1o
# número digitado com o 3o, 5o, 7o e 9o e o mesmo para os números pares. Após, informar
# se o somatório dos números ímpares é maior, igual ou menor do que o dos números
# pares.

# par = 0
# soma_par = 0
# soma_impar = 0

# for x in range(10):
#     valor = int(input("N valor: "))
#     if par == 0:
#         soma_par = soma_par + valor
#         par = 1
#     else:
#         soma_impar = soma_impar + valor
#         par = 0

# if soma_impar > soma_par:
#     print(f"Somatória dos números ímpares ({soma_impar}) maior que a somátoria dos números pares ({soma_par})!")
# elif soma_impar < soma_par:
#     print(f"Somatória dos números pares ({soma_par}) maior que a somátoria dos números ímpares ({soma_impar})!")
# else:
#     print(f"Somatória dos números pares ({soma_par}) igual a somátoria dos números ímpares ({soma_impar})!")


# 10. Escreva um algoritmo que solicite do usuário 10 valores inteiros. O algoritmo deverá
# calcular o somatório dos números pares e dos números ímpares que forem digitados
# pelo usuário. Após o somatório, o algoritmo deve informar se o somatório dos números
# ímpares é maior, igual ou menor do que o dos números pares.

# soma_par = 0
# soma_impar = 0

# for x in range(10):
#     valor = int(input("N valor: "))
#     if (valor % 2 == 0):
#         soma_par = soma_par + valor
#     else:
#         soma_impar = soma_impar + valor

# if soma_impar > soma_par:
#     print(f"Somatória dos números ímpares ({soma_impar}) maior que a somátoria dos números pares ({soma_par})!")
# elif soma_impar < soma_par:
#     print(f"Somatória dos números pares ({soma_par}) maior que a somátoria dos números ímpares ({soma_impar})!")
# else:
#     print(f"Somatória dos números pares ({soma_par}) igual a somátoria dos números ímpares ({soma_impar})!")  


# 11. Escreva um algoritmo que informe ao usuário que calcula o somatório de uma sequên-
# cia de números. O algoritmo deverá solicitar ao usuário o total de números que deverão
# ser somados. Depois o algoritmo deve realizar a soma de todos os números e apre-
# sentar na tela o resultado dessa soma conforme exemplo abaixo:
# Digite o total de números a serem somados: 5
# 2 7 3 8 6 (números digitados pelo usuário)
# Saída no terminal: 2+7+3+8+6=26

# valores = int(input("Quantidade de valores: "))
# soma = 0
# saida = ""

# for x in range(valores):
#     n = float(input("N valor: "))
#     soma = soma + n

# for x in range(valores-1):
#     saida = saida + f"{n} + "

# saida = saida + f"{n}"
# print(f"{saida} = {soma}")


# 12. Escreva um algoritmo que imprima na tela todos os números divisíveis por 7 (separa-
# dos por “;”), mas que não sejam múltiplos de 5 no intervalo de 1000 a 3000.

# for x in range(1000, 3001):
#     if (x % 7 == 0):
#         if (x % 5 != 0):
#             print(x)


# 13. Escreva um algoritmo que imprima na tela a tabuada da multiplicação de um número
# inteiro de 1 a 10. Exemplo:
# Entrada: 9
# Saída: 1x9=9; 2x9=18; 3x9=27; 4x9=36; 5x9=45; 6x9=54; 7x9=63; 8x9=72;
# 9x9=81; 10x9=90;

# n = int(input("Número: "))

# for x in range(1, 11):
#     resultado = x * n
#     print(f"{x}x{n}={resultado}", end="; ")


# 14. Escreva um algoritmo que solicite ao usuário um número inteiro e depois imprima uma
# sequência de caracteres que represente um triângulo. Exemplo:
# Entrada: 3
# Saída:
# *
# * *
# * * *
# * *
# *

# n = int(input("Número inteiro: "))

# for x in range(1, n):
#      print('*' * x)

# for x in range(n, n-n, -1):
#      print('*' * x)

# 15. Escreva um algoritmo que solicite números ao usuário e conte quantos desses são
# pares e quantos são ímpares, até que seja digitado um número negativo. Ao final im-
# prima na tela quantos números pares e ímpares foram digitados.

# pares = 0
# impares = 0

# n = 0

# while n >= 0:
#     n = int(input("Número: "))
#     if (n < 0):
#         pass
#     elif (n % 2 == 0):
#         pares = pares + 1
#     else:
#         impares = impares + 1

# print(f"Números pares: {pares}\nNúmeros ímpares: {impares};")


# 16. Escreva um algoritmo que solicite ao usuário um valor e em seguida apresente na tela
# uma sequência começando em 1 e indo até o valor fornecido pelo usuário. Porém, se
# nessa sequência houver um número que seja múltiplo de 3 escreva PI, e se houver
# um número que seja múltiplo de 7 escreva PA. Caso haja um número que seja múltiplo
# de 3 e 7 escreva POW.

# valor = int(input("Valor: "))

# for x in range(1, valor+1):
#     if (x % 3 == 0) and (x % 7 == 0):
#         print("POW")
#     elif (x % 3 == 0):
#         print("PI")
#     elif (x % 7 == 0):
#         print("PA")
#     else:
#         print(x)