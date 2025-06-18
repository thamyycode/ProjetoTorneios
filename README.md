# 🎮 Projeto de Gerenciamento de Torneios 🏆

Este projeto é um sistema simples para gerenciar times, jogadores, torneios, inscrições e gerar relatórios. Foi desenvolvido como parte da disciplina de Engenharia de Software, com foco em boas práticas e organização de código.

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

```bash
git clone https://github.com/thamyycode/ProjetoTorneios.git
cd ProjetoTorneios

pip install tabulate

python times.py
python jogadores.py
python torneios.py
python inscricoes.py
python relatorios.py

Autor
Thamy — Estudante de Engenharia de Software
[Meu LinkedIn](linkedin.com/in/thamyres-oliveira-112820357)

Observações
Este projeto foi desenvolvido como parte do meu aprendizado em Engenharia de Software.
Feedbacks são super bem-vindos! 
