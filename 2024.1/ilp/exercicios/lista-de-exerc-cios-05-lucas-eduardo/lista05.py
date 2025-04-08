# 1. Criação e acesso: Escreva um programa que crie uma tupla que seja criada contendo
# os dados nome, idade e estado. Como saída, o programa deve imprimir cada um
# desses valores separadamente.

# nome = input("Nome: ")
# idade = int(input("Idade: "))
# uf = input("UF: ")

# tupla_dados = (nome, idade, uf)
# print(f"\n- Dados - \nNome: {tupla_dados[0]}\nIdade: {tupla_dados[1]}\nUF: {tupla_dados[2]}\n")

# 2. Desempacotamento: Escreva um programa que realiza o cálculo da distância entre
# dois pontos no plano cartesiano. O programa deve receber como entrada 4 valores
# inteiros para os dois pontos. Em seguida, calcular a distância entre os dois pontos e
# exibir o valor da distância ao usuário.

# import math

# ponto1 = (float(input("Posição no eixo X do primeiro ponto: ")), float(input("Posição no eixo Y do primeiro ponto: ")))
# ponto2 = (float(input("Posição no eixo X do segundo ponto: ")), float(input("Posição no eixo Y do segundo ponto: ")))

# x1, y1 = ponto1 # Atribui x1 e y1 aos valores em ordem da tupla ponto1
# x2, y2 = ponto2 # Atribui x2 e y2 aos valores em ordem da tupla ponto2

# distancia_ponto1_ponto2 = round(math.sqrt(((x2-x1)**2) + (y2-y1)**2), 3)

# print(f"Distância = {distancia_ponto1_ponto2}")

# 3. Concatenação de tuplas: Escreva um programa que cria duas tuplas: uma para frutas
# e outra para vegetais. O programa deve imprimir no terminal o resultado de uma única
# tupla formada pela concatenação das duas tuplas anteriormente fornecidas pelo
# usuário.

# tamanho_tupla_frutas = int(input("Quantidade de frutas: "))
# tamanho_tupla_vegetais = int(input("Quantidade de vegetais: "))
# lista_frutas = []
# lista_vegetais = []

# for x in range(tamanho_tupla_frutas):
#     fruta = input(f"{x+1}º fruta: ")
#     lista_frutas += [fruta]

# for x in range(tamanho_tupla_vegetais):
#     vegetal = input(f"{x+1}º vegetal: ")
#     lista_vegetais += [vegetal]

# tupla_frutas = tuple(lista_frutas)
# tupla_vegetais = tuple(lista_vegetais)

# tupla_frutas_e_vegetais = tupla_frutas + tupla_vegetais

# print(f"Alimentos: \n{tupla_frutas_e_vegetais}")

# 4. Conversão de Lista para Tupla: Escreva um programa que dada uma lista de números,
# converta essa lista em uma tupla e, em seguida, utilize slices para criar uma nova tupla
# que contenha apenas os três primeiros elementos da tupla original. Imprima o
# resultado da lista original e as duas tuplas criadas.

# lista_numeros = []

# numeros = input("Sequência de números separados por espaço: ")

# for x in numeros:
#     if x != " ":
#         lista_numeros += [int(x)]

# tupla_numeros = tuple(lista_numeros)
# tupla_tres_primeiros_numeros = tuple(tupla_numeros[0:3])

# print(f"Tupla: {tupla_numeros}\nSlice da tupla: {tupla_tres_primeiros_numeros}")

# 5. Troca de posições em tuplas: Escreva um programa que, dada uma tupla e dois valores
# inteiros correspondentes às posições nessa tupla, troque os elementos conforme as
# posições fornecidas. Lembre-se de que tuplas são imutáveis, portanto, você precisará
# converter a tupla para uma lista, fazer a troca e depois converter de volta para uma
# tupla. Imprima o resultado da tupla inicial e com as posições permutadas.

# lista_numeros = []

# numeros = input("Sequência de números separados por espaço: ")

# for x in numeros:
#     if x != " ":
#         lista_numeros += [int(x)]

# tupla_inicial = tuple(lista_numeros)

# posicao1 = int(input("Primeira posição para troca: "))
# posicao2 = int(input("Segunda posição para troca: "))

# lista_numeros[posicao1], lista_numeros[posicao2] = lista_numeros[posicao2], lista_numeros[posicao1]

# tupla_final = tuple(lista_numeros)

# print(f"Tupla A: {tupla_inicial}\nTupla B: {tupla_final}")

# Conjuntos:

