import os
import shutil
from tabulate import tabulate 
from colorama import init, Fore, Style
from times import incluir_time, alterar_time, excluir_time, listar_times, pesquisar_times
from jogadores import incluir_jogador, alterar_jogador, excluir_jogador, listar_jogadores, pesquisar_jogadores
from torneios import incluir_torneio, alterar_torneio, excluir_torneio, listar_torneios, pesquisar_torneios
from inscricoes import menu_inscricoes, inscrever_time, listar_inscricoes, cancelar_inscricao
from relatorios import menu_relatorios, relatorio_quantidades, ultimos_torneios,  jogos_dos_torneios

init()

Titulo = """ 
 _________ ____  ____                                    
|  _   _  |_   ||   _|                                   
|_/ | | \_| | |__| |                                     
    | |     |  __  |                                     
   _| |_   _| |  | |_                                    
  |_____| |____||____|                                   
                                                         
   ______       _      ____    ____ ________   ______    
 .' ___  |     / \    |_   \  /   _|_   __  |.' ____ \   
/ .'   \_|    / _ \     |   \/   |   | |_ \_|| (___ \_|  
| |   ____   / ___ \    | |\  /| |   |  _| _  _.____`.   
\ `.___]  |_/ /   \ \_ _| |_\/_| |_ _| |__/ || \____) |  
 `._____.'|____| |____|_____||_____|________| \______.'  
                                                         
 ____  ____ _____  _____ ______                          
|_   ||   _|_   _||_   _|_   _ \                         
  | |__| |   | |    | |   | |_) |                        
  |  __  |   | '    ' |   |  __'.                        
 _| |  | |_   \ \__/ /   _| |__) |                       
|____||____|   `.__.'   |_______/                        
                                                         """

def exibir_menu():
    os.system("cls" if os.name == "nt" else "clear")
    largura_terminal = shutil.get_terminal_size().columns

    # Centralizando o título
    titulo_centralizado = "\n".join(line.center(largura_terminal) for line in Titulo.split("\n"))
    
    print(f"{Fore.MAGENTA}{titulo_centralizado}{Style.RESET_ALL}")


def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        init(autoreset=True)

        menu = [
            ["1", "Times"],
            ["2", "Jogadores"],
            ["3", "Torneios"],
            ["4", "Inscrições"],
            ["5", "Relatórios"],
            ["0", "Sair"]
        ]
        print(Fore.CYAN + Style.BRIGHT + "=== SISTEMA DE GERENCIAMENTO DE TORNEIOS E TIMES ===")
        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()
        opcao = input(Fore.BLUE + "Escolha uma opção: ")
        if opcao == "1":
            menu_times()
        elif opcao == "2":
            menu_jogadores()
        elif opcao == "3":
            menu_torneios()
        elif opcao == "4":
            menu_inscricoes()
        elif opcao == "5":
            menu_relatorios()
        elif opcao == "0":
            print(Fore.GREEN + "Saindo... Até logo! :)")
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")

def menu_times():
    init(autoreset=True)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        menu = [
            ["1", "Incluir Time"],
            ["2", "Alterar Time"],
            ["3", "Excluir Time"],
            ["4", "Listar Times"],
            ["5", "Pesquisar Times"],
            ["0", "Voltar ao menu principal"]
        ]
        print(Fore.CYAN + Style.BRIGHT + "=== MENU TIMES ===")
        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()
        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        if opcao == "1":
            incluir_time()
            input(Fore.GREEN + "\nTime incluído! Pressione Enter para continuar...")
        elif opcao == "2":
            alterar_time()
            input(Fore.GREEN + "\nTime alterado! Pressione Enter para continuar...")
        elif opcao == "3":
            excluir_time()
            input(Fore.GREEN + "\nTime excluído! Pressione Enter para continuar...")
        elif opcao == "4":
            listar_times()
            input(Fore.CYAN + "\nPressione Enter para continuar...")
        elif opcao == "5":
            pesquisar_times()
            input(Fore.CYAN + "\nPressione Enter para continuar...")
        elif opcao == "0":
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")

