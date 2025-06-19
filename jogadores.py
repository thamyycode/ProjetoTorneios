import os
from tabulate import tabulate

# Criar diretório e arquivo automaticamente se não existir
os.makedirs("dados", exist_ok=True)
if not os.path.exists("dados/jogadores.txt"):
    with open("dados/jogadores.txt", "w") as arquivo:
        arquivo.write("ID;Nome;Posição;ID_Time\n")  # Adiciona cabeçalho inicial

def incluir_jogador():
    print("\n=== Inclusão de Jogador ===")
    id_do_jogador = input("Digite o ID do jogador: ").strip()
    nome_do_jogador = input("Digite o nome do jogador: ").strip()
    posicao = input("Digite a posição do jogador: ").strip()
    id_do_time = input("Digite o ID do time ao qual pertence: ").strip()

    existe = False
    try:
        with open("dados/times.txt", "r") as arquivo_times:
            next(arquivo_times)
            for linha in arquivo_times:
                partes = linha.strip().split(";")
                if partes[0] == id_do_time:
                    existe = True
                    break
    except FileNotFoundError:
        print("Arquivo de times não encontrado.")
        return

    if not existe:
        print("ERRO: ID do time não encontrado. Verifique e tente novamente.")
        return

    try:
        with open("dados/jogadores.txt", "r") as arquivo_jogadores:
            for linha in arquivo_jogadores:
                partes = linha.strip().split(";")
                if partes[0] == id_do_jogador:
                    print(f"\nERRO: O jogador com ID '{id_do_jogador}' já está cadastrado!\n")
                    return
    except FileNotFoundError:
        pass

    linha = f"{id_do_jogador};{nome_do_jogador};{posicao};{id_do_time}\n"
    with open("dados/jogadores.txt", "a") as arquivo:
        arquivo.write(linha)
        arquivo.flush()

    print("Jogador incluído com sucesso!")

def alterar_jogador():
    print("\n=== Alterar Jogador ===")
    id_alvo = input("Digite o ID do jogador que deseja alterar: ").strip()

    try:
        with open("dados/jogadores.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de jogadores não encontrado.")
        return

    encontrado = False
    jogadores_alterados = []

    for linha in linhas:
        partes = linha.strip().split(";")
        if len(partes) != 4:
            jogadores_alterados.append(linha)
            continue

        id_jogador, nome, posicao, id_time = partes

        if id_jogador == id_alvo:
            print(f"Jogador encontrado: {nome}, Posição: {posicao}, Time ID: {id_time}")
            novo_nome = input(f"Novo nome (Enter para manter '{nome}'): ").strip()
            nova_posicao = input(f"Nova posição (Enter para manter '{posicao}'): ").strip()
            novo_id_time = input(f"Novo ID do time (Enter para manter '{id_time}'): ").strip()

            if novo_id_time:
                id_time_existe = False
                try:
                    with open("dados/times.txt", "r") as arq_times:
                        next(arq_times)
                        for linha in arq_times:
                            partes = linha.strip().split(";")
                            if partes[0] == novo_id_time:
                                id_time_existe = True
                                break
                except FileNotFoundError:
                    print("Arquivo de times não encontrado.")
                    return

                if not id_time_existe:
                    print("ID do time não encontrado. Alteração cancelada.")
                    return

            nome = novo_nome if novo_nome else nome
            posicao = nova_posicao if nova_posicao else posicao
            id_time = novo_id_time if novo_id_time else id_time

            nova_linha = f"{id_jogador};{nome};{posicao};{id_time}\n"
            jogadores_alterados.append(nova_linha)
            encontrado = True
        else:
            jogadores_alterados.append(linha)

    if not encontrado:
        print("Jogador com esse ID não foi encontrado.")
        return

    with open("dados/jogadores.txt", "w") as arquivo:
        arquivo.writelines(jogadores_alterados)

    print("Jogador alterado com sucesso!")

def excluir_jogador():
    print("\n=== Excluir Jogador ===")
    id_jogador = input("Digite o ID do jogador que deseja excluir: ").strip()

    try:
        with open("dados/jogadores.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de jogadores não encontrado.")
        return

    encontrado = False
    jogadores_alterados = []

    for linha in linhas:
        partes = linha.strip().split(";")
        if len(partes) < 4:
            jogadores_alterados.append(linha)
            continue

        if partes[0] != id_jogador:
            jogadores_alterados.append(linha)
        else:
            encontrado = True

    if not encontrado:
        print("Jogador com esse ID não foi encontrado.")
        return

    with open("dados/jogadores.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(jogadores_alterados)

    print(f"Jogador com ID '{id_jogador}' excluído com sucesso!")

def listar_jogadores():
    print("\n=== Listagem de Jogadores ===")
    try:
        with open("dados/jogadores.txt", "r") as arq_jogadores:
            linhas = arq_jogadores.readlines()
            if len(linhas) <= 1:
                print("Nenhum jogador cadastrado.")
                return
    except FileNotFoundError:
        print("Arquivo de jogadores não encontrado.")
        return

    tabela = []
    for linha in linhas[1:]:
        partes = linha.strip().split(";")
        if len(partes) != 4:
            continue
        id_jogador, nome_jogador, posicao, id_time = partes
        tabela.append([id_jogador, nome_jogador, posicao, id_time])

    print(tabulate(tabela, headers=["ID", "Nome", "Posição", "ID do Time"], tablefmt="fancy_grid"))
    print(f"\nTotal de jogadores listados: {len(tabela)}")

def pesquisar_jogadores():
    print("\n=== Pesquisar Jogador ===")
    termo = input("Digite parte do nome para buscar: ").strip().lower()

    try:
        with open("dados/jogadores.txt", "r", encoding="utf-8") as arquivo:
            jogadores = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de jogadores não encontrado.")
        return

    encontrados = [j.strip() for j in jogadores if termo in j.lower()]

    if encontrados:
        print("\nJogadores encontrados:")
        for jogador in encontrados:
            print(jogador)
    else:
        print("Nenhum jogador encontrado com esse termo.")

def menu_jogadores():
    while True:
        print("\n=== MENU JOGADORES ===")
        print("1. Incluir Jogador")
        print("2. Alterar Jogador")
        print("3. Excluir Jogador")
        print("4. Listar Jogadores")
        print("5. Pesquisar Jogadores")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            incluir_jogador()
        elif opcao == '2':
            alterar_jogador()
        elif opcao == '3':
            excluir_jogador()
        elif opcao == '4':
            listar_jogadores()
        elif opcao == '5':
            pesquisar_jogadores()
        elif opcao == '6':
            break
        else:
            print(f"Opção inválida: {opcao}. Tente novamente.")

if __name__ == "__main__":
    menu_jogadores()
