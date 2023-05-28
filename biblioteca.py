<<<<<<< HEAD

livros = []
usuarios = []
reservas = []

def cadastrar_livro():
    codigo = int(input("Digite o codigo do livro: "))
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    quantidade = float(input("Digite a quantidade de exemplares: "))
    livro = {
        "codigo": codigo,
        "título": titulo,
        "autor": autor,
        "ano": ano,
        "quantidade":quantidade
    }
    livros.append(livro)
    print("Livro cadastrado com sucesso!")


def cadastrar_usuario():
    codigo = int(input("Digite codigo do usuário: "))
    nome = input("Digite o nome do usuário: ")
    usuario = {
        "codigo": codigo,
        "nome": nome,
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def cadastrar_reserva():
    codigo_reserva = int(input("Digite o codigo da reserva: "))
    codigo_usuario = int(input("Digite o codigo do usuário: "))
    codigo_livro = int(input("Digite o codigo do livro: "))
    reserva = {
        "codigo": codigo_reserva,
        "codigo_usuario": codigo_usuario,
        "codigo_livro": codigo_livro
    }
    reservas.append(reserva)
    print("Reserva cadastrada com sucesso!")


def devolver_livro(): 
 pass
def alterar_informacoes_livro():
    pass
def alterar_informacoes_usuario():
    pass
def alterar_informacoes_reserva():

 pass

def remover_livro():
    codigo_livro = int(input("Digite o codigo do livro que deseja remover: "))
    for livro in livros:
        if livro["codigo"] == codigo_livro:
            livros.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado.")


def remover_usuario():
    codigo_usuario = int(input("Digite o codigo do usuário que deseja remover: "))
    for usuario in usuarios:
        if usuario["codigo"] == codigo_usuario:
            usuarios.remove(usuario)
            print("Usuário removido com sucesso!")
            return
    print("Usuário não encontrado.")


def remover_reserva():
    codigo_reserva = int(input("Digite o codigo da reserva que deseja remover: "))
    for reserva in reservas:
        if reserva["codigo"] == codigo_reserva:
            reservas.remove(reserva)
            print("Reserva removida com sucesso!")
            return
    print("Reserva não encontrada.")


def pesquisar_livro():
 pass

def pesquisar_usuario():
 pass

def pesquisar_reserva():
 pass
def listar_usuarios():

 pass
def listar_livros():
    print("Lista de livros:")
    for livro in livros:
        print(f"codigo: {livro['codigo']}")
        print(f"Título: {livro['título']}")
        print(f"Autor: {livro['autor']}")
        print(f"ano: {livro['ano']}")
        print(f"quantidade exemplares: {livro['quantidade']}")
        print()


def listar_reservas():
    print("Lista de reservas:")
    for reserva in reservas:
        print(f"codigo da reserva: {reserva['codigo']}")
        print(f"codigo do Usuário: {reserva['codigo_usuario']}")
        print(f"codigo do Livro: {reserva['codigo_livro']}")
        print()


def listar_reservas_ativas():
 pass

def listar_reservas_finalizadas():
  pass

def gerar_relatorio():
    print("Relatório:")
    print(f"Total de livros: {len(livros)}")
    print(f"Total de usuários: {len(usuarios)}")
    print(f"Total de reservas: {len(reservas)}")
    print()


def encerrar_programa():
    print("Programa encerrado.")


def menu():
    while True:
        print("--- Sistema de Biblioteca ---")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Usuário")
        print("3 - Cadastrar Reserva")
        print("4 - Devolver Livro")
        print("5 - Alterar Informações de Livro")
        print("6 - Alterar Informações de Usuário")
        print("7 - Alterar Informações de Reserva")
        print("8 - Remover Livro")
        print("9 - Remover Usuário")
        print("10 - Remover Reserva")
        print("11 - Pesquisar Livros")
        print("12 - Pesquisar Usuários")
        print("13 - Pesquisar Reservas")
        print("14 - Listar Todos os Usuários")
        print("15 - Listar Todos os Livros")
        print("16 - Listar Todas as Reservas")
        print("17 - Listar Reservas Ativas")
        print("18 - Listar Reservas Finalizadas")
        print("19 - Gerar Relatório")
        print("0 - Encerrar Programa")
        opcao = input("Digite a opção desejada: ")


        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            cadastrar_reserva()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            alterar_informacoes_livro()
        elif opcao == "6":
            alterar_informacoes_usuario()
        elif opcao == "7":
            alterar_informacoes_reserva()
        elif opcao == "8":
            remover_livro()
        elif opcao == "9":
            remover_usuario()
        elif opcao == "10":
            remover_reserva()
        elif opcao == "11":
            pesquisar_livro()
        elif opcao == "12":
            pesquisar_usuario()
        elif opcao == "13":
            pesquisar_reserva()
        elif opcao == "14":
            listar_usuarios()
        elif opcao == "15":
            listar_livros()
        elif opcao == "16":
            listar_reservas()
        elif opcao == "17":
            listar_reservas_ativas()
        elif opcao == "18":
            listar_reservas_finalizadas()
        elif opcao == "19":
            gerar_relatorio()
        elif opcao == "0":
            encerrar_programa()
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()



=======
#teste
print("Função que descobre o mundo!")
>>>>>>> b378a72e8ed95b3fa66f0f232d830d36f6934886
