# Função para cadastrar livro
def cadastrar_livro():
    codigo = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário
    titulo = input("Digite o título do livro: ")  # Solicita o título do livro ao usuário
    autor = input("Digite o autor do livro: ")  # Solicita o autor do livro ao usuário
    ano_publicacao = input("Digite o ano de publicação do livro: ")  # Solicita o ano de publicação do livro ao usuário
    quant_exemplares = input("Digite a quantidade de exemplares do livro: ")  # Solicita a quantidade de exemplares do livro ao usuário

    linha_desejada = "Codigo|Titulo|Autor|Ano_publicacao|Quant_exemplares"  # Define a linha desejada no arquivo
    arquivo = "livros.txt"  # Define o nome do arquivo onde os livros serão cadastrados

    with open(arquivo, "a+") as arquivo_leitura:  # Abre o arquivo no modo de leitura e escrita, criando o arquivo se não existir
        arquivo_leitura.seek(0)  # Volta para o início do arquivo
        if linha_desejada not in arquivo_leitura.read():  # Verifica se a linha desejada já existe no arquivo
            arquivo_leitura.write(linha_desejada + "\n")  # Se não existir, escreve a linha desejada no arquivo

    with open(arquivo, "a") as arquivo_escrita:  # Abre o arquivo no modo de escrita, adicionando ao final do arquivo
        arquivo_escrita.write(f"{codigo}|{titulo}|{autor}|{ano_publicacao}|{quant_exemplares}\n")  # Escreve os dados do livro no arquivo

    print("Livro cadastrado com sucesso!")  # Exibe uma mensagem de sucesso ao usuário

# Função para cadastrar usuário
def cadastrar_usuario():
    codigo = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    nome = input("Digite o nome do usuário: ")  # Solicita o nome do usuário ao usuário
    email = input("Digite o email do usuário: ")  # Solicita o email do usuário ao usuário
    telefone = input("Digite o telefone do usuário: ")  # Solicita o telefone do usuário ao usuário

    # Formatando o telefone no formato desejado
    telefone_formatado = f"+55 {telefone[:2]} {telefone[2:7]} {telefone[7:]} "

    linha_desejada = "Codigo|Nome|Email|Telefone"  # Define a linha desejada no arquivo
    arquivo = "usuarios.txt"  # Define o nome do arquivo onde os usuários serão cadastrados

    with open(arquivo, "a+") as arquivo_leitura:  # Abre o arquivo no modo de leitura e escrita, criando o arquivo se não existir
        arquivo_leitura.seek(0)  # Volta para o início do arquivo
        if linha_desejada not in arquivo_leitura.read():  # Verifica se a linha desejada já existe no arquivo
            arquivo_leitura.write(linha_desejada + "\n")  # Se não existir, escreve a linha desejada no arquivo

    with open(arquivo, "a") as arquivo_escrita:  # Abre o arquivo no modo de escrita, adicionando ao final do arquivo
        arquivo_escrita.write(f"{codigo}    |{nome} |{email}|   {telefone_formatado}\n")  # Escreve os dados do usuário no arquivo

    print("Usuário cadastrado com sucesso!")  # Exibe uma mensagem de sucesso ao usuário

# Função para reservar um livro
def reservar_livro():
    codigo_reserva = input("Digite o código da reserva: ")  # Solicita o código da reserva ao usuário
    codigo_usuario = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    codigo_livro = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário
    data = input("Digite a data da reserva: ")  # Solicita a data da reserva ao usuário
    status = "Ativa"  # Define o status da reserva como "Ativa"

    linha_desejada = "Codigo  |Usuario    |Livro  |Data   |Status"  # Define a linha desejada no arquivo
    arquivo = "reservas.txt"  # Define o nome do arquivo onde as reservas serão registradas

    with open(arquivo, "a+") as arquivo_leitura:  # Abre o arquivo no modo de leitura e escrita, criando o arquivo se não existir
        arquivo_leitura.seek(0)  # Volta para o início do arquivo
        if linha_desejada not in arquivo_leitura.read():  # Verifica se a linha desejada já existe no arquivo
            arquivo_leitura.write(linha_desejada + "\n")  # Se não existir, escreve a linha desejada no arquivo

    with open(arquivo, "a") as arquivo_escrita:  # Abre o arquivo no modo de escrita, adicionando ao final do arquivo
        arquivo_escrita.write(f"{codigo_reserva}|   {codigo_usuario}|   {codigo_livro}| {data}| {status}\n")  # Escreve os dados da reserva no arquivo

    print("Reserva realizada com sucesso!")  # Exibe uma mensagem de sucesso ao usuário



