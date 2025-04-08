# Tuplas:

# 1. Escreva um programa que receba uma tupla de números inteiros e como
# saída uma nova tupla com os elementos pares da tupla original. Por
# exemplo, se a tupla for (1, 2, 3, 4, 5), o programa deve imprimir (2, 4).

# tupla_inteiros = (1, 2, 3, 4, 5)
# tupla_pares = ()
# lista_pares = []

# for x in tupla_inteiros:
#     if x % 2 == 0:
#         lista_pares += [x]

# tupla_pares = tuple(lista_pares)
# print(tupla_pares)

# 2. Escreva um programa que receba uma tupla de strings e exiba uma nova
# tupla com as strings ordenadas alfabeticamente e sem repetições. Por
# exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), o
# programa deve imprimir ("banana", "laranja", "maçã", "uva").

# tupla_strings = ("banana", "maçã", "laranja", "banana", "uva")
# lista_ordenada = sorted(tupla_strings)
# conjunto_sem_repeticoes = set(lista_ordenada)
# tupla_sem_repeticoes = tuple(conjunto_sem_repeticoes)
# print(tupla_sem_repeticoes)

# Dicionários:

# 3. Escreva um programa que receba um dicionário que mapeia nomes de
# países para suas populações e exiba o nome do país com a maior
# população. Por exemplo, se o dicionário for {"Brasil": 211.8, "China":
# 1400.5, "Índia": 1366.4}, o programa deve exibir "China".

# paises_populacoes = {"Brasil": 211.8, "China": 1400.5, "Índia": 1366.4}

# maior_populacao = max(paises_populacoes, key=paises_populacoes.get)

# print(maior_populacao)

# 4. Escreva um programa que receba como entrada um dicionário que mapeia
# nomes de alunos para suas notas e exiba um novo dicionário com os nomes
# dos alunos aprovados e suas respectivas médias. Considere que um aluno é
# aprovado se sua média for maior ou igual a 7. Por exemplo, se o dicionário
# for {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]},
# o programa deve exibir {"Ana": 8.33, "Carla": 8.0}.

quantidade_alunos = int(input("Quantidade de alunos: "))
lista_nomes = []
lista_notas = []

for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do aluno(a) {i+1}: ")
    lista_nomes += [nome]
    for j in range(3):
        nota = int(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        lista_notas += [nota]

notas_alunos = {}
tamanho = len(lista_nomes)
razao = 3
for i in range(tamanho):
    notas_alunos[lista_nomes[i]] = lista_notas[i*razao:(i+1)*razao]

# Calcular médias
lista_medias = []
for i in range(quantidade_alunos):
    soma = 0
    for nota in notas_alunos[lista_nomes[i]]:
        soma += nota
    lista_medias += [soma/3]

# Alunos aprovados
aprovados = {}
for i in range(len(lista_medias)):
    if lista_medias[i] > 7:
        aprovados[lista_nomes[i]] = lista_medias[i]

# Saída do programa
print(aprovados)

# Conjuntos:

# 5. Escreva um programa que receba dois conjuntos de números inteiros como
# entrada e exiba um novo conjunto com os elementos que estão em ambos
# os conjuntos. Por exemplo, se os conjuntos forem {1, 2, 3, 4} e {3, 4, 5, 6},
# o programa deve exibir {3, 4}.

# conjunto1 = {1, 2, 3, 4}
# conjunto2 = {3, 4, 5, 6}
# conjunto3 = set()

# for x in conjunto1:
#     if x in conjunto2:
#         conjunto3.add(x)

# print(conjunto3)

# 6. Escreva um programa que receba um conjunto de strings e exiba um novo
# conjunto com as strings que são palíndromos. Um palíndromo é uma palavra
# que é igual a ela mesma quando lida de trás para frente. Por exemplo, se o
# conjunto for {"arara", "casa", "ovo", "radar"}, o programa deve exibir
# {"arara", "ovo", "radar"}.

# conjunto1 = {"arara", "casa", "ovo", "radar"}
# conjunto2 = set()

# for x in conjunto1:
#     string = x
#     string_inversa = string[::-1]
#     if string == string_inversa:
#         conjunto2.add(x)

# print(conjunto2)