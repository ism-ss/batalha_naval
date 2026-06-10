# Batalha Naval - Matriz Python

## Descrição

Este projeto implementa uma versão simplificada do jogo Batalha Naval utilizando Python e matrizes (listas de listas). O programa gera automaticamente um tabuleiro 10x10 contendo navios e permite que o jogador realize tiros informando linha e coluna. O sistema contabiliza acertos, erros e estatísticas da partida.

## Como executar

1. Certifique-se de ter o Python instalado.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python main.py
```

## Regras do jogo

* O tabuleiro possui tamanho 10x10.
* Existem navios distribuídos automaticamente pelo sistema.
* O jogador escolhe uma linha e uma coluna para realizar um tiro.
* Acertos são marcados com `X`.
* Erros são marcados com `O`.
* Não é permitido repetir tiros na mesma posição.
* O jogo termina quando todos os navios forem destruídos ou quando o jogador digitar `-1` para sair.

## Exemplo de uso

```text
Aperte enter para começar a Batalha Naval

--- MENU ---
1 - Mostrar Tabuleiro
2 - Dar Tiro

Escolha: 2

Digite a linha do tabuleiro onde deseja atirar: 4
Digite a coluna do tabuleiro onde deseja atirar: 7

Acertou!
```

## Tecnologias utilizadas

* Python
* Matrizes (listas de listas)
* Estruturas de repetição
* Estruturas condicionais
* Funções
* Biblioteca random
