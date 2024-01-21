
# Software de Gestão para Locadora de Veículos
Este código em Python implementa um sistema simples para uma locadora de veículos. O programa permite ao usuário visualizar os veículos disponíveis, alugar um veículo por um determinado número de dias, devolver um veículo alugado e sair do sistema.
<hr>

##Estrutura do Código:

A lista veiculos contém tuplas representando veículos e seus preços de aluguel por dia.
<hr>

## Loop Principal:

O programa entra em um loop principal, onde o usuário pode escolher entre as opções de visualizar veículos, alugar, devolver ou sair do sistema.
<hr>

### Visualizar Veículos:

Esta opção exibe os veículos disponíveis e seus preços por dia.
<hr>

### Alugar Veículo:

Nesta opção, o usuário pode selecionar um veículo da lista, escolher o número de dias para aluguel e confirmar a transação. Os veículos alugados são armazenados em veiculos_alugados, enquanto os disponíveis são atualizados em veiculos.
<hr>

### Devolver Veículo:
Nesta opção, o programa permite ao usuário devolver um veículo previamente alugado. O veículo devolvido é removido da lista de veículos alugados e adicionado à lista de veículos disponíveis.
<hr>

### Sair:
Se o usuário escolher a opção 3, o programa exibe uma mensagem de despedida e encerra o loop principal, finalizando a execução.
<hr>

## Considerações Finais:
O código usa estruturas de repetição (while), condicionais (if, elif, else) e manipulação de listas para criar um sistema básico de locadora de veículos em Python. Ele também incorpora o uso da biblioteca os para limpar a tela do console, tornando a experiência mais amigável ao usuário, seja ele de Windows, Mac ou Linux.
<hr>