# 6. Criação de conjuntos a partir de listas: Escreva um programa que, dada uma lista
# números fornecida pelo usuário, converta a lista em um conjunto para eliminar
# duplicatas. Em seguida, adicione um número extra que seja o dobro do maior valor do
# conjunto e adicione ao conjunto resultante. Imprima a lista inicial e o conjunto final.

# elementos_lista = input(f"Elementos da lista separados por espaço: ")
# elemento = ""
# lista_numeros = []
# maior_valor = 0

# for x in elementos_lista:
#     if x != " ":
#         lista_numeros += [int(x)]

# for valor in lista_numeros:
#     if valor > maior_valor:
#         maior_valor = valor

# print(maior_valor)

# lista_numeros += [int(maior_valor*2)]

# lista_numeros = set(lista_numeros)

# print(f"Conj: {lista_numeros}")

# 7. União e diferença: Escreva um programa que solicite ao usuário 3 conjuntos (A, B e
# C) de números inteiros e em seguida realize as seguintes operações sobre conjuntos:
# união: (A È B); e diferença: (A È B) - C. O programa deverá exibir como saída o
# resultado da união e diferença entre os conjuntos (use as funções embutidas union()
# e difference()).

# elementos_lista_a = input(f"Elementos da lista A separados por vírgula: ")
# elementos_lista_b = input(f"Elementos da lista B separados por vírgula: ")
# elementos_lista_c = input(f"Elementos da lista C separados por vírgula: ")
# lista_A = []
# lista_B = []
# lista_C = []

# for x in elementos_lista_a:
#     if x != ",":
#         lista_A += [int(x)]

# for x in elementos_lista_b:
#     if x != ",":
#         lista_B += [int(x)]

# for x in elementos_lista_c:
#     if x != ",":
#         lista_C += [int(x)]

# conjunto_A = set(lista_A)
# conjunto_B = set(lista_B)
# conjunto_C = set(lista_C)

# uniao_A_B = conjunto_A.union(conjunto_B)
# diferenca_uniao_A_B_e_C = uniao_A_B.difference(conjunto_C)

# print(f"União: {uniao_A_B}")
# print(f"Diferença: {diferenca_uniao_A_B_e_C}")

# 8. Remoção Condicional em Conjuntos: Escreva um programa que receba como entrada
# uma sequência de valores inteiros e cria um conjunto a partir desses valores. Além
# disso, o programa também recebe um valor numérico base para atuar como um divisor.
# Crie um novo conjunto, a partir dos valores inicialmente fornecidos, formado pelos
# números divisíveis pelo divisor digitado pelo usuário. Exiba na tela os dois conjuntos e
# o divisor.

# valores = input("Valores inteiros separados por espaço: ")
# divisor = int(input("Divisor: "))
# lista_valores = []
# lista_valores_inteiros = []
# lista_valores_divisiveis = []
# valor_atual = ""

# for valor in valores:
#     if valor == " ":
#         lista_valores.append(valor_atual)
#         valor_atual = ""
#     else:
#         valor_atual += valor
    
# if valor_atual: # Adiciona o úlimo valor
#     lista_valores.append(valor_atual)

# for valor in lista_valores: # Converte os elementos da lista em inteiros
#     lista_valores_inteiros.append(int(valor))

# for valor in lista_valores_inteiros:
#     if valor % divisor == 0:
#         lista_valores_divisiveis.append(valor)

# conjunto1 = set(lista_valores_inteiros)
# conjunto2 = set(lista_valores_divisiveis)

# print(f"Conj 1: {conjunto1}")
# print(f"Conj 2: {conjunto2}")

# 9. Operações em Conjuntos: Escreva um programa que, dados dois conjuntos A e B de
# valores fornecidos pelo usuário, verifique se B é um subconjunto de A. Em seguida crie
# um conjunto C com valores do conjunto A, mas sem os valores do conjunto B. Ao final,
# exiba os valores de ambos os conjuntos. 

# 10. Presença de valores em Conjuntos: Escreva um programa que solicite ao usuário uma
# relação de valores e adicione-os a um conjunto (utilize o operador | para isso). Em
# seguida, crie uma lista com outros valores e verifique quais desses valores estão
# presentes no conjunto. A quantidade de valores a serem fornecidos para o conjunto e
# para a lista é indeterminada e deve ser interrompida quando o usuário digitar o valor
# ‘$$’ para indicar o término de cada uma das coleções. Ao final o programa deverá exibir
# o conjunto e a relação de valores da lista informando se os mesmos estão presentes
# no conjunto.

# valores_conjunto = []
# valores_lista = []
# valor_conjunto = ""
# valor_lista = ""

# while valor_conjunto != "$$":
#     valor_conjunto = input("Adicionar ao conjunto o valor ($$ para finalizar): ")
#     if valor_conjunto != "$$":
#         valores_conjunto += [int(valor_conjunto)]

