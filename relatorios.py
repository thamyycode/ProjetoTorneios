import os
from tabulate import tabulate

CAMINHO_TIMES = "dados/times.txt"
CAMINHO_JOGADORES = "dados/jogadores.txt"
CAMINHO_TORNEIOS = "dados/torneios.txt"

def contar_registros(caminho):
    if not os.path.exists(caminho):
        return 0
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        # Descontar o cabeçalho, se tiver
        return max(len(linhas) - 1, 0)

def relatorio_quantidades():
    print("\n=== RELATÓRIO DE QUANTIDADES ===")
    dados = [
        ["Times cadastrados", contar_registros(CAMINHO_TIMES)],
        ["Jogadores cadastrados", contar_registros(CAMINHO_JOGADORES)],
        ["Torneios cadastrados", contar_registros(CAMINHO_TORNEIOS)]
    ]
    print(tabulate(dados, headers=["Categoria", "Quantidade"], tablefmt="fancy_grid"))

def ultimos_torneios(qtd=3):
    print(f"\n=== ÚLTIMOS {qtd} TORNEIOS CADASTRADOS ===")
    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Nenhum torneio cadastrado.")
        return
    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    if len(linhas) <= 1:
        print("Nenhum torneio cadastrado.")
        return

    # Pular cabeçalho e pegar os últimos qtd torneios
    ultimos = linhas[-qtd:]
    tabela = []
    for linha in ultimos:
        partes = linha.strip().split(";")
        if len(partes) == 4:
            id_torneio, nome, data, jogo = partes
            tabela.append([id_torneio, nome, data, jogo])
    print(tabulate(tabela, headers=["ID", "Nome", "Data", "Jogo"], tablefmt="fancy_grid"))

def jogos_dos_torneios():
    print("\n=== JOGOS ÚNICOS CADASTRADOS EM TORNEIOS ===")
    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Nenhum torneio cadastrado.")
        return

    jogos = set()
    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        next(f)  # Pular cabeçalho
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) == 4:
                jogos.add(partes[3])

    if jogos:
        tabela = [[jogo] for jogo in sorted(jogos)]
        print(tabulate(tabela, headers=["Jogos"], tablefmt="fancy_grid"))
    else:
        print("Nenhum jogo cadastrado.")

def menu_relatorios():
    while True:
        print("\n=== MENU RELATÓRIOS ===")
        print("1. Relatório de Quantidades")
        print("2. Últimos Torneios")
        print("3. Jogos dos Torneios")
        print("4. Voltar ao Menu Principal")
        print("-" * 30)
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            relatorio_quantidades()
        elif opcao == '2':
            ultimos_torneios()
        elif opcao == '3':
            jogos_dos_torneios()
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")
            
if __name__ == "__main__":
    menu_relatorios()