# Função para devolver livro
def devolver_livro():
    codigo_reserva = input("Digite o código da reserva: ")  # Solicita o código da reserva ao usuário
    reservas = []  # Cria uma lista vazia para armazenar as reservas

    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    encontrou_reserva = False  # Variável para indicar se a reserva foi encontrada ou não

    with open("reservas.txt", "w") as arquivo:  # Abre o arquivo de reservas no modo de escrita, sobrescrevendo o arquivo existente
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_reserva[0] == codigo_reserva:  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário
                encontrou_reserva = True  # Marca que a reserva foi encontrada
                dados_reserva[4] = "Finalizada"  # Atualiza o status da reserva para "Finalizada"
                arquivo.write("|".join(dados_reserva) + "\n")  # Escreve os dados atualizados da reserva no arquivo
            else:
                arquivo.write(reserva)  # Escreve a reserva original no arquivo, sem alterações

    if encontrou_reserva:
        print("Livro devolvido com sucesso!")  # Exibe uma mensagem de sucesso se a reserva foi encontrada e atualizada
    else:
        print("Reserva não encontrada.")  # Exibe uma mensagem de erro se a reserva não foi encontrada

# Função para alterar livro
def alterar_livro():
    codigo_livro = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário
    livros = []  # Cria uma lista vazia para armazenar os livros

    with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    encontrou_livro = False  # Variável para indicar se o livro foi encontrado ou não

    with open("livros.txt", "w") as arquivo:  # Abre o arquivo de livros no modo de escrita, sobrescrevendo o arquivo existente
        for livro in livros:  # Itera sobre cada livro na lista de livros
            dados_livro = livro.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_livro[0] == codigo_livro:  # Verifica se o código do livro atual é igual ao código fornecido pelo usuário
                encontrou_livro = True  # Marca que o livro foi encontrado
                titulo = input("Digite o novo título do livro: ")  # Solicita o novo título do livro ao usuário
                autor = input("Digite o novo autor do livro: ")  # Solicita o novo autor do livro ao usuário
                ano_publicacao = input("Digite o novo ano de publicação do livro: ")  # Solicita o novo ano de publicação do livro ao usuário
                quant_exemplares = input("Digite a nova quantidade de exemplares do livro: ")  # Solicita a nova quantidade de exemplares do livro ao usuário
                dados_livro[1] = titulo  # Atualiza o título do livro
                dados_livro[2] = autor  # Atualiza o autor do livro
                dados_livro[3] = ano_publicacao  # Atualiza o ano de publicação do livro
                dados_livro[4] = quant_exemplares  # Atualiza a quantidade de exemplares do livro
                arquivo.write("|".join(dados_livro) + "\n")  # Escreve os dados atualizados do livro no arquivo
            else:
                arquivo.write(livro)  # Escreve o livro original no arquivo, sem alterações
                
    if encontrou_livro:
        print("Livro alterado com sucesso!")  # Exibe uma mensagem de sucesso se o livro foi encontrado e atualizado
    else:
        print("Livro não encontrado.")  # Exibe uma mensagem de erro se o livro não foi encontrado

# Função para alterar usuário
def alterar_usuario():
    codigo_usuario = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    usuarios = []  # Cria uma lista vazia para armazenar os usuários

    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    encontrou_usuario = False  # Variável para indicar se o usuário foi encontrado ou não

    with open("usuarios.txt", "w") as arquivo:  # Abre o arquivo de usuários no modo de escrita, sobrescrevendo o arquivo existente
        for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
            dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_usuario[0] == codigo_usuario:  # Verifica se o código do usuário atual é igual ao código fornecido pelo usuário
                encontrou_usuario = True  # Marca que o usuário foi encontrado
                nome = input("Digite o novo nome do usuário: ")  # Solicita o novo nome do usuário ao usuário
                email = input("Digite o novo e-mail do usuário: ")  # Solicita o novo e-mail do usuário ao usuário
                telefone = input("Digite o novo telefone do usuário: ")  # Solicita o novo telefone do usuário ao usuário
                dados_usuario[1] = nome  # Atualiza o nome do usuário
                dados_usuario[2] = email  # Atualiza o e-mail do usuário
                dados_usuario[3] = telefone  # Atualiza o telefone do usuário
                arquivo.write("|".join(dados_usuario) + "\n")  # Escreve os dados atualizados do usuário no arquivo
            else:
                arquivo.write(usuario)  # Escreve o usuário original no arquivo, sem alterações

    if encontrou_usuario:
        print("Usuário alterado com sucesso!")  # Exibe uma mensagem de sucesso se o usuário foi encontrado e atualizado
    else:
        print("Usuário não encontrado.")  # Exibe uma mensagem de erro se o usuário não foi encontrado