# while valor_lista != "$$":
#     valor_lista = input("Adicionar a lista o valor ($$ para finalizar): ")
#     if valor_lista != "$$":
#         valores_lista += [int(valor_lista)]

# valores_conjunto = set(valores_conjunto)

# print(f"Conjunto: {valores_conjunto}")
# for valor in valores_lista:
#     if valor in valores_conjunto:
#         print(f"{valor}:Sim", end=", ")
#     else:

# Dicionários:

# 11. Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
# cada palavra no texto repassado como entrada para o programa, sem fazer distinção
# entre letras maiúsculas ou minúsculas. Os sinais de pontuação não devem ser
# contabilizados, como por exemplo “.” Ou “,”. Crie um dicionário que armazene a
# contagem de cada palavra no texto. A chave do dicionário deve ser a palavra e o valor
# deve ser o número de vezes que a palavra aparece no texto. Imprima o dicionário
# resultante. 

# string = input("Palavras separadas por espaço: ")

# lista_palavras = string.split(" ")
# lista_palavras_tratadas = []
# dicionario_palavras = {}

# for palavra in lista_palavras:
#     if ("," in palavra) or ("." in palavra):
#         palavra = palavra.lower()
#         lista_palavras_tratadas += [palavra[:-1]]
#     else:
#         palavra = palavra.lower()
#         lista_palavras_tratadas += [palavra]

# for palavra in lista_palavras_tratadas:
#     if palavra not in dicionario_palavras:
#         dicionario_palavras[palavra] = 1
#     else:
#         dicionario_palavras[palavra] += 1

# #Lorem ipsum dolor sit amet. Lorem opsum dolor amet, dolor comem.

# print(f"Contagem de palavras: {dicionario_palavras}")

# 12. Escreva um programa que receba como entrada uma relação de tuplas formadas por
# nomes de frutas e valores. O programa deverá realizar o agrupamento da relação de
# tuplas pelo nome das tuplas e somar dos valores para criação de um dicionário onde
# o nome da fruta deve ser a chave e o resultado da soma o valor. Ao final, exiba a lista
# de valores inicialmente fornecida e o dicionário criado. 

# string = 1
# lista_frutas_valores = []
# dicionario_frutas_valores = {}

# while string != "0":
#     string = input("Fruta e quantidade separados por espaço: ('0' para finalizar): ")
#     if string != "0":
#         tupla_fruta_valor = tuple(string.split(" "))
#         lista_frutas_valores += tupla_fruta_valor
#         if tupla_fruta_valor[0] not in dicionario_frutas_valores.keys():
#             dicionario_frutas_valores[tupla_fruta_valor[0]] = int(tupla_fruta_valor[1])
#         else:
#             dicionario_frutas_valores[tupla_fruta_valor[0]] += int(tupla_fruta_valor[1])

# print(f"Lista: {lista_frutas_valores}\nValores: {dicionario_frutas_valores}")

# 13. Escreva um programa que dado um dicionário aluno_nota, onde as chaves
# representam nomes de alunos e os valores representam suas respectivas notas, cujos
# valores sejam fornecidos pelo usuário. Crie um novo dicionário que inverta as chaves
# e os valores do dicionário aluno_nota, ou seja, as notas serão as chaves e os nomes
# dos alunos serão os valores. Considere que duas ou mais pessoas podem ter a mesma
# nota, e neste caso, o valor deve ser uma lista com os nomes dos alunos. Imprima o
# dicionário resultante. 

# 14. Escreva um programa que dado dois dicionários que representam valores de estoque
# de itens em duas lojas, cujos valores sejam fornecidos pelo usuário. Crie um novo
# dicionário para representar o estoque total que combine esses dois primeiros
# dicionários, somando as quantidades dos itens que aparecem em ambas as lojas. Para
# itens que aparecem apenas em uma loja, mantenha a quantidade original. Imprima o
# dicionário de cada loja e o dicionário resultante.

# 15. Escreva um programa que realiza o cálculo das vendas de uma lista de vendedores
# ao longo de um trimestre. O programa deve solicitar a relação de nomes dos
# vendedores e em seguida criar um dicionário em que o nome do vendedor é a chave
# e o valor deve ser o total das vendas desse vendedor. Faça com que o programa
# solicite para cada vendedor o quantitativo de vendas ao longo de cada mês no
# trimestre. Em seguida, calcule a soma das vendas de cada vendedor e crie uma lista
# de tuplas contendo o nome o valor total das vendas de cada vendedor ordenada pelo
# valor das vendas em ordem decrescente. Exiba ao final o dicionário do relatório de
# vendas e a lista ordenada de tuplas.