# Tuplas

# nomes = ("Lucas", "Maria")
# print(nomes[1])

# tuplas = (1, 2, 3)
# a,b,c = tuplas # desempacotamento simples
# print(a)
# print(b)
# print(c)

# Dicionários

# meu_dicionario1 = {1: "casa", 7: "comida", 3: 3.14}
# print(meu_dicionario1[1]) # imprime casa

# meu_dicionario1[3] = "novo valor" # altera o valor 3.14 do item de chave 3 para “novo valor”
# print(meu_dicionario1[3]) # imprime novo valor

# meu_dicionario1["casa"] = "bonita" # adiciona novo item ao dicionário
# print(meu_dicionario1) # imprime {1: 'casa', 7: 'comida', 3: 'novo valor', 'casa': 'bonita’}

# del meu_dicionario1["casa"] # remove o item do dicionário cuja chave é “casa”
# print(meu_dicionario1) # imprime {1: 'casa', 7: 'comida', 3: 'novo valor'}

# Criando o dicionário de registros de alunos
# alunos = {
# 101 : {"nome": "Maria", "idade": 20, "curso": "TSI"},
# 102 : {"nome": "Pedro", "idade": 18, "curso": "Mecatrônica"},
# 103 : {"nome": "Ana", "idade": 19, "curso": "Informática"}
# }

# # Acessando informações de um aluno específico pelo ID
# id_aluno = 102
# print(f"Informações do aluno ID {id_aluno}:") # Informações do aluno ID 102
# print(f"Nome: {alunos[id_aluno]['nome']}") # Nome: Pedro
# print(f"Idade: {alunos[id_aluno]['idade']}") # Idade: 18
# print(f"Curso: {alunos[id_aluno]['curso']}") # Curso: Mecatrônica

# Conjuntos

meu_conjunto = {(1,2,3), "coisa", 12}
meu_conjunto.add("novo valor")
print(meu_conjunto)