# Função para remover livro
def remover_livro():
    codigo_livro = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário
    livros = []  # Cria uma lista vazia para armazenar os livros

    with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    encontrou_livro = False  # Variável para indicar se o livro foi encontrado ou não

    with open("livros.txt", "w") as arquivo:  # Abre o arquivo de livros no modo de escrita, sobrescrevendo o arquivo existente
        for livro in livros:  # Itera sobre cada livro na lista de livros
            dados_livro = livro.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_livro[0] == codigo_livro:  # Verifica se o código do livro atual é igual ao código fornecido pelo usuário
                encontrou_livro = True  # Marca que o livro foi encontrado e será removido
            else:
                arquivo.write(livro)  # Escreve o livro no arquivo, exceto o livro que será removido

    if encontrou_livro:
        print("Livro removido com sucesso!")  # Exibe uma mensagem de sucesso se o livro foi encontrado e removido
    else:
        print("Livro não encontrado.")  # Exibe uma mensagem de erro se o livro não foi encontrado

# Função para remover usuário
def remover_usuario():
    codigo_usuario = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    usuarios = []  # Cria uma lista vazia para armazenar os usuários

    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    encontrou_usuario = False  # Variável para indicar se o usuário foi encontrado ou não

    with open("usuarios.txt", "w") as arquivo:  # Abre o arquivo de usuários no modo de escrita, sobrescrevendo o arquivo existente
        for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
            dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_usuario[0] == codigo_usuario:  # Verifica se o código do usuário atual é igual ao código fornecido pelo usuário
                encontrou_usuario = True  # Marca que o usuário foi encontrado e será removido
            else:
                arquivo.write(usuario)  # Escreve o usuário no arquivo, exceto o usuário que será removido

    if encontrou_usuario:
        print("Usuário removido com sucesso!")  # Exibe uma mensagem de sucesso se o usuário foi encontrado e removido
    else:
        print("Usuário não encontrado.")  # Exibe uma mensagem de erro se o usuário não foi encontrado

# Função para remover reserva
def remover_reserva():
    codigo_reserva = input("Digite o código da reserva: ")  # Solicita o código da reserva ao usuário
    reservas = []  # Cria uma lista vazia para armazenar as reservas

    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    encontrou_reserva = False  # Variável para indicar se a reserva foi encontrada ou não

    with open("reservas.txt", "w") as arquivo:  # Abre o arquivo de reservas no modo de escrita, sobrescrevendo o arquivo existente
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_reserva[0] == codigo_reserva:  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário
                encontrou_reserva = True  # Marca que a reserva foi encontrada e será removida
            else:
                arquivo.write(reserva)  # Escreve a reserva no arquivo, exceto a reserva que será removida

    if encontrou_reserva:
        print("Reserva removida com sucesso!")  # Exibe uma mensagem de sucesso se a reserva foi encontrada e removida
    else:
        print("Reserva não encontrada.")  # Exibe uma mensagem de erro se a reserva não foi encontrada

# Função para pesquisar livros
def pesquisar_livros():
    codigo_livro = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário
    livros = []  # Cria uma lista vazia para armazenar os livros

    with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    encontrado = False  # Variável para indicar se o livro foi encontrado ou não

    for livro in livros:  # Itera sobre cada livro na lista de livros
        dados_livro = livro.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
        if dados_livro[0] == codigo_livro:  # Verifica se o código do livro atual é igual ao código fornecido pelo usuário
            print("Livro encontrado:")
            print(f"Código: {dados_livro[0]}")
            print(f"Título: {dados_livro[1]}")
            print(f"Autor: {dados_livro[2]}")
            print(f"Ano de Publicação: {dados_livro[3]}")
            print(f"Quantidade de Exemplares: {dados_livro[4]}")
            encontrado = True
            break

    if not encontrado:
        print("Livro não encontrado.")  # Exibe uma mensagem de erro se o livro não foi encontrado

