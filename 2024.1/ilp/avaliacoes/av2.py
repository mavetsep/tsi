# 1 – (20 pts) Você foi contratado para desenvolver um sistema que calcula descontos para um supermercado.
# As regras de desconto são as seguintes:
# • Se o cliente tiver um cartão fidelidade e a compra for acima de R$ 500, aplicar um desconto de 10%.
# • Se o cliente não tiver um cartão fidelidade, mas a compra for acima de R$ 1000, aplicar um desconto
# de 5%.
# Escreva um programa que leia o valor da compra e se o cliente possui ou não um cartão fidelidade, e então
# calcule e mostre o valor final da compra após aplicar os descontos apropriados. Utilize alguma das estruturas
# condicionais estudadas para solucionar o problema.

# valor = float(input("Valor da compra em R$ "))
# fidelidade = input("Possui cartão fidelidade (n/s): ")

# if (valor > 500 and fidelidade == "s"):
#     desconto = valor * 0.1
#     valor = valor - desconto
#     print(f"Valor final da compra é de R$ {valor}")

# elif (fidelidade == "n" and valor > 1000):
#     desconto = valor * 0.05
#     valor = valor - desconto
#     print(f"Valor final da compra é de R$ {valor}")

# else:
#     print(f"Valor final da compra é de R$ {valor}")


# 2 – (20 pts) Crie um programa para verificar a presença, ou ausência, de 100 valores fornecidos pelo usuário
# em um dado intervalo. Neste sentido o seu programa deverá realizar as seguintes ações:
# 1) Solicitar ao usuário dois valores inteiros e diferentes que determinarão o intervalo;
# 2) Solicitar ao usuário que sejam fornecidos 100 valores e verificar se esses valores estão contidos no
# intervalo;
# 3) Contabilizar os valores digitados pelo usuário que estejam contidos dentro do intervalo;
# 4) Exibir o maior valor digitado pelo usuário (pertencente ao intervalo) e o total de valores digitados pelo
# usuário que estão contidos dentro do intervalo.

# v1 = int(input("Primeiro valor: "))
# v2 = int(input("Segundo valor: "))
# contidos = 0
# maior = 0

# for x in range(0, 99):
#     valor = int(input("Valor para o intervalo: "))
#     for x in range(v1, v2+1):
#         if valor == x:
#             contidos = contidos + 1
#             if valor > maior:
#                 maior = valor

# print(f"Maior valor digitado (pertencente ao invervalo): {maior};\nValores digitados dentro no intervalo: {contidos}.")


# 3 – (20 pts) O Jogo do par ou ímpar. Crie um programa que simula um campeonato de par ou ímpar. O
# programa, ao ser iniciado, deve solicitar a quantidade de jogadores que irão disputar as partidas de par
# ou ímpar e distribuir esses jogadores em grupos, sempre com três jogadores, preferencialmente, e no
# mínimo 2. Divisão dos grupos: o campeonato deve ter no mínimo 2 e no máximo 9 jogadores. Caso o
# campeonato tenha de 2 a 3 jogadores, então deverá existir apenas um grupo e o campeão do grupo será
# o vencedor do campeonato. Caso o jogo tenha 4 jogadores, deverão ser criados dois grupos com dois
# jogadores; caso tenha 5 jogadores, deverá ser criado um grupo com 3 e outro com 2; caso tenha 6
# jogadores, deverão ser criados dois grupos com 3 jogadores e assim por diante. O campeonato deve ter
# no máximo 3 grupos e envolve duas fases: uma classificatória e a decisão final com aqueles que se
# classificaram par a fase final. A fase classificatória, cada jogador de um grupo jogará uma vez contra os
# rivais desse mesmo grupo. Cada partida será disputada em um formato “melhor de 3”, ou seja, quem
# vencer duas rodas primeiro vence a partida. Se houver empate, esses dois jogadores deverão disputar
# uma partida entre si para decidir quem será o campeão do grupo. O caminho para a fase final se dará da
# seguinte forma: se o campeonato tiver apenas um grupo, o campeão do grupo será o campeão do
# campeonato. Se o campeonato tiver 2 ou 3 grupos, os campeões de cada grupo formarão um novo grupo
# e se enfrentam na fase final nos mesmos moldes do que ocorreu na fase classificatória. O programa
# deverá solicitar ao usuário que seja informado a quantidade de participantes do campeonato e, em
# seguida, realizar automaticamente a divisão desses jogadores nos grupos. O programa também deverá
# simular o campeonato e apresentar os resultados das disputas em cada grupo de forma detalhada, bem
# como quem foi o vencedor em cada grupo. Posteriormente, fazer o mesmo e apresentar os resultados
# das disputas na fase final, caso haja mais de um jogador na fase final. Por fim, informar quem foi o
# vencedor do campeonato. Utilize a função randint() do pacote random do Python variando entre os
# valores 1 e 2 para cada jogada de cada jogador ao longo das disputas que forem simuladas pelo programa.