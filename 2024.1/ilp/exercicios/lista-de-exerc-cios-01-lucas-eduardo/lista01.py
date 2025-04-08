# 1. Calculadora Simples: Solicite ao usuário para inserir dois valores numéricos,
# realize as operações de soma, subtração, multiplicação e divisão, e ao final exiba
# os valores de cada uma das operações.

# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))

# soma = n1 + n2
# sub = n1 - n2
# mult = n1 * n2
# div = n1 / n2

# print(f"\nSoma = {soma}\nSubtração = {sub}\nMultiplicação = {mult}\nDivisão = {div}")


# 2. Conversor de Temperatura: Solicite ao usuário um valor de temperatura em graus
# Celsius, converta-a para Fahrenheit e exiba o resultado da conversão.

# celsius = float(input("Digite a temperatura em graus celsius: "))
# fahr = (celsius * 9/5) + 32

# print(f"A temperatura em fahrenheit é de {fahr}°")


# 3. Área do Círculo: Solicite ao usuário um valor do raio de um círculo, calcule sua
# área e exiba o resultado do cálculo.

# raio = float(input("Digite o valor de um raio: "))
# area = 3.14*(raio**2)

# print(f"O valor da área do círculo é de {area}")


# 4. Área do Triângulo: Solicite ao usuário um valor da base e da altura de um
# triângulo, calcule sua área e exiba o resultado do cálculo.

# base = float(input("Digite o valor da base: "))
# altura = float(input("Digite o valor da altura: "))

# area = (base*altura)/2

# print(f"O valor da área de triângulo é de {area}")


# 5. Volume da Esfera: Solicite ao usuário um valor do raio de uma esfera, calcule seu
# volume e exiba o resultado do cálculo.

# raio = float(input("Digite um valor para o raio: "))
# volume = (4*3.14*(raio**3))/3

# print(f"O valor do volume da esfera é de {volume:.2f}")


# 6. Calculadora de Média Aritmética: Solicite ao usuário para que ele insira três
# valores de notas, realize o cálculo da média aritmética e em seguida exiba os três
# valores digitados pelo usuário e o resultado do cálculo.

# n1 = float(input("Digite o valor da primeira nota: "))
# n2 = float(input("Digite o valor da segunda nota: "))
# n3 = float(input("Digite o valor da terceira nota: "))

# ma = (n1+n2+n3)/3

# print(f"Média aritimética = {ma:.2f} \n As notas foram: {n1}, {n2}, {n3}")


# 7. Calculadora de Média Ponderada: Solicite ao usuário para que ele insira os
# valores de 4 notas e seus respectivos pesos, em seguida realize o cálculo da média
# pondera e exiba o resultado do cálculo.

# n1 = float(input("Primeira nota: "))
# p1 = int(input("Peso da primeira nota: "))
# n2 = float(input("Segunda nota: "))
# p2 = int(input("Peso da segunda nota: "))
# n3 = float(input("Terceira nota: "))
# p3 = int(input("Peso da terceira nota: "))
# n4 = float(input("Quarta nota: "))
# p4 = int(input("Peso da quarta nota: "))

# cima = (n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)
# baixo = p1+p2+p3+p4

# mp = cima/baixo

# print(f"A média ponderada é de {mp:.1f}")


# 8. Equação de Segundo Grau: Solicite ao usuário os valores de “a”, “b”, “c” e “x”, em
# seguida resolva uma equação quadrática do tipo y = ax2 + bx + c e exiba o valor
# de y para o usuário.

# a = float(input("Valor de a: "))
# b = float(input("Valor de b: "))
# c = float(input("Valor de c: "))
# x = float(input("Valor de x: "))

# y = a*(x**2) + b*x + c

# print(f"Valor de Y é de: {y}")


# 9. Calculadora de IMC: Solicite ao usuário os valores de peso (kg) e altura (m),
# calcule o índice de massa corporal (IMC), sabendo que IMC = peso/altura², em seguida
# exiba o valor do IMC calculado.

# peso = float(input("Peso: "))
# altura = float(input("Altura: "))

# imc = peso/(altura**2)

# print(f"Valor do IMC é de: {imc:.1f}")


# 10.Tabuada: Solicite ao usuário um valor numérico, em seguida, exiba a tabuada de
# um número específico (por exemplo, 5). O programa deverá ter como saída:
# 5x1 = 5; 5x2 = 10; 5x3 = 15; 5x4 = 20; 5x5 = 25; 5x6 = 30; 5x7 = 35; 5x8 = 40; 5x9
# = 45; 5x10 = 50;

# n = int(input("Número: "))
# print(f"Tabuada do {n}:\n{n}*1 = {n*1}\n{n}*2 = {n*2}\n{n}*3 = {n*3}\n{n}*4 = {n*4}\n{n}*5 = {n*5}\n{n}*6 = {n*6}\n{n}*7 = {n*7}\n{n}*8 = {n*8}\n{n}*9 = {n*9}\n{n}*10 = {n*10}")


# 11.Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO: Solicite
# ao usuário um valor numérico correspondente à quantidade de segundos, em
# seguida converta o valor para o formato de HORA:MINUTO:SEGUNDO.

# segundos = int(input("Segundos: "))
# hh = segundos // 3600
# mm = (segundos % 3600) // 60
# ss = segundos % 60

# print(f"{hh}:{mm}:{ss}")