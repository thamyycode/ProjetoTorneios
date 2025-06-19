import os
from tabulate import tabulate  # Importa o tabulate

# Cria o diretório 'dados' e o arquivo 'times.txt' com cabeçalho, se ainda não existirem
os.makedirs("dados", exist_ok=True)
if not os.path.exists("dados/times.txt"):
    with open("dados/times.txt", "w") as arquivo:
        arquivo.write("ID;Nome do Time;Nome do Jogo\n")  # Cabeçalho

def incluir_time():
    print("\n=== Incluir Time ===")
    id_time = input("Digite o ID do time: ").strip()
    nome_time = input("Digite o nome do time: ").strip()
    nome_jogo = input("Digite o nome do jogo: ").strip()

    try:
        with open("dados/times.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if partes[0] == id_time:
                    print(f"ERRO: Já existe um time com o ID '{id_time}'!")
                    return
    except FileNotFoundError:
        pass  # Se o arquivo não existir, ele será criado depois

    with open("dados/times.txt", "a") as arquivo:
        linha = f"{id_time};{nome_time};{nome_jogo}\n"
        arquivo.write(linha)

    print("Time incluído com sucesso!")

def alterar_time():
    print("\n=== Alterar Time ===")
    id_alvo = input("Digite o ID do time que deseja alterar: ").strip()

    try:
        with open("dados/times.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de times não encontrado.")
        return

    encontrado = False
    novos_dados = []

    for linha in linhas:
        partes = linha.strip().split(";")
        if len(partes) < 3 or partes[0] == "ID":
            novos_dados.append(linha)
            continue

        id_time, nome_time, nome_jogo = partes

        if id_time == id_alvo:
            print(f"Time encontrado: {nome_time} (Jogo: {nome_jogo})")
            novo_nome = input(f"Novo nome do time (Enter para manter '{nome_time}'): ").strip()
            novo_jogo = input(f"Novo nome do jogo (Enter para manter '{nome_jogo}'): ").strip()

            nome_time = novo_nome if novo_nome else nome_time
            nome_jogo = novo_jogo if novo_jogo else nome_jogo

            nova_linha = f"{id_time};{nome_time};{nome_jogo}\n"
            novos_dados.append(nova_linha)
            encontrado = True
        else:
            novos_dados.append(linha)

    if not encontrado:
        print("Time com esse ID não foi encontrado.")
        return

    with open("dados/times.txt", "w") as arquivo:
        arquivo.writelines(novos_dados)

    print("Time alterado com sucesso!")

def excluir_time():
    print("\n=== Excluir Time ===")
    id_excluir = input("Digite o ID do time que deseja excluir: ").strip()

    try:
        with open("dados/times.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de times não encontrado.")
        return

    encontrado = False
    novos_dados = []

    for linha in linhas:
        partes = linha.strip().split(";")
        if len(partes) < 3 or partes[0] == "ID":
            novos_dados.append(linha)
            continue

        if partes[0] != id_excluir:
            novos_dados.append(linha)
        else:
            encontrado = True

    if not encontrado:
        print("ID não encontrado. Nenhum time excluído.")
        return

    with open("dados/times.txt", "w") as arquivo:
        arquivo.writelines(novos_dados)

    print(f"Time com ID '{id_excluir}' foi excluído com sucesso!")

def listar_times():
    print("\n=== Lista de Times ===")

    try:
        with open("dados/times.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de times não encontrado.")
        return

    if len(linhas) <= 1:
        print("Nenhum time cadastrado.")
        return

    tabela = []
    for linha in linhas[1:]:  # pula o cabeçalho
        partes = linha.strip().split(";")
        if len(partes) >= 3:
            tabela.append(partes)

    print(tabulate(tabela, headers=["ID", "Nome do Time", "Nome do Jogo"], tablefmt="fancy_grid"))
    print(f"\nTotal de times: {len(tabela)}")

def pesquisar_times():
    print("\n=== Pesquisar Time ===")
    termo = input("Digite parte do nome do time: ").strip().lower()

    try:
        with open("dados/times.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de times não encontrado.")
        return

    encontrados = []

    for linha in linhas[1:]:  # pula o cabeçalho
        partes = linha.strip().split(";")
        if len(partes) >= 3 and termo in partes[1].lower():
            encontrados.append(partes)

    if encontrados:
        print("\nTimes encontrados:")
        print(tabulate(encontrados, headers=["ID", "Nome do Time", "Nome do Jogo"], tablefmt="fancy_grid"))
    else:
        print("Nenhum time encontrado com esse nome.")

def menu_times():
    while True:
        print("\n=== MENU TIMES ===")
        print("1. Incluir Time")
        print("2. Alterar Time")
        print("3. Excluir Time")
        print("4. Listar Times")
        print("5. Pesquisar Time")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            incluir_time()
        elif opcao == '2':
            alterar_time()
        elif opcao == '3':
            excluir_time()
        elif opcao == '4':
            listar_times()
        elif opcao == '5':
            pesquisar_times()
        elif opcao == '6':
            break
        else:
            print(f"Opção inválida: {opcao}. Tente novamente.")

if __name__ == "__main__":
    menu_times()
