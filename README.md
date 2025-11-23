<div align="center" width="100%" style="margin-top: 14px;">
  <img
    src="https://readme-typing-svg.demolab.com/?font=Iosevka&color=00FF00&width=1050&size=22&center=true&lines=+Mini+jogos+em+Python;Jogo+da+Forca;Jogo+da+Adivinhacao"
    alt="typing"
  />
</div>

# Menu de Jogos em Python  
Projeto simples e didático contendo dois jogos clássicos feitos em Python: **Forca** e **Adivinhação**.  
O usuário pode escolher qual deseja jogar através de um menu interativo no terminal.

Este projeto faz parte do meu início nos estudos de programação pela **Alura**, onde aprendi lógica, modularização e boas práticas em Python.

---

## Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de praticar:

- Lógica de programação  
- Modularização  
- Manipulação de arquivos  
- Estruturação de diretórios em projetos Python  

Ele contém:

- Menu inicial para seleção dos jogos  
- Jogo da Forca com categorias (países, frutas, animais)  
- Jogo de Adivinhação com três níveis de dificuldade  
- Sistema de ranking para ambos os jogos  
- Arquivos externos `.txt` para armazenar:
  - Palavras do jogo da forca  
  - Ranking da forca  
  - Ranking da adivinhação  
  - Histórico da adivinhação  

---

## Funcionalidades

### 1. Menu Principal
- Exibe as opções disponíveis  
- Permite escolher o jogo  
- Retorna ao menu após cada partida  

### 2. Jogo da Forca
- Categoria escolhida pelo usuário  
- Carregamento das palavras por meio de arquivos `.txt`  
- Desenho da forca conforme os erros  
- Sistema de pontuação  
- Salvamento automático do ranking

### 3. Jogo de Adivinhação
- Solicita o nome do jogador  
- Três níveis de dificuldade  
- Pontuação baseada na proximidade do chute  
- Histórico de partidas salvo automaticamente  
- Atualização do ranking  

---

## Estrutura do Projeto

```
GAMES/
├── adivinhacao/
│   ├── jogo_adivinhacao.py
│   ├── ranking.txt
│   └── historico.txt
├── forca/
│   ├── jogo_forca.py
│   ├── ranking.txt
│   ├── frutas.txt
│   ├── animais.txt
│   └── paises.txt
└── menu.py
```

---

## Tecnologias Utilizadas

- Python
  - Módulos padrão:
    - random
    -  os

## Erica Almeida
| Estudante de Engenharia de Computação | Iniciante em Python. 
| Comecei meus estudos na plataforma Alura, com foco em lógica, Python e boas práticas. 
| Interessada em programação e cibersegurança. |


