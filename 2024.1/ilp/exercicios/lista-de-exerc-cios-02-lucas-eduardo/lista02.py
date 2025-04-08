# 1. Crie um programa que leia o salário de uma pessoa e calcule o imposto de renda a
# ser pago baseado nas seguintes faixas: até R$ 1.903,98 isento, de R$ 1.903,99 até
# R$ 2.826,65 o imposto é de 7,5%, de R$ 2.826,66 até R$ 3.751,05 o imposto é de
# 15%, de R$ 3.751,06 até R$ 4.664,68 o imposto é de 22,5%, acima de R$ 4.664,68
# o imposto é de 27,5%.

# salario = float(input("Salário: "))
# ir_porcentagem = 0
# ir_valor = 0

# if(salario <= 1903.98):
#     ir_situacao = 0
#     ir_porcentagem = 0
#     ir_valor = 0

# elif(2826.65 > salario > 1903.98):
#     ir_situacao = 7.5
#     ir_porcentagem = 0.075
#     ir_valor = salario * ir_porcentagem

# elif(3751.05 > salario > 2826.66):
#     ir_situacao = 15
#     ir_porcentagem = 0.15
#     ir_valor = salario * ir_porcentagem

# elif(4664.68 > salario > 3751.06):
#     ir_situacao = 22.5
#     ir_porcentagem = 0.225
#     ir_valor = salario * ir_porcentagem

# else:
#     ir_situacao = 27.5
#     ir_porcentagem = 0.275
#     ir_valor = salario * ir_porcentagem

# print(f"{ir_situacao}% do seu salário, equivalente a R${ir_valor}, será convertido em imposto de renda.")


# 2. Escreva um programa que solicita o valor de um ano ao usuário, em seguida informa
# se o ano fornecido é ou não bissexto. [Dica: um ano é bissexto se é divisível por 4,
# mas não por 100. Para que um número X seja considerado divisível por um número
# Y é preciso que o resto da divisão de X por Y seja igual a ZERO].

# ano = int(input("Ano: "))

# if (ano % 4 == 0) and (ano % 100 != 0):
#     print(f"{ano} é um ano bissexto.")

# else:
#     print(f"{ano} não é um ano bissexto.")


# 3. Escreva um programa que solicite um número entre 1 e 10. Caso o usuário digite um
# valor dentro dessa faixa o programa deverá exibir a mensagem “O número digitado
# está DENTRO da faixa solicitada.”, senão o programa deverá exibir a mensagem “O
# número digitado está FORA da faixa solicitada.”.

# n = float(input("Um número de 1 a 10: "))
# if (1 > n > 10):
#     print(f"{n} não está na faixa solicitada.")
# else:
#     print(f"{n} está dentro da faixa solicitada.")


# 4. Escreva um programa que dado dois valores informe qual deles é o maior.

# n1 = float(input("Primeiro número: "))
# n2 = float(input("Segundo número: "))

# if n1 > n2:
#     print(f"{n1} é maior que {n2}")
# elif n1 == n2:
#     print(f"{n1} é igual a {n2}")
# else:
#     print(f"{n2} é maior que {n1}")


# 5. Escreva um programa que leia dois valores inteiros e escreva como saída a diferença
# entre o maior valor e o menor valor.

# n1 = int(input("Primeiro número: "))
# n2 = int(input("Segundo número: "))

# if n1 > n2:
#     print(f"A diferença entre {n1} e {n2} é de {n1-n2}.")
# elif n2 > n1:
#     print(f"A diferença entre {n2} e {n1} é de {n2-n1}.")


# 6. Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá exibir os 3 valores digitados pelo usuário em ordem crescente.

# v1 = int(input("Digite o primeiro valor inteiro: "))
# v2 = int(input("Digite o segundo valor inteiro: "))
# v3 = int(input("Digite o terceiro valor inteiro: "))

# if v1 > v2:
#     v1, v2 = v2, v1
# if v1 > v3:
#     v1, v3 = v3, v1
# if v2 > v3:
#     v2, v3 = v3, v2

# print(f"Em ordem crescente: {v1}, {v2}, {v3}.")


# 7. Escreva um programa que solicita ao usuário 3 valores inteiros. Em seguida o pro-
# grama deverá perguntar ao usuário se deseja ver os valores impressos em ordem
# crescente ou decrescente. Após a escolha, o programa deverá exibir os valores or-
# denados conforme indicação do usuário.

# v1 = int(input("Digite o primeiro valor inteiro: "))
# v2 = int(input("Digite o segundo valor inteiro: "))
# v3 = int(input("Digite o terceiro valor inteiro: "))
# escolha = int(input("(1) Ordenar em ordem crescente - (2) Ordenar em ordem descrescente: "))

# if (escolha == 1):
#     if v1 > v2:
#         v1, v2 = v2, v1
#     if v1 > v3:
#         v1, v3 = v3, v1
#     if v2 > v3:
#         v2, v3 = v3, v2
#     print(f"Em ordem crescente: {v1}, {v2}, {v3}.")
# elif (escolha == 2):
#     if v1 > v2:
#         v1, v2 = v2, v1
#     if v1 > v3:
#         v1, v3 = v3, v1
#     if v2 > v3:
#         v2, v3 = v3, v2
#     print(f"Em ordem decrescente: {v3}, {v2}, {v1}.")


# 8. Escreva um programa que leia três valores e determine se eles podem formar um
# triângulo. Caso possam, classifique o triângulo como equilátero, isósceles ou esca-
# leno.

# a = float(input("Digite o primeiro valor: "))
# b = float(input("Digite o segundo valor: "))
# c = float(input("Digite o terceiro valor: "))

# if (a+b>c) or (b+c>a) or (a+c>b):
#     if (a != b and b != c and a != c):
#         print("Triângulo escaleno.")
#     elif (a == b) and (b == c) and (c == a):
#         print("Triângulo equilátero.")
#     elif (a == b != c) or (b == c != a) or (c == a != b):
#         print("Triângulo isóceles")
#     else:
#         print("Triângulo sem definição")
# else:
#     print("Os valores não podem formar um triângulo.")