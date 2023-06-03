# Função para cadastrar livro
def cadastrar_livro():
    codigo = input("Digite o código do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    quant_exemplares = input("Digite a quantidade de exemplares do livro: ")

    with open("livros.txt", "a") as arquivo:
        arquivo.write(f"Codigo|Titulo|Autor|Ano_publicacao|Quant_exemplares\n")
        arquivo.write(f"{codigo}|{titulo}|{autor}|{ano_publicacao}|{quant_exemplares}\n")

    print("Livro cadastrado com sucesso!")

# Função para cadastrar usuário
def cadastrar_usuario():
    codigo = input("Digite o código do usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    telefone = input("Digite o telefone do usuário: ")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"Codigo|Nome|Email|Telefone\n")
        arquivo.write(f"{codigo}|{nome}|{email}|{telefone}\n")

    print("Usuário cadastrado com sucesso!")

# Função para reservar um livro
def reservar_livro():
    codigo_reserva = input("Digite o código da reserva: ")
    codigo_usuario = input("Digite o código do usuário: ")
    codigo_livro = input("Digite o código do livro: ")
    data = input("Digite a data da reserva: ")
    status = "Ativa"

    with open("reservas.txt", "a") as arquivo:
        arquivo.write(f"Codigo|Usuario|Livro|Data|Status\n")
        arquivo.write(f"{codigo_reserva}|{codigo_usuario}|{codigo_livro}|{data}|{status}\n")

    print("Reserva realizada com sucesso!")


# Função para devolver livro
def devolver_livro():
    codigo_reserva = input("Digite o código da reserva: ")
    reservas = []

    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    encontrou_reserva = False

    with open("reservas.txt", "w") as arquivo:
        for reserva in reservas:
            dados_reserva = reserva.strip().split("|")
            if dados_reserva[0] == codigo_reserva:
                encontrou_reserva = True
                dados_reserva[4] = "Finalizada"
                arquivo.write("|".join(dados_reserva) + "\n")
            else:
                arquivo.write(reserva)

    if encontrou_reserva:
        print("Livro devolvido com sucesso!")
    else:
        print("Reserva não encontrada.")

# Função para alterar livro
def alterar_livro():
    codigo_livro = input("Digite o código do livro: ")
    livros = []

    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    encontrou_livro = False

    with open("livros.txt", "w") as arquivo:
        for livro in livros:
            dados_livro = livro.strip().split("|")
            if dados_livro[0] == codigo_livro:
                encontrou_livro = True
                titulo = input("Digite o novo título do livro: ")
                autor = input("Digite o novo autor do livro: ")
                ano_publicacao = input("Digite o novo ano de publicação do livro: ")
                quant_exemplares = input("Digite a nova quantidade de exemplares do livro: ")
                dados_livro[1] = titulo
                dados_livro[2] = autor
                dados_livro[3] = ano_publicacao
                dados_livro[4] = quant_exemplares
                arquivo.write("|".join(dados_livro) + "\n")
            else:
                arquivo.write(livro)

    if encontrou_livro:
        print("Livro alterado com sucesso!")
    else:
        print("Livro não encontrado.")

# Função para alterar usuário
def alterar_usuario():
    codigo_usuario = input("Digite o código do usuário: ")
    usuarios = []

    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    encontrou_usuario = False

    with open("usuarios.txt", "w") as arquivo:
        for usuario in usuarios:
            dados_usuario = usuario.strip().split("|")
            if dados_usuario[0] == codigo_usuario:
                encontrou_usuario = True
                nome = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo e-mail do usuário: ")
                telefone = input("Digite o novo telefone do usuário: ")
                dados_usuario[1] = nome
                dados_usuario[2] = email
                dados_usuario[3] = telefone
                arquivo.write("|".join(dados_usuario) + "\n")
            else:
                arquivo.write(usuario)

    if encontrou_usuario:
        print("Usuário alterado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função para remover livro
def remover_livro():
    codigo_livro = input("Digite o código do livro: ")
    livros = []

    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    encontrou_livro = False

    with open("livros.txt", "w") as arquivo:
        for livro in livros:
            dados_livro = livro.strip().split("|")
            if dados_livro[0] == codigo_livro:
                encontrou_livro = True
            else:
                arquivo.write(livro)

    if encontrou_livro:
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")

# Função para remover usuário
def remover_usuario():
    codigo_usuario = input("Digite o código do usuário: ")
    usuarios = []

    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    encontrou_usuario = False

    with open("usuarios.txt", "w") as arquivo:
        for usuario in usuarios:
            dados_usuario = usuario.strip().split("|")
            if dados_usuario[0] == codigo_usuario:
                encontrou_usuario = True
            else:
                arquivo.write(usuario)

    if encontrou_usuario:
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função para remover reserva
def remover_reserva():
    codigo_reserva = input("Digite o código da reserva: ")
    reservas = []

    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    encontrou_reserva = False

    with open("reservas.txt", "w") as arquivo:
        for reserva in reservas:
            dados_reserva = reserva.strip().split("|")
            if dados_reserva[0] == codigo_reserva:
                encontrou_reserva = True
            else:
                arquivo.write(reserva)

    if encontrou_reserva:
        print("Reserva removida com sucesso!")
    else:
        print("Reserva não encontrada.")

# Função para pesquisar livros
def pesquisar_livros():
    codigo_livro = input("Digite o código do livro: ")
    livros = []

    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    encontrado = False

    for livro in livros:
        dados_livro = livro.strip().split("|")
        if dados_livro[0] == codigo_livro:
            print("Livro encontrado:")
            print(f"Código: {dados_livro[0]}")
            print(f"Título: {dados_livro[1]}")
            print(f"Autor: {dados_livro[2]}")
            print(f"Ano de Publicação: {dados_livro[3]}")
            print(f"Quantidade de Exemplares: {dados_livro[4]}")
            encontrado = True
            break

    if not encontrado:
        print("Livro não encontrado.")

# Função para pesquisar usuários
def pesquisar_usuarios():
    codigo_usuario = input("Digite o código do usuário: ")
    usuarios = []

    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    encontrado = False

    for usuario in usuarios:
        dados_usuario = usuario.strip().split("|")
        if dados_usuario[0] == codigo_usuario:
            print("Usuário encontrado:")
            print(f"Código: {dados_usuario[0]}")
            print(f"Nome: {dados_usuario[1]}")
            print(f"E-mail: {dados_usuario[2]}")
            print(f"Telefone: {dados_usuario[3]}")
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")

# Função para pesquisar reservas
def pesquisar_reservas():
    codigo_reserva = input("Digite o código da reserva: ")
    reservas = []

    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    encontrado = False

    for reserva in reservas:
        dados_reserva = reserva.strip().split("|")
        if dados_reserva[0] == codigo_reserva:
            print("Reserva encontrada:")
            print(f"Código: {dados_reserva[0]}")
            print(f"Usuário: {dados_reserva[1]}")
            print(f"Livro: {dados_reserva[2]}")
            print(f"Data: {dados_reserva[3]}")
            print(f"Status: {dados_reserva[4]}")
            encontrado = True
            break

    if not encontrado:
        print("Reserva não encontrada.")

# Função para listar usuários
def listar_livros():
    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    if livros:
        print("Lista de livros:")
        print("Código | Título | Autor | Ano de Publicação | Quantidade de Exemplares")
        for livro in livros:
            dados_livro = livro.strip().split("|")
            codigo = dados_livro[0]
            titulo = dados_livro[1]
            autor = dados_livro[2]
            ano_publicacao = dados_livro[3]
            quant_exemplares = dados_livro[4]
            print(f"{codigo} | {titulo} | {autor} | {ano_publicacao} | {quant_exemplares}")
        print("\n"*2)
    else:
        print("Não há livros cadastrados.")

def listar_usuarios():
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    if usuarios:
        print("Lista de usuários:")
        print("Código | Nome | E-mail | Telefone")
        for usuario in usuarios:
            dados_usuario = usuario.strip().split("|")
            codigo = dados_usuario[0]
            nome = dados_usuario[1]
            email = dados_usuario[2]
            telefone = dados_usuario[3]
            print(f"{codigo} | {nome} | {email} | {telefone}")
        print("\n"*2)
    else:
        print("Não há usuários cadastrados.")

def listar_reservas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    if reservas:
        print("Lista de reservas:")
        print("Código | Usuário | Livro | Data | Status")
        for reserva in reservas:
            dados_reserva = reserva.strip().split("|")
            codigo = dados_reserva[0]
            usuario = dados_reserva[1]
            livro = dados_reserva[2]
            data = dados_reserva[3]
            status = dados_reserva[4]
            print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
        print("\n"*2)
    else:
        print("Não há reservas cadastradas.")

def listar_reservas_finalizadas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    if reservas:
        print("Lista de reservas finalizadas:")
        print("Código | Usuário | Livro | Data | Status")
        for reserva in reservas:
            dados_reserva = reserva.strip().split("|")
            if dados_reserva[4] == "Finalizada":
                codigo = dados_reserva[0]
                usuario = dados_reserva[1]
                livro = dados_reserva[2]
                data = dados_reserva[3]
                status = dados_reserva[4]
                print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
        print("\n"*2)
    else:
        print("Não há reservas finalizadas.")

# Função para listar reservas ativas
def listar_reservas_ativas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    if reservas:
        print("Lista de reservas ativas:")
        print("Código | Usuário | Livro | Data | Status")
        for reserva in reservas:
            dados_reserva = reserva.strip().split("|")
            if dados_reserva[4] == "Ativa":
                codigo = dados_reserva[0]
                usuario = dados_reserva[1]
                livro = dados_reserva[2]
                data = dados_reserva[3]
                status = dados_reserva[4]
                print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
        print("\n"*2)
    else:
        print("Nenhuma reserva ativa encontrada.")

# Função para gerar relatório
def gerar_relatorio():
    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    total_livros = len(livros)
    total_usuarios = len(usuarios)
    total_reservas = len(reservas)
    total_reservas_ativas = 0
    total_reservas_finalizadas = 0

    for reserva in reservas:
        dados_reserva = reserva.strip().split("|")
        if dados_reserva[4] == "Ativa":
            total_reservas_ativas += 1
        elif dados_reserva[4] == "Finalizada":
            total_reservas_finalizadas += 1

    print("Relatório:")
    print(f"Total de livros cadastrados: {total_livros}")
    print(f"Total de usuários cadastrados: {total_usuarios}")
    print(f"Total de reservas realizadas: {total_reservas}")
    print(f"Total de reservas ativas: {total_reservas_ativas}")
    print(f"Total de reservas finalizadas: {total_reservas_finalizadas}")

# Função principal
def main():
    while True:
        print("======= MENU =======")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Reservar livro")
        print("4. Devolver livro")
        print("5. Alterar livro")
        print("6. Alterar usuário")
        print("7. Remover livro")
        print("8. Remover usuário")
        print("9. Remover reserva")
        print("10. Pesquisar livros")
        print("11. Pesquisar usuários")
        print("12. Pesquisar reservas")
        print("13. Listar usuários")
        print("14. Listar livros")
        print("15. Listar reservas")
        print("16. Listar reservas ativas")
        print("17. Listar reservas finalizadas")
        print("18. Gerar relatório")
        print("19. Encerrar programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            reservar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            alterar_livro()
        elif opcao == "6":
            alterar_usuario()
        elif opcao == "7":
            remover_livro()
        elif opcao == "8":
            remover_usuario()
        elif opcao == "9":
            remover_reserva()
        elif opcao == "10":
            pesquisar_livros()
        elif opcao == "11":
            pesquisar_usuarios()
        elif opcao == "12":
            pesquisar_reservas()
        elif opcao == "13":
            listar_usuarios()
        elif opcao == "14":
            listar_livros()
        elif opcao == "15":
            listar_reservas()
        elif opcao == "16":
            listar_reservas_ativas()
        elif opcao == "17":
            listar_reservas_finalizadas()
        elif opcao == "18":
            gerar_relatorio()
        elif opcao == "19":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")

if __name__ == "__main__":
    main()

