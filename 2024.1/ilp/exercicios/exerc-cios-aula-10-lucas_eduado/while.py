###1 Escreva um programa que exiba os valores dos números de 1 até 100. Ao término o programa deverá exibir uma mensagem de encerramento informando que o programa terminou.

# n = 1
# while n != 101:
#     print(n)
#     n = n + 1


###2 Escreva um programa que solicita ao usuário valores numéricos e realiza a soma desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do
#somatório e encerrar o programa com uma mensagem de término do programa. O
#usuário deverá ser informado no início do programa o que o programa faz e qual a
#condição para encerramento do programa.

# programa = 1
# soma = 0

# print("Para encerrar o programa digite '0'. ")
# while programa != 0:
#     numero = int(input("Digite um número para adicionar à soma: "))
#     programa = numero
#     soma = soma + numero

# print("O valor da soma é =", soma)


###3 Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor
#com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor
#da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a
#senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar
#que o usuário acertou a senha.

# senha_bd = 21
# senha_u = 0

# while senha_u != 21:
#     senha_u = int(input("Digite a senha: "))

# print("Senha correta. Programa encerrado.")


###4 Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
#para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
# usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
#necessários e informar que o programa encerrou.

# from random import randint

# numero = randint(1, 100)
# palpite = 0
# vezes = 0

# while palpite != numero:
#     palpite = int(input("Aposta: "))
#     vezes = vezes + 1

# print("Você precisou de",vezes,"tentativas para acertar meu número!")


###5 Escreva um programa que solicita ao usuário um valore numérico inteiro positivo e, em
#seguida, calcule o fatorial desse número usando um loop do tipo while. Ao final o
#programa deverá exibir o valor do fatorial do número informado pelo usuário e término
#do programa.
# numero = int(input("Digite um número: "))
# fatorial = 1
# contador = 1

# while contador <= numero:
#     fatorial *= contador
#     contador += 1

# print(fatorial)

###6 Escreva um programa que peça ao usuário para digitar um número “n” inteiro positivo
#e, em seguida, imprima os “n” primeiros termos da sequência de Fibonacci. A
#sequência de Fibonacci é dada pela somatório de dois números que resulta no seu
#sucessor. Ex: 0, 1, 1, 2, 3, 5, 8... Esses são os 7 primeiros números da sequência.
#Exiba os números na tela e informa o término do programa ao final.

###7 Escreva um algoritmo que solicite ao usuário um número entre 1 e 10.000 e
#depois informe ao usuário se o número digitado é primo ou não. Um número é
#dito ser primo quando ele é divisível apenas por 1 e ele mesmo. Ao término,
#informe que o programa foi encerrado.

# n = int(input("Digite um número de 1 até 10.0000: "))
# if (n == 3) or (n == 2):
#     print("É primo.")
# elif (n < 2):
#     print("Não é primo")
# elif (n % 2 == 0) or (n % 3 == 0):
#     print("Não é primo")
# else:
#     print("É primo")

###8 Escreva um programa que peça ao usuário para digitar um número inteiro e,
#em seguida, calcule a soma dos dígitos desse número usando um loop while.
#Ao término, informe que o programa foi encerrado.

# num = int(input("Digite um número inteiro: "))
# somadigitos = 0

# while (num > 0):
#     resto = num % 10
#     num = (num - resto)/10
#     somadigitos = int(somadigitos + resto)

# print("A soma dos números é =", somadigitos)

###9 Escreva um programa que peça ao usuário para digitar um número inteiro e,
#em seguida, calcule a soma dos dígitos desse número usando um loop while.
#Ao término, informe que o programa foi encerrado.

# soma = 0
# numero = 1

# n = int(input("Digite um número: "))

# while numero <= n:
#     soma = soma + 1 / numero
#     numero = numero + 1

# print("A soma da séria harmônica é =", soma, "\nFim do programa.")