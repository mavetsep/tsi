import matplotlib.pyplot as plt
import numpy as np

# pip install matplotlib
# pip install numpy




# dados coletados dos tempos de execucao dos algoritmos
# // 10 elementos:
# // Tempo com Stooge: 0.11510 ms
# // Tempo com Bubble Sort: 0.12270 ms
# // Tempo com Selection Sort: 0.06290 ms
# // Tempo com Insertion Sort: 0.04060 ms
# // Tempo com Gnome Sort: 0.11130 ms

# // 100 elementos:
# // Tempo com Stooge: 3.45340 ms
# // Tempo com Bubble Sort: 0.73640 ms
# // Tempo com Selection Sort: 0.31020 ms
# // Tempo com Insertion Sort: 0.10480 ms
# // Tempo com Gnome Sort: 0.38860 ms

# // 1000 elementos
# // Tempo com Stooge: 424.47400 ms
# // Tempo com Bubble Sort: 5.86230 ms
# // Tempo com Selection Sort: 4.07340 ms
# // Tempo com Insertion Sort: 2.00270 ms
# // Tempo com Gnome Sort: 6.73790 ms

# // 10000 elementos:
# // Tempo com Stooge: 332078.96780 ms
# // Tempo com Bubble Sort: 239.58370 ms
# // Tempo com Selection Sort: 82.01780 ms
# // Tempo com Insertion Sort: 45.09520 ms
# // Tempo com Gnome Sort: 119.81500 ms


# 1. estruturar os dados coletados
# eixo X: numero de elementos
n_elementos = [10, 100, 1000, 10000]

# eixo Y: tempos de execução em milissegundos (ms) 
tempos = {
    'Stooge Sort': [0.11510, 3.45340, 424.47400, 332078.96780],
    'Bubble Sort': [0.12270, 0.73640, 5.86230, 239.58370],
    'Selection Sort': [0.06290, 0.31020, 4.07340, 82.01780],
    'Insertion Sort': [0.04060, 0.10480, 2.00270, 45.09520],
    'Gnome Sort': [0.11130, 0.38860, 6.73790, 119.81500]  # <-- gnomeSort adicionado 
}

# cores para os algoritmos 
cores = {
    'Stooge Sort': 'red',
    'Bubble Sort': 'orange',
    'Selection Sort': 'blue',
    'Insertion Sort': 'green',
    'Gnome Sort': 'purple'  # <-- cor do gnomeSort 
}


# 2. config e criacao do grafico
# plt.subplots() mais controle sobre a figura
fig, ax = plt.subplots(figsize=(12, 10)) # aumentar a figura para caber a nova legenda

# 3. plotar os dados de cada algoritmo
for algoritmo, tempos_execucao in tempos.items():
    ax.plot(
        n_elementos, 
        tempos_execucao, 
        label=algoritmo,
        marker='o', # adiciona um ponto em cada medição
        linestyle='-', # linha conectando os pontos
        color=cores[algoritmo]
    )

# 4. configurar as escalas para logaritmica
# essencial para visualizar dados com grandes variações
ax.set_xscale('log')
ax.set_yscale('log')

# 5. adicionar os titulos, legendas e grade para melhorar a visualização
ax.set_title('Comparação de Desempenho de Algoritmos de Ordenação', fontsize=16)
ax.set_xlabel('Número de Elementos (N) - Escala Logarítmica', fontsize=12)
ax.set_ylabel('Tempo de Execução (ms) - Escala Logarítmica', fontsize=12)
ax.legend(title='Algoritmos')
ax.grid(True, which="both", linestyle='--', linewidth=0.5)

# 6. gráfico
plt.show()