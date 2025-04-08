# Sistema de Gerenciamento de Estacionamento
# Descrição: Desenvolver um sistema para gerenciar as vagas de um estacionamento. O sistema
# deve permitir o registro de entrada e saída de veículos, calcular o tempo de permanência e o valor
# a ser pago.
# Funcionalidades (50 pontos):
# o Registro de entrada e saída de veículos com data e hora (15 pontos).
# o Cálculo do tempo de permanência e do valor a ser pago com base no tempo (15 pontos).
# o Exibição de relatório com todos os veículos estacionados no momento (10 pontos).
# o Salvamento e leitura/exibição dos registros em um arquivo de texto (10 pontos).

import datetime

estacionamento = {}

def salvar_registros(nome_arquivo):
    """Salva os registros do estacionamento em um arquivo txt."""
    with open(nome_arquivo, 'w') as arquivo:
        for placa, dados in estacionamento.items():
            entrada = dados['entrada'].strftime("%Y-%m-%d %H:%M:%S") if dados['entrada'] else 'N/A'
            saida = dados['saida'].strftime("%Y-%m-%d %H:%M:%S") if dados['saida'] else 'N/A'
            arquivo.write(f"placa: {placa}, entrada: {entrada}, saída: {saida}\n")
    print(f"Registros salvos em {nome_arquivo}")

def registrar_entrada(placa):
    """Registra a entrada de um veículo."""
    if placa in estacionamento:
        print("veículo já está estacionado.")
    else:
        agora = datetime.datetime.now()
        estacionamento[placa] = {'entrada': agora, 'saida': None}
        print(f"Veículo {placa} registrado com entrada às {agora}")

def registrar_saida(placa):
    """Registra a saída do veículo."""
    if placa not in estacionamento or estacionamento[placa]['saida'] is not None: # procura pela ausência da chave placa no dicionário ou pelo valor da saída não ser nula,
        # pois aí já haveria uma saída.
        print("Veículo não encontrado.")
    else:
        agora = datetime.datetime.now() # atribui o horário do sistema à variável
        estacionamento[placa]['saida'] = agora # atribui a variável ao valor de saída
        print(f"Veículo {placa} saiu às {agora}")

def calcular_tempo_virgula(entrada, saida):
    """Calcula o tempo em horas entre a entrada e saída."""
    tempo = saida - entrada
    return tempo.total_seconds() / 3600

def calcular_valor(tempo):
    """calcula o valor a ser pago com base no tempo >em horas<."""
    taxa_por_hora = 6.0
    return tempo * taxa_por_hora

def calcular_valor_a_ser_pago(placa):
    """Calcula o valor a ser pago p um veículo específico."""
    if placa in estacionamento and estacionamento[placa]['saida']:
        entrada = estacionamento[placa]['entrada']
        saida = estacionamento[placa]['saida']
        tempo = calcular_tempo_virgula(entrada, saida)
        valor = calcular_valor(tempo)
        return valor
    else:
        print("Veículo não encontrado ou saída não registrada.")
        return None

def exibir_relatorio():
    """Exibe todos os veículos q estao estacionados no momento."""
    print("Veículos estacionados no momento:")
    for placa, dados in estacionamento.items():
        if dados['saida'] is None:
            print(f"placa: {placa}, entrada: {dados['entrada']}")

def main():
    while True:
        print("\n--- Sistema de gerenciamento do estacionamento Entra e Sai ---")
        print("1. Registrar entrada de veículo")
        print("2. Registrar saída de veículo")
        print("3. Calcular valor a ser pago")
        print("4. Exibir veículos estacionados")
        print("5. Salvar registros")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Digite a placa do veículo: ")
            registrar_entrada(placa)
        elif opcao == '2':
            placa = input("Digite a placa do veículo: ")
            registrar_saida(placa)
        elif opcao == '3':
            placa = input("Digite a placa do veículo: ")
            valor = calcular_valor_a_ser_pago(placa)
            if valor is not None:
                print(f"Valor a ser pago: R${valor:.2f}")
        elif opcao == '4':
            exibir_relatorio()
        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo para salvar os registros: ")
            salvar_registros(nome_arquivo)
        elif opcao == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
