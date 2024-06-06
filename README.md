# Global_solution_1_Python

## Índice

1. [Descrição](#descrição-memo)
2. [Pré-requisitos](#pré-requisitos-mag)
   - [Bibliotecas](#bibliotecas-books)
   - [Compilador](#compilador-computer)
3. [Instalação](#instalação-arrows_counterclockwise)
4. [Uso](#uso-rocket)
5. [Menu de Opções](#menu-de-opções-hammer_and_wrench)
   - [Gerar Dados](#gerar-dados-bar_chart)
   - [Visualização Gráfica](#visualização-gráfica-chart_with_upwards_trend)
   - [Cálculo da Média](#cálculo-da-média-abacus)
   - [Visualização no Terminal](#visualização-dos-valores-no-terminal-computer)
   - [Configuração da Cor do Terminal](#cores-no-terminal-art)
   - [Sair do Sistema](#sair-do-sistema-door)
6. [Desenvolvedores do Projeto](#desenvolvedores-do-projeto-man_technologist)

## Descrição :memo:

Olá! Nós, da equipe BluepH, faremos uma breve descrição do nosso projeto. Ele consiste em criar um gráfico baseado em dados simulados de pH. O projeto atualmente gera gráficos internos em um caminho especificado do computador, realiza as leituras e, através de um menu de interação com o usuário, é possível:

- Gerar dados fictícios
- Gerar um gráfico
- Mostrar a média dos valores
- Mostrar os valores no terminal
- Mudar a cor das letras no terminal

Futuramente, pretendemos utilizar dados gerados diretamente do Arduino. O link para o repositório da simulação do Arduino pode ser encontrado no seguinte [link](https://github.com/LucasYuki1/Global_solution_1_Edge).

## Pré-requisitos :mag:

### Bibliotecas :books:

- Biblioteca `matplotlib` para a visualização gráfica
- Biblioteca `os` para limpeza do terminal e verificação de existência de arquivo
- Biblioteca `random` para a geração de valores randômicos

### Compilador :computer:

No seu VSCode ou PyCharm, insira o [código fonte](https://github.com/LucasYuki1/Global_solution_1_Python-/blob/main/Global_solution/gs.py) na IDE, ou clone este repositório, após rodar o código basta apenas inserir os prompts no comando.

**Obs:** No PyCharm, a limpeza do terminal não funciona.

## Instalação :arrows_counterclockwise:

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/LucasYuki1/Global_solution_1_Python-

## Uso :rocket:

Após o repositório ser clonado na sua IDE, existem alguns passos a serem seguidos. Certifique-se de que o path do arquivo com os valores gerados seja ajustado conforme necessário, como no seguinte exemplo:

![Captura de tela 2024-06-05 183652](https://github.com/LucasYuki1/Global_solution_1_Python-/assets/148162404/cccf9fd6-6706-475c-a9f2-bbdbf7bcc7f9)

É importante que as "\\" sejam inseridas corretamente para que o Python faça a identificação do path e encontre o arquivo armazenado, retornando assim os valores.

## Menu de opções :hammer_and_wrench:

### Gerar dados :bar_chart:

Com a primeira opção do menu, uma lista de valores aleatórios uniformes com intervalo de 7.0 até 8.5 será gerada. É possível selecionar a quantidade de valores que serão gerados.

### Visualização gráfica :chart_with_upwards_trend:

Na segunda opção, será mostrado um gráfico indicando os pontos de variação do respectivo pH. Os pontos serão definidos de acordo com os dados do arquivo interno do computador, que foram gerados. Se não houver valores, o gráfico não mostrará nenhum ponto.

![Captura de tela 2024-06-05 183730](https://github.com/LucasYuki1/Global_solution_1_Python-/assets/148162404/61c54930-cf72-4f5c-9c3b-b5864d638b6b)

### Cálculo da média :abacus:

Com base nos valores do arquivo externo, o programa irá pegar os valores, fazer a soma e dividir pela quantidade de números, que é definida pela função len(ph_data), e mostrará no terminal.

### Visualização dos valores no terminal :computer:

Os valores poderão ser visualizados no terminal com a opção 4, dessa maneira, é possível ver com números os valores gerados pela opção 1.

### Cores no terminal :art:

Uma opção para o usuário é a troca de cores que são mostradas no terminal. Não tem uma utilização que afeta diretamente o usuário, porém pode ser útil alterar a coloração das letras dependendo do tema utilizado na IDE da pessoa que utilizará o sistema.

### Sair do sistema :door:

Com a última opção, você consegue encerrar o programa.

## Desenvolvedores do Projeto :man_technologist:

| Nome                          | RM      |
|-------------------------------|---------|
| Leonardo Rocha Scarpitta      | 555460  |
| Lucas Henzo Ide Yuki          | 554865  |
| Nicolas Haubricht Heinfellner | 556259  |