# Função para pesquisar usuários
def pesquisar_usuarios():
    codigo_usuario = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    usuarios = []  # Cria uma lista vazia para armazenar os usuários

    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    encontrado = False  # Variável para indicar se o usuário foi encontrado ou não

    for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
        dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
        if dados_usuario[0] == codigo_usuario:  # Verifica se o código do usuário atual é igual ao código fornecido pelo usuário
            print("Usuário encontrado:")
            print(f"Código: {dados_usuario[0]}")
            print(f"Nome: {dados_usuario[1]}")
            print(f"E-mail: {dados_usuario[2]}")
            print(f"Telefone: {dados_usuario[3]}")
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")  # Exibe uma mensagem de erro se o usuário não foi encontrado

# Função para pesquisar reservas
def pesquisar_reservas():
    codigo_reserva = input("Digite o código da reserva: ")  # Solicita o código da reserva ao usuário
    reservas = []  # Cria uma lista vazia para armazenar as reservas

    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    encontrado = False  # Variável para indicar se a reserva foi encontrada ou não

    for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
        dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
        if dados_reserva[0] == codigo_reserva:  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário
            print("Reserva encontrada:")
            print(f"Código: {dados_reserva[0]}")
            print(f"Usuário: {dados_reserva[1]}")
            print(f"Livro: {dados_reserva[2]}")
            print(f"Data: {dados_reserva[3]}")
            print(f"Status: {dados_reserva[4]}")
            encontrado = True
            break

    if not encontrado:
        print("Reserva não encontrada.")  # Exibe uma mensagem de erro se a reserva não foi encontrada

def menu_pesquisa():
    while True:
        print("\n------------------------------")
        print("------------------------------\n")
        print("=== Menu de Pesquisa ===")
        print("1. Pesquisar livros")
        print("2. Pesquisar usuários")
        print("3. Pesquisar reservas")
        print("4. Voltar")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            pesquisar_livros()

        elif opcao == "2":
            pesquisar_usuarios()

        elif opcao == "3":
            pesquisar_reservas()

        elif opcao == "4":
            break

        else:
            print("Opção inválida. Tente novamente.")

# Função para listar usuários
def listar_livros():
    with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    if livros:
        print("Lista de livros:")
        for livro in livros:  # Itera sobre cada livro na lista de livros
            dados_livro = livro.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            codigo = dados_livro[0]  # Obtém o código do livro
            titulo = dados_livro[1]  # Obtém o título do livro
            autor = dados_livro[2]  # Obtém o autor do livro
            ano_publicacao = dados_livro[3]  # Obtém o ano de publicação do livro
            quant_exemplares = dados_livro[4]  # Obtém a quantidade de exemplares do livro
            print(f"{codigo} | {titulo} | {autor} | {ano_publicacao} | {quant_exemplares}")  # Exibe os dados do livro formatados
        print("\n"*2)  # Exibe linhas em branco para separar as informações na saída
    else:
        print("Não há livros cadastrados.")  # Exibe uma mensagem se não houver livros cadastrados


def listar_usuarios():
    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    if usuarios:
        print("Lista de usuários:")
        for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
            dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            codigo = dados_usuario[0]  # Obtém o código do usuário
            nome = dados_usuario[1]  # Obtém o nome do usuário
            email = dados_usuario[2]  # Obtém o e-mail do usuário
            telefone = dados_usuario[3]  # Obtém o telefone do usuário
            print(f"{codigo} | {nome} | {email} | {telefone}")  # Exibe os dados do usuário formatados
        print("\n"*2)  # Exibe linhas em branco para separar as informações na saída
    else:
        print("Não há usuários cadastrados.")  # Exibe uma mensagem se não houver usuários cadastrados


def listar_reservas():
    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    if reservas:
        print("Lista de reservas:")
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            codigo = dados_reserva[0]  # Obtém o código da reserva
            usuario = dados_reserva[1]  # Obtém o usuário da reserva
            livro = dados_reserva[2]  # Obtém o livro da reserva
            data = dados_reserva[3]  # Obtém a data da reserva
            status = dados_reserva[4]  # Obtém o status da reserva
            print(f"{codigo} | {usuario} | {livro} | {data} | {status}")  # Exibe os dados da reserva formatados
        print("\n"*2)  # Exibe linhas em branco para separar as informações na saída
    else:
        print("Não há reservas cadastradas.")  # Exibe uma mensagem se não houver reservas cadastradas


