## Desenvolva um jogo de RPG em Python que atenda aos seguintes requisitos:

### Título e Boas-Vindas:
- Ao iniciar o jogo, exiba um título e uma mensagem de boas-vindas com um elemento visual ASCII.

### Criação de Personagem:
- O jogador deve informar seu nome ao iniciar o jogo.
- O personagem deve começar com os seguintes atributos:
  - <b>HP (pontos de vida):</b> 100
  - <b>Level (nível):</b> 1
  - <b>Força:</b> 3
  - <b>EXP (experiência):</b> 0
  - <b>Inventário:</b> vazio
  - <b>Status:</b> vivo

### Sistema de Combate:
- O jogador pode enfrentar monstros sorteados com base no nível do personagem.
- Cada monstro possui os atributos: <b>nome, HP, força e experiência concedida ao ser derrotado</b>.
- Durante o combate, ataques podem causar dano com base na força e sorte de ambos os lados.
- O jogador pode:
  - <b>Atacar:</b> causar dano ao monstro.
  - <b>Usar item:</b> consumir itens do inventário, como poções que recuperam HP.
  - <b>Fugir:</b> tentar escapar da batalha.
  - <b>Visualizar status:</b> exibir os atributos do jogador.
  - <b>Sair do jogo:</b> encerrar a partida.

### Progressão do Personagem:
- Ao derrotar um monstro, o jogador recebe pontos de experiência e pode subir de nível.
- Subir de nível restaura o HP, dobra a força e redefine a experiência necessária para o próximo nível.

### Itens e Inventário:
- Há uma chance de o jogador receber uma poção ao derrotar um monstro.
- Poções podem ser usadas para recuperar HP.

### Fim de Jogo:
- O jogo termina se o jogador perder todo o HP ou optar por sair.
- Exiba uma mensagem de "Game Over" ao final do jogo.

### Requisitos Técnicos:
- Implemente o código usando funções para organizar as diferentes funcionalidades do jogo, como combate, criação de personagem, e sorteio de monstros.
- Utilize a biblioteca random para eventos aleatórios, como a sorte dos ataques e o sorteio de monstros.

###Resumo dos Conceitos de Python Abordados
1. Importação de Módulos (```import random```)
2. Trabalhando com Strings e Impressão (```print, multi-line strings, raw strings```)
3. Definição e Chamada de Funções (```def, return```)
4. Variáveis e Tipos de Dados (```str, int, list, bool```)
5. Entrada de Dados do Usuário (```input()```)
6. Estruturas de Dados (```Listas```)
7. Estruturas Condicionais (```if, elif, else```)
8. Laços de Repetição (```while```)
9. Funções com Parâmetros e Retorno de Valores
10. Manipulação de Listas (Adicionar, Remover, Iterar)
11. Geração de Números Aleatórios (```random.choice(), random.randint(), random.random()```)
12. Formatação de Strings Avançada (```f-strings```)
13. Gerenciamento de Estado do Programa (```if __name__ == "__main__":```)
14. Conceitos Avançados (Opcional): Programação Orientada a Objetos, Manipulação de Arquivos, etc.
