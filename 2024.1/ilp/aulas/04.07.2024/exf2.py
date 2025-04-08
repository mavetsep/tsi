programa = 1
soma = 0

print("Para encerrar o programa digite '0'. ")
while programa != 0:
    numero = int(input("Digite um número para adicionar à soma: "))
    programa = numero
    soma = soma + numero

print("O valor da soma é =", soma)
