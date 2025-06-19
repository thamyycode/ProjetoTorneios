import os
from tabulate import tabulate

CAMINHO_TORNEIOS = "dados/torneios.txt"

def incluir_torneio():
    print("\n=== Cadastro de Torneio ===")
    nome = input("Nome do torneio: ").strip()
    data = input("Data do torneio (dd/mm/aaaa): ").strip()
    jogo = input("Nome do jogo: ").strip()

    if not os.path.exists(CAMINHO_TORNEIOS):
        with open(CAMINHO_TORNEIOS, "w", encoding="utf-8") as f:
            f.write("ID;Nome;Data;Jogo\n")  # cabeçalho

    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        proximo_id = len(linhas)  # considerando que a primeira linha é o cabeçalho

    with open(CAMINHO_TORNEIOS, "a", encoding="utf-8") as f:
        f.write(f"{proximo_id};{nome};{data};{jogo}\n")
    print("Torneio cadastrado com sucesso!")

def listar_torneios():
    print("\n=== Lista de Torneios ===")

    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Arquivo de torneios não encontrado.")
        return

    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    if len(linhas) <= 1:
        print("Nenhum torneio cadastrado.")
        return

    tabela = []
    for linha in linhas[1:]:  # pula o cabeçalho
        partes = linha.strip().split(";")
        if len(partes) >= 4:
            tabela.append(partes)

    print(tabulate(tabela, headers=["ID", "Nome do Torneio", "Data", "Jogo"], tablefmt="fancy_grid"))
    print(f"\nTotal de torneios: {len(tabela)}")

def pesquisar_torneios():
    print("\n=== Pesquisar Torneio ===")
    termo = input("Digite parte do nome do torneio: ").strip().lower()

    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Arquivo de torneios não encontrado.")
        return

    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    encontrados = []
    for linha in linhas[1:]:  # pula o cabeçalho
        partes = linha.strip().split(";")
        if len(partes) >= 4 and termo in partes[1].lower():
            encontrados.append(partes)

    if encontrados:
        print("\nTorneios encontrados:")
        print(tabulate(encontrados, headers=["ID", "Nome do Torneio", "Data", "Jogo"], tablefmt="fancy_grid"))
    else:
        print("Nenhum torneio encontrado com esse nome.")

def alterar_torneio():
    listar_torneios()
    id_alvo = input("\nDigite o ID do torneio que deseja alterar: ").strip()

    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Arquivo de torneios não encontrado.")
        return

    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    encontrado = False
    for i in range(1, len(linhas)):
        partes = linhas[i].strip().split(";")
        if partes[0] == id_alvo:
            print(f"Torneio atual: {partes[1]} - {partes[2]} - {partes[3]}")
            novo_nome = input("Novo nome do torneio: ").strip()
            nova_data = input("Nova data do torneio (dd/mm/aaaa): ").strip()
            novo_jogo = input("Novo nome do jogo: ").strip()
            linhas[i] = f"{id_alvo};{novo_nome};{nova_data};{novo_jogo}\n"
            encontrado = True
            break

    if encontrado:
        with open(CAMINHO_TORNEIOS, "w", encoding="utf-8") as f:
            f.writelines(linhas)
        print("Torneio alterado com sucesso!")
    else:
        print(" ID não encontrado.")

def excluir_torneio():
    listar_torneios()
    id_alvo = input("\nDigite o ID do torneio que deseja excluir: ").strip()

    if not os.path.exists(CAMINHO_TORNEIOS):
        print("Arquivo de torneios não encontrado.")
        return

    with open(CAMINHO_TORNEIOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    nova_lista = [linhas[0]]  # cabeçalho
    encontrado = False

    for linha in linhas[1:]:
        partes = linha.strip().split(";")
        if partes[0] != id_alvo:
            nova_lista.append(linha)
        else:
            encontrado = True

    if encontrado:
        with open(CAMINHO_TORNEIOS, "w", encoding="utf-8") as f:
            f.writelines(nova_lista)
        print("Torneio excluído com sucesso!")
    else:
        print("ID não encontrado.")

def menu_torneios():
    while True:
        print("\n=== MENU TORNEIOS ===")
        print("1. Cadastrar Torneio")
        print("2. Listar Torneios")
        print("3. Pesquisar Torneio")
        print("4. Alterar Torneio")
        print("5. Excluir Torneio")
        print("6. Voltar ao Menu Principal")
        print("-" * 30)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            incluir_torneio()
        elif opcao == "2":
            listar_torneios()
        elif opcao == "3":
            pesquisar_torneios()
        elif opcao == "4":
            alterar_torneio()
        elif opcao == "5":
            excluir_torneio()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tenta de novo!")

if __name__ == "__main__":
    menu_torneios()