def menu_jogadores():
    init(autoreset=True)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        menu = [
            ["1", "Incluir Jogador"],
            ["2", "Alterar Jogador"],
            ["3", "Excluir Jogador"],
            ["4", "Listar Jogadores"],
            ["5", "Pesquisar Jogadores"],
            ["0", "Voltar ao Menu Principal"]
        ]

        print(Fore.CYAN + Style.BRIGHT + "=== MENU JOGADORES ===")
        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()
        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        if opcao == "1":
            incluir_jogador()
            input(Fore.GREEN + "\nJogador incluído! Pressione Enter para continuar...")
        elif opcao == "2":
            alterar_jogador()
            input(Fore.GREEN + "\nJogador alterado! Pressione Enter para continuar...")
        elif opcao == "3":
            excluir_jogador()
            input(Fore.GREEN + "\nJogador excluído! Pressione Enter para continuar...")
        elif opcao == "4":
            listar_jogadores()
            input(Fore.BLUE + "\nPressione Enter para continuar...")
        elif opcao == "5":
            pesquisar_jogadores()
            input(Fore.BLUE + "\nPressione Enter para continuar...")
        elif opcao == "0":
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")


def menu_torneios():
    init(autoreset=True)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        menu = [
            ["1", "Incluir Torneio"],
            ["2", "Alterar Torneio"],
            ["3", "Excluir Torneio"],
            ["4", "Listar Torneios"],
            ["5", "Pesquisar Torneios"],
            ["0", "Voltar ao Menu Principal"]
        ]

        print(Fore.CYAN + Style.BRIGHT + "=== MENU TORNEIOS ===")
        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()
        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        if opcao == "1":
            incluir_torneio()
            input(Fore.GREEN + "\nTorneio incluído! Pressione Enter para continuar...")
        elif opcao == "2":
            alterar_torneio()
            input(Fore.GREEN + "\nTorneio alterado! Pressione Enter para continuar...")
        elif opcao == "3":
            excluir_torneio()
            input(Fore.GREEN + "\nTorneio excluído! Pressione Enter para continuar...")
        elif opcao == "4":
            listar_torneios()
            input(Fore.BLUE + "\nPressione Enter para continuar...")
        elif opcao == "5":
            pesquisar_torneios()
            input(Fore.BLUE + "\nPressione Enter para continuar...")
        elif opcao == "0":
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")

def menu_inscricoes():
    init(autoreset=True)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        menu = [
            ["1", "Inscrever Time em Torneio"],
            ["2", "Listar Inscrições"],
            ["3", "Cancelar Inscrição"],
            ["0", "Voltar ao Menu Principal"]
        ]

        print(Fore.CYAN + Style.BRIGHT + "=== MENU INSCRIÇÕES ===")
        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()
        opcao = input(Fore.BLUE + "Escolha uma opção: ")

        if opcao == "1":
            inscrever_time()
            input(Fore.GREEN + "\nTime inscrito! Pressione Enter para continuar...")
        elif opcao == "2":
            listar_inscricoes()
            input(Fore.BLUE + "\nPressione Enter para continuar...")
        elif opcao == "3":
            cancelar_inscricao()
            input(Fore.YELLOW + "\nInscrição cancelada! Pressione Enter para continuar...")
        elif opcao == "0":
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")

def menu_relatorios():
    init(autoreset=True)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        exibir_menu()

        print(Fore.CYAN + Style.BRIGHT + "=== MENU RELATÓRIOS ===\n")

        menu = [
            ["1", "Relatório de Quantidades"],
            ["2", "Últimos Torneios"],
            ["3", "Jogos dos Torneios"],
            ["4", "Voltar ao Menu Principal"]
        ]

        print(Fore.MAGENTA + tabulate(menu, headers=["Opção", "Descrição"], tablefmt="fancy_grid"))
        print()

        opcao = input(Fore.BLUE + "Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            relatorio_quantidades()
            input(Fore.GREEN + "\nPressione Enter para continuar...")
        elif opcao == '2':
            ultimos_torneios()
            input(Fore.GREEN + "\nPressione Enter para continuar...")
        elif opcao == '3':
            jogos_dos_torneios()
            input(Fore.GREEN + "\nPressione Enter para continuar...")
        elif opcao == '4':
            break
        else:
            input(Fore.RED + "Opção inválida. Pressione Enter para continuar...")  

if __name__ == "__main__":
    menu_principal()
