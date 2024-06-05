import matplotlib.pyplot as plt
import os
import random

# Inicializa a variável terminal com código ANSI padrão para resetar cor
terminal = '\033[m'

# Definir o caminho do arquivo (ajuste conforme necessário)
file_path = 'C:\\Users\\Lucas Enzo Ideyuki\\Desktop\\caderno\\fiap\\Python\\Senha-jogo\\ph_data.txt'

def cor(parametro):
    """Função para definir a cor do terminal"""
    match parametro:
        case 1:
            terminal = '\033[31m'
        case 2:
            terminal = '\033[32m'
        case 3:
            terminal = '\033[33m'
        case 4:
            terminal = '\033[m'
        case 5:
            terminal = '\033[35m'
        case 6:
            terminal = '\033[36m'
        case 7:
            terminal = '\033[7m'
        case 8:
            terminal = '\033[m'
        case _:
            print('Opção inválida')
            menu()
    return terminal

def limpar():
    """Função para limpar o terminal"""
    os.system('cls')

def sair():
    """Função para sair do programa"""
    print('Obrigado por usar o nosso sistema!')
    exit()

def gerar_dados(leituras=100):
    """Função para gerar dados simulados de pH"""
    dados = []
    for _ in range(leituras):
        # Simulando leituras de pH entre 7.0 e 8.5
        ph_value = round(random.uniform(7.0, 8.5), 2)
        dados.append(ph_value)
    return dados

def ler_dados():
    """Função para ler dados de pH do arquivo"""
    ph_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            ph_data = [float(line.strip()) for line in file]
    return ph_data

def salvar_dados(ph_data):
    """Função para salvar dados de pH no arquivo"""
    with open(file_path, 'w') as file:
        for ph in ph_data:
            file.write(f"{ph}\n")
    print(f"Dados de pH simulados gerados e salvos em '{file_path}'")

def gerar_grafico(ph_data):
    """Função para gerar gráfico das leituras de pH"""
    plt.figure(figsize=(10, 6))
    plt.plot(ph_data, marker='o', linestyle='-', color='b')
    plt.title('Simulação de Leituras de pH')
    plt.xlabel('Número da Leitura')
    plt.ylabel('Valor do pH')
    plt.ylim(6.5, 9.0)  # Definindo o limite do eixo y para visualização
    plt.grid(True)
    plt.show()

def media(ph_data):
    """Função para calcular e imprimir a média dos valores de pH"""
    ph_media = sum(ph_data) / len(ph_data)
    print(f'O pH médio é de: {ph_media:.1f}')
    print('-='*15)

def valor_terminal(ph_data):
    """Função para imprimir os valores de pH no terminal"""
    print()
    for i in ph_data:
        print(f'{i:.1f}, ', end='')
    print('...')

def menu():
    """Função para exibir o menu e lidar com as opções do usuário"""
    global terminal       # Criação de uma variável global que poderá ser alterada
    ph_data = ler_dados()
    while True:
        print(f"""
{terminal}         
1- Gerar dados 
2- Visualização gráfica das leituras do pH
3- Média calculada dos valores lidos
4- Visualizar os valores no terminal
5- Selecionar uma cor para o terminal
6- Sair

Selecione uma opção:
""")
        opcao = int(input())
        limpar()
        print(f'Opção selecionada: {opcao}')
        print('-=' * 15)
        if opcao == 1:
            ph_data = gerar_dados(int(input('Digite quantas leituras você deseja: ')))
            salvar_dados(ph_data)
        elif opcao == 2:
            gerar_grafico(ph_data)
        elif opcao == 3:
            media(ph_data)
        elif opcao == 4:
            valor_terminal(ph_data)
        elif opcao == 5:
            parametro = int(input(f'''
Opções:
1- Vermelho
2- Verde
3- Amarelo
4- Azul
5- Roxo
6- Ciano
7- Inversão de cor
8- Remover cor
                                  
Selecione uma opção:
'''))
            terminal = cor(parametro)
        elif opcao == 6:
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
