#Exercício de fixação 01
#Escreva um algoritmo que leia o valor de um número inteiro digitado pelo usuário e armazene esse vallor em uma variável;
#O algoritmo deve verificar se o valor digitado é um número positivo.
#Se o valor digitado for maior do que ZERO o programa deve escrever na tela “O número é positivo!”

n = int(input("Digite um número: "))
if (n > 0):
  print("O número é positivo!")


# Estruturas aninhadas
curso_tsi = input("Você faz TSI no IFRN? (s/n): ")
potiguar = input("Você é potiguar? (s/n): ")

if (curso_tsi == "s" and potiguar == "s"):
  print("Você faz TSI e é portiguar")

elif (curso_tsi == "s" and potiguar == "n"):
  print("Você faz TSI mas não é portiguar")

elif (curso_tsi == "n" and potiguar == "s"):
  print("Você não faz TSI mas é portiguar")

elif (curso_tsi == "n" and potiguar == "n"):
  print("Você nem faz TSI e nem é portiguar")

else:
  print("Você não é nada.")

#Exercício de Fixação 02
#Escreva um algoritmo que solicite ao usuário o valor de duas notas e armazene o resultado em duas variáveis diferentes (float);
#Calcule o resultado da média desses valores;
#Imprima “Você está em RECUPERAÇÃO!!!” caso o resultado da média seja maior ou igual a 30 e menor do que 70.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if (media >= 30 and media < 70):
  print("Você está em RECUPERAÇÃO!!!")