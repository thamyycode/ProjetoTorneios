# 🎮 Projeto de Gerenciamento de Torneios (TH Games Hub) 🏆

Este projeto é uma aplicação simples e funcional, desenvolvida em Python, para gerenciar times, jogadores, torneios, inscrições e gerar relatórios detalhados, ideal para fãs de jogos competitivos como Valorant, League of Legends e outros games multiplayer. Pensado para quem curte o mundo dos e-sports, o sistema oferece uma forma prática e eficiente de organizar campeonatos e times.

## Autor
Thamyres Oliveira — Estudante de Engenharia de Software
[Meu LinkedIn](https://www.linkedin.com/in/thamyres-oliveira-112820357)

## Observações
Este projeto foi desenvolvido como parte do meu aprendizado em Engenharia de Software.
Feedbacks são super bem-vindos!


## Estrutura do Projeto

- `times.py` → Gerenciamento de times (CRUD)
- `jogadores.py` → Gerenciamento de jogadores (CRUD)
- `torneios.py` → Gerenciamento de torneios (CRUD)
- `inscricoes.py` → Gerenciamento de inscrições dos jogadores nos torneios
- `relatorios.py` → Geração de relatórios gerais e específicos

## Tecnologias Utilizadas

- Python 3.13
- Biblioteca [`tabulate`](https://pypi.org/project/tabulate/) (para exibição formatada no terminal)
- Arquivos `.txt` como base de dados simples

## Como Executar

Clone o repositório:

git clone (https://github.com/thamyycode/ProjetoTorneios.git)

cd ProjetoTorneios

```bash
pip install tabulate

python times.py
python jogadores.py
python torneios.py
python inscricoes.py
python relatorios.py