def listar_reservas_finalizadas():
    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    if reservas:
        print("Lista de reservas finalizadas:")
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_reserva[4] == "Finalizada":  # Verifica se o status da reserva é "Finalizada"
                codigo = dados_reserva[0]  # Obtém o código da reserva
                usuario = dados_reserva[1]  # Obtém o usuário da reserva
                livro = dados_reserva[2]  # Obtém o livro da reserva
                data = dados_reserva[3]  # Obtém a data da reserva
                status = dados_reserva[4]  # Obtém o status da reserva
                print(f"{codigo} | {usuario} | {livro} | {data} | {status}")  # Exibe os dados da reserva formatados
        print("\n"*2)  # Exibe linhas em branco para separar as informações na saída
    else:
        print("Não há reservas finalizadas.")  # Exibe uma mensagem se não houver reservas cadastradas


# Função para listar reservas ativas
def listar_reservas_ativas():
    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    if reservas:
        print("Lista de reservas ativas:")
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_reserva[4].strip() == "Ativa":  # Verifica se o status da reserva é "Ativa"  
                codigo = dados_reserva[0]  # Obtém o código da reserva
                usuario = dados_reserva[1]  # Obtém o usuário da reserva
                livro = dados_reserva[2]  # Obtém o livro da reserva
                data = dados_reserva[3]  # Obtém a data da reserva
                status = dados_reserva[4]  # Obtém o status da reserva
                print(f"{codigo} | {usuario} | {livro} | {data} | {status}")  # Exibe os dados da reserva formatados
        print("\n"*2)  # Exibe linhas em branco para separar as informações na saída
    else:
        print("Nenhuma reserva ativa encontrada.")  # Exibe uma mensagem se não houver reservas cadastradas

#função para remover 
def remover():
    while True:
        print("\n------------------------------")
        print("------------------------------\n")
        print("=== Remover ===")
        print("1. Remover livro")
        print("2. Remover usuário")
        print("3. Remover reserva")
        print("4. Voltar")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            remover_livro()
        elif opcao == "2":
            remover_usuario()
        elif opcao == "3":
            remover_reserva()
        elif opcao == "4":
            print("Voltando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#função listagem
def listagem():
    while True:
        print("\n------------------------------")
        print("------------------------------\n")
        print("=== Menu de Listagem ===")
        print("1. Listar livros")
        print("2. Listar usuários")
        print("3. Listar reservas")
        print("4. Listar reservas ativas")
        print("5. Listar reservas finalizadas")
        print("6. Voltar")
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            listar_reservas()
        elif opcao == "4":
            listar_reservas_ativas()
        elif opcao == "5":
            listar_reservas_finalizadas()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para gerar relatório
def gerar_relatorio():
    with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    total_livros = len(livros)  # Calcula o total de livros cadastrados
    total_usuarios = len(usuarios)  # Calcula o total de usuários cadastrados
    total_reservas = len(reservas)  # Calcula o total de reservas realizadas
    total_reservas_ativas = 0  # Inicializa o contador de reservas ativas
    total_reservas_finalizadas = 0  # Inicializa o contador de reservas finalizadas

    for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
        dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
        if dados_reserva[4] == "Ativa":  # Verifica se o status da reserva é "Ativa"
            total_reservas_ativas += 1  # Incrementa o contador de reservas ativas
        elif dados_reserva[4] == "Finalizada":  # Verifica se o status da reserva é "Finalizada"
            total_reservas_finalizadas += 1  # Incrementa o contador de reservas finalizadas

    print("Relatório:")
    print(f"Total de livros cadastrados: {total_livros}")  # Exibe o total de livros cadastrados
    print(f"Total de usuários cadastrados: {total_usuarios}")  # Exibe o total de usuários cadastrados
    print(f"Total de reservas realizadas: {total_reservas}")  # Exibe o total de reservas realizadas
    print(f"Total de reservas ativas: {total_reservas_ativas}")  # Exibe o total de reservas ativas
    print(f"Total de reservas finalizadas: {total_reservas_finalizadas}")  # Exibe o total de reservas finalizadas


# Função principal
def main():
    while True:
        print("\n")
        print("======= MENU =======")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Reservar livro")
        print("4. Devolver livro")
        print("5. Alterar livro")
        print("6. Alterar usuário")
        print("7. Remover ")
        print("8. Pesquisar")
        print("9. listagem")
        print("10. gerar relatorio")
        print("0. Encerrar programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastrar_livro() # Chama a função para cadastrar um livro
        elif opcao == "2":
            cadastrar_usuario()  # Chama a função para cadastrar um usuario
        elif opcao == "3":
            reservar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            alterar_livro()
        elif opcao == "6":
            alterar_usuario()
        elif opcao == "7":
            remover()
        elif opcao == "8":
            menu_pesquisa()
        elif opcao == "9":
            listagem()
        elif opcao == "10":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")

if __name__ == "__main__":
    main()
    
   
