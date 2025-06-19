import os
from tabulate import tabulate

CAMINHO_INSCRICOES = "dados/inscricoes.txt"
CAMINHO_TIMES = "dados/times.txt"
CAMINHO_TORNEIOS = "dados/torneios.txt"

def ler_arquivo(caminho):
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return [linha.strip().split(";") for linha in arquivo if linha.strip()]

def salvar_inscricoes(inscricoes):
    with open(CAMINHO_INSCRICOES, "w", encoding="utf-8") as arquivo:
        for i in inscricoes:
            arquivo.write(";".join(i) + "\n")

def listar_inscricoes():
    inscricoes = ler_arquivo(CAMINHO_INSCRICOES)
    if not inscricoes:
        print("\nNenhuma inscrição encontrada.")
        return
    print("\nLista de Inscrições:")
    for i in inscricoes:
        print(f"Torneio ID: {i[0]} | Time ID: {i[1]}")

def inscrever_time():
    torneios = ler_arquivo(CAMINHO_TORNEIOS)
    times = ler_arquivo(CAMINHO_TIMES)
    inscricoes = ler_arquivo(CAMINHO_INSCRICOES)

    print("\nTorneios disponíveis:")
    for t in torneios:
        print(f"ID: {t[0]} - Nome: {t[1]}")
    id_torneio = input("Digite o ID do torneio: ")

    print("\nTimes disponíveis:")
    for t in times:
        print(f"ID: {t[0]} - Nome: {t[1]}")
    id_time = input("Digite o ID do time: ")

    for i in inscricoes:
        if i[0] == id_torneio and i[1] == id_time:
            print("Esse time já está inscrito nesse torneio.")
            return

    inscricoes.append([id_torneio, id_time])
    salvar_inscricoes(inscricoes)
    print("Inscrição realizada com sucesso.")

def cancelar_inscricao():
    inscricoes = ler_arquivo(CAMINHO_INSCRICOES)
    listar_inscricoes()
    id_torneio = input("Digite o ID do torneio da inscrição a remover: ")
    id_time = input("Digite o ID do time da inscrição a remover: ")

    nova_lista = [i for i in inscricoes if not (i[0] == id_torneio and i[1] == id_time)]

    if len(nova_lista) == len(inscricoes):
        print("Inscrição não encontrada.")
    else:
        salvar_inscricoes(nova_lista)
        print("Inscrição cancelada com sucesso.")

def menu_inscricoes():
    while True:
        print("\nMenu de Inscrições:")
        print("1. Inscrever time em torneio")
        print("2. Listar inscrições")
        print("3. Cancelar inscrição")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inscrever_time()
        elif opcao == "2":
            listar_inscricoes()
        elif opcao == "3":
            cancelar_inscricao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    inscrever_time()
