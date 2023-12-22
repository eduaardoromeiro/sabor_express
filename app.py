# Biblioteca

import os

# Lista

restaurantes = [
    {"nome": "Restaurante 1", "categoria": "Massa", "ativo": False},
    {"nome": "Restaurante 2", "categoria": "Doces", "ativo": True},
    {"nome": "Restaurante 3", "categoria": "Japonesa", "ativo": True},
]


def exibir_nome():
    print(
        """
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░"""
    )

    print(
        "----------------------------------------------------------------------------------------------\n"
    )


def exibir_menu():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair")


def voltar_menu():
    input("Digite a tecla para voltar ao menu principal: ")
    main()


def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu()


def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja adicionar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante foi cadastrado com sucesso!\n")
    voltar_menu()


def listar_restaurante():
    exibir_subtitulo("Listar Restaurante")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"{nome_restaurante} | {categoria} | {ativo}")


def entrada_opcao():
    try:
        opcao_escolhida = int(input("\nEntre com uma opção: "))
        print(f"Opção escolhida: {opcao_escolhida}")

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                print("Ativar Restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

        # if opcao_escolhida == 1:
        #     print("Cadastrar Restaurante")
        # elif opcao_escolhida == 2:
        #     print("Listar Restaurante")
        # elif opcao_escolhida == 3:
        #     print("Ativar Restaurante")
        # else:
        #     finalizar_app()
    except:
        opcao_invalida()


# -------- Função --------

# -------- Condicionais: if-else, elif --------


def finalizar_app():
    exibir_subtitulo("Finalizando o programa...")


def main():
    os.system("clear")
    exibir_nome()
    exibir_menu()
    entrada_opcao()


if __name__ == "__main__":
    main()
