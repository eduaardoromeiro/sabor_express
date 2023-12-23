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
    print("3. Alternar Restaurante")
    print("4. Sair")


def voltar_menu():
    input("Digite a tecla para voltar ao menu principal: ")
    main()


def exibir_subtitulo(texto):
    os.system("clear")
    linha = '*' * (len(texto) + 4)
    print(linha)
    print()
    print(texto)
    print()
    print(linha)
    print()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_menu()


def cadastrar_restaurante():
    '''
    Função que serve para cadastrar um restaurante

    Inputs:
        - Nome do restaurante
        - Categoria

    Outputs:
        - Adiciona um novo restaurante na lista
    '''

    exibir_subtitulo("Cadastro de restaurante")

    nome_restaurante = input(
        "Digite o nome do restaurante que deseja adicionar: ")
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {"nome": nome_restaurante,
                         "categoria": categoria, "ativo": True}

    restaurantes.append(dados_restaurante)
    print(f"O restaurante foi cadastrado com sucesso!\n")
    voltar_menu()


def alternar_estado():
    exibir_subtitulo("Alterando o estado atual do restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'ativo'] else f'O restaurante foi desativado com sucesso'
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    print(mensagem, "\n")
    voltar_menu()


def listar_restaurante():
    exibir_subtitulo("Listar Restaurante")

    print(f"{'Nome do resturante'.ljust(20)} | {'Categoria'.ljust(20)} | Status")
    print("--------------------------------------------------------------------")
    print()
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    print()
    voltar_menu()


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
                alternar_estado()
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
