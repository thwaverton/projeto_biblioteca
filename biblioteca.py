#Isso permite que você utilize os recursos relacionados a datas  fornecidos pela biblioteca datetime .
from datetime import datetime # importa a classe datetime do módulo datetime
import os  # Importa a biblioteca 'os', que possui várias funções, mas neste caso é usada para limpar o terminal toda vez que o menu for executado.

def limpar():  # Define a função 'limpar' para limpar o terminal e deixá-lo mais organizado.
 os.system("cls")  # Chama a função 'system' do módulo 'os' para executar o comando "cls", que limpa o terminal no Windows.

# Função para verificar se o arquivo está vazio e, caso esteja, adiciona o nome das categorias
def arquivo_vazio(arquivo):
    with open(arquivo, "r") as leitura:  # Abre o arquivo especificado em modo de leitura
        conteudo = leitura.read()  # Lê o conteúdo do arquivo e o armazena na variável 'conteudo'
        return len(conteudo) == 0  # Retorna True se o tamanho do conteúdo for igual a zero, indicando que o arquivo está vazio
    #resumo essa função e para verificar se existe cabeçalho 
def codigo_existente(arquivo, codigo):
    with open(arquivo, "r") as arquivo_leitura:
        # Verifica se o código já existe no arquivo
        for linha in arquivo_leitura:
            campos = linha.strip().split("|")
            if campos[0] == codigo:
                return True
    return False
# Função para cadastrar um livro
def cadastrar_livro():
    arquivo =  open("livros.txt","a")
    while True: # enquanto fou verdade
        codigo = input("\nDigite o código do Livro: ") #solicitar ao usuario o codigo
        if codigo_existente("livros.txt", codigo): # chama a função para verificar se o codigo do usuario ja esta em uso
            print("--------------------------------\nO código já está em uso. Insira um código diferente.") #exibir mensagem
        else:
            break # sai do loop se o codigo nao existir
    # Solicita ao usuário que digite o código do livro e o armazena na variável 'codigo'
    titulo = input("Digite o título do livro: ")  
    # Solicita ao usuário que digite o título do livro e o armazena na variável 'titulo'
    autor = input("Digite o autor do livro: ")  
    # Solicita ao usuário que digite o autor do livro e o armazena na variável 'autor'
    ano_publicacao = input("Digite o ano de publicação do livro: ")  
    # Solicita ao usuário que digite o ano de publicação do livro e o armazena na variável 'ano_publicacao'
    quant_exemplares = input("Digite a quantidade de exemplares do livro: ")  
    # Solicita ao usuário que digite a quantidade de exemplares do livro e a armazena na variável 'quant_exemplares'
    arquivo = "livros.txt"  # Define o nome do arquivo como "livros.txt"

    if arquivo_vazio(arquivo):  # Verifica se o arquivo está vazio chamando a função 'arquivo_vazio' com o nome do arquivo como argumento
        with open(arquivo, "w+") as leitura:  # Abre o arquivo especificado em modo de anexo ("w+")
            leitura.write("codigo|titulo|autor|ano_publicacao|quant_exemplares\n")  # Escreve o cabeçalho das colunas no arquivo, separado por '|'
   
    with open(arquivo, "r") as leitura:  # Abre o arquivo especificado em modo de leitura ("r")
        livros = leitura.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista chamada 'livros'

    for linha in livros[1:]:  # Percorre todas as linhas da lista 'livros', começando a partir da segunda linha (índice 1)
        livro_info = linha.strip().split("|")  # Remove os espaços em branco e quebras de linha da linha atual e divide os elementos pelo caractere "|"
        if livro_info[0] == codigo:  # Verifica se o código do livro atual é igual ao código informado pelo usuário
            print("-------------------------\nLivro já está cadastrado.\n-------------------------")
            return  
    with open(arquivo, "a") as leitura:  # Abre o arquivo especificado em modo de anexo ("a")
        leitura.write(f"{codigo}|{titulo}|{autor}|{ano_publicacao}|{quant_exemplares}\n")  # Escreve os dados do livro no arquivo, separados por '|'
        #estao separasos por chaves as variaveis mais o valores digitado pelo usuario irao substituir as chaves
    print("--------------------------------\nLivro cadastrado com sucesso!\n--------------------------------")  # Exibe uma mensagem informando que o livro foi cadastrado com sucesso

# Função para cadastrar usuário
def cadastrar_usuario():
    arquivo = open("usuarios.txt","a")
    # Solicita o código do usuário ao usuário
    while True: # enquanto fou verdade
        codigo = input("\nDigite o código do usuário: ") #solicitar ao usuario o codigo
        if codigo_existente("usuarios.txt", codigo): # chama a função para verificar se o codigo do usuario ja esta em uso
            print("--------------------------------\nO código já está em uso. Insira um código diferente.") #exibir mensagem
        else:
            break # sai do loop se o codigo nao existir

    # Solicita o nome do usuário ao usuário
    nome = input("Digite o nome do usuário: ")
    # Solicita o email do usuário ao usuário
    email = input("Digite o email do usuário: ")

    telefone = ""  # Define o telefone como vazio inicialmente
    telefone_formatado = ""  # Define o telefone formatado como vazio inicialmente

    # Loop para garantir que o usuário digite um telefone válido ou escolha não fornecer telefone
    while True:
        resposta = input("Deseja digitar o número de telefone? (s/n): ")  # Solicita ao usuário se deseja digitar o telefone
        if resposta.lower() == "s":  # Se a resposta for 's' (sim)
            telefone = input("Digite o telefone do usuário: ")  # Solicita o telefone
            if len(telefone) == 11:  # Verifica se o telefone possui 11 dígitos
                try: # tentar
                    # Formata o telefone no formato desejado
                    telefone_formatado = f"+55 {telefone[:2]} {telefone[2:7]} {telefone[7:]}"
                    break  # Sai do loop se o telefone for válido
                except ValueError:# pode ocorre erro não conversao de str para int e isso evitar , em vez de da erro ele imprimi a mensagem abaixo
                    print("O número de telefone deve conter apenas dígitos numéricos. Tente novamente.") # exibir essa mensagem de erro
            else: # condição se o numero digitado fou diferente de 11 digitos
                print("O número de telefone deve conter 11 dígitos. Tente novamente.")
        elif resposta.lower() == "n":  # Se a resposta for 'n' (não)
            break  # Sai do loop se o usuário escolher não fornecer telefone
        else:
                print("Resposta inválida. Digite 's' para sim ou 'n' para não.") # se o usuario digitar caract diferente de (s/n) ele 

    # Define o nome do arquivo onde os usuários serão cadastrados
    arquivo = "usuarios.txt"

    # Verifica se o arquivo existe
    if arquivo_vazio(arquivo):   # e verdae q o arquivo esta vazio 
        # Cria o arquivo e escreve o cabeçalho
        with open(arquivo, "w") as arquivo_criacao:
            arquivo_criacao.write("codigo|nome|email|telefone\n")

    # Monta a linha com os dados do usuário
    if telefone:  # Verifica se o telefone está preenchido
        linha_desejada = f"{codigo}|{nome}|{email}|{telefone_formatado}\n"
    else:
        linha_desejada = f"{codigo}|{nome}|{email}|\n"  # Cadastro do usuário sem telefone

    # Abre o arquivo no modo de escrita, adicionando ao final do arquivo
    with open(arquivo, "a") as arquivo_escrita:
        # Escreve os dados do usuário no arquivo
        arquivo_escrita.write(linha_desejada)

    # Exibe uma mensagem de sucesso ao usuário
    if telefone:
        print("--------------------------------\nUsuário cadastrado com sucesso!\n--------------------------------")
    else:
        print("--------------------------------\nUsuário cadastrado sem telefone!\n--------------------------------")

    
#reserva livro
def reservar_livro():
    arquivo = open("reservas.txt","a")
    arquivo_reservas = "reservas.txt"
    # Verifica se o arquivo de reservas existe e cria o cabeçalho se necessário
    if arquivo_vazio(arquivo_reservas):
        with open(arquivo_reservas, "w") as arquivo_criacao:
            arquivo_criacao.write("Codigo | Codigo do Usuario | Codigo do Livro | Data | Status\n")

    with open(arquivo_reservas, "r") as arquivo:
        reservas = arquivo.readlines()

    while True:
        codigo = input("\nDigite o código da reserva: ")
        codigo_repetido = False
        for linha in reservas[1:]:
            campos = linha.strip().split("|")
            if campos[0].strip() == codigo:
                codigo_repetido = True
                if "Finalizada" in campos[4].strip():
                    print("Não é possível fazer uma reserva para uma reserva finalizada.")
                    return
                else:
                    print("--------------------------------\nO código já está em uso. Insira um código diferente.")
                break
        if not codigo_repetido:
            break

    codigo_usuario = input("Digite o código do usuário: ")
    codigo_livro = input("Digite o código do livro: ")

    if not codigo_existente("usuarios.txt", codigo_usuario):
        print("Usuário não encontrado. Cadastre o usuário antes de fazer a reserva.")
        return

    if not codigo_existente("livros.txt", codigo_livro):
        print("Livro não encontrado. Cadastre o livro antes de fazer a reserva.")
        return

    data = datetime.now().strftime("%d/%m/%Y")
    status = "Ativa"
    linha_reserva = f"{codigo} | {codigo_usuario} | {codigo_livro} | {data} | {status}\n"

    with open(arquivo_reservas, "a") as arquivo:
        arquivo.write(linha_reserva)

    print("--------------------------------\nReserva realizada com sucesso!\n--------------------------------")



# Função para devolver livro
def devolver_livro():
    codigo_reserva = input("--------------------------------\nDigite o código da reserva: ")  # Solicita o código da reserva ao usuário
    reservas = []  # Cria uma lista vazia para armazenar as reservas

    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    encontrou_reserva = False  # Variável para indicar se a reserva foi encontrada ou não

    with open("reservas.txt", "w") as arquivo:  # Abre o arquivo de reservas no modo de escrita, sobrescrevendo o arquivo existente
        for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
            dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
            if dados_reserva[0].strip() == codigo_reserva.strip():  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário
                encontrou_reserva = True  # Marca que a reserva foi encontrada
                if dados_reserva[4].strip() == "Finalizada":
                    print("Este livro já foi devolvido anteriormente.")
                    arquivo.write(reserva)  # Escreve a reserva original no arquivo, sem alterações
                else:
                    dados_reserva[4] = "Finalizada"  # Atualiza o status da reserva para "Finalizada"
                    arquivo.write(dados_reserva[0] + "|" + dados_reserva[1] + "|" + dados_reserva[2] + "|" + dados_reserva[3] + "|" + dados_reserva[4] + "\n")  # Escreve os dados atualizados da reserva no arquivo
            else:
                arquivo.write(reserva)  # Escreve a reserva original no arquivo, sem alterações

    if encontrou_reserva:
        print("--------------------------------\nLivro devolvido com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se a reserva foi encontrada e atualizada
    else:
        print("--------------------------------\nReserva não encontrada.\n--------------------------------")  # Exibe uma mensagem de erro se a reserva não foi encontrada



# Função para alterar livr
def alterar():
    while True:
        print("\n=======Menu=======\n")
        print("1. Alterar livros")
        print("2. Alterar Usuários")
        print("3. Alterar Reservas")
        print("4. Voltar")
        opcao = input("Selecione uma opção: ")
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
            print("Opção incorreta. Por favor, tente novamente!")
        if opcao == "1":
            codigo_livro = input("--------------------------------\nDigite o código do livro: ")  # Solicita o código do livro ao usuário
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
                print("--------------------------------\nLivro alterado com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se o livro foi encontrado e atualizado
            else:
                print("--------------------------------\nLivro não encontrado.\n--------------------------------")  # Exibe uma mensagem de erro se o livro não foi encontrado

        if opcao =="2":
            # Função para alterar usuário
            codigo_usuario = input("--------------------------------\nDigite o código do usuário: ")
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

                        # Loop para garantir que o usuário digite um telefone válido ou escolha não fornecer telefone
                        while True:
                            resposta = input("Deseja digitar o número de telefone? (s/n): ")
                            if resposta.lower() == "s":
                                telefone = input("Digite o novo telefone do usuário: ")
                                if len(telefone) == 11:
                                    try:
                                        # Formata o telefone no formato desejado
                                        telefone_formatado = f"+55 {telefone[:2]} {telefone[2:7]} {telefone[7:]}"
                                        dados_usuario[3] = telefone_formatado
                                        break
                                    except ValueError:
                                        print("O número de telefone deve conter apenas dígitos numéricos. Tente novamente.")
                                else:
                                    print("O número de telefone deve conter 11 dígitos. Tente novamente.")
                            elif resposta.lower() == "n":
                                break
                            else:
                                print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

                        dados_usuario[1] = nome
                        dados_usuario[2] = email
                        arquivo.write("|".join(dados_usuario) + "\n")
                    else:
                        arquivo.write(usuario)

            if encontrou_usuario:
                print("--------------------------------\nUsuário alterado com sucesso!\n--------------------------------")
            else:
                print("--------------------------------\nUsuário não encontrado.\n--------------------------------")


        if opcao == "3":
            # Função para alterar reservas
            codigo_reserva = input("--------------------------------\nDigite o código da reserva: ")  # Solicita o código da reserva ao usuário
            reservas = []  # Cria uma lista vazia para armazenar as reservas

            with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
                reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

            encontrou_reserva = False  # Variável para indicar se a reserva foi encontrada ou não

            with open("reservas.txt", "w") as arquivo:  # Abre o arquivo de reservas no modo de escrita, sobrescrevendo o arquivo existente
                for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
                    dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                    if dados_reserva[0].strip() == codigo_reserva.strip():  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário (após remover os espaços em branco)
                        encontrou_reserva = True  # Marca que a reserva foi encontrada
                        data_reserva = input("Digite a nova data da reserva (DD/MM/AAAA): ")  # Solicita a nova data da reserva ao usuário
                        status_reserva = input("Digite o novo status da reserva (ativa/finalizada): ")  # Solicita o novo status da reserva ao usuário
                        
                        # Verifica se o valor do status é válido (ativa ou finalizada)
                        if status_reserva.lower() == "ativa" or status_reserva.lower() == "finalizada":
                            dados_reserva[3] = data_reserva  # Atualiza a data da reserva (índice 3, considerando a posição dos dados)
                            dados_reserva[4] = status_reserva  # Atualiza o status da reserva (índice 4, considerando a posição dos dados)
                            arquivo.write("|".join(dados_reserva) + "\n")  # Escreve os dados atualizados da reserva no arquivo
                            print("--------------------------------\nReserva alterada com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se a reserva foi encontrada e atualizada
                        else:
                            print("--------------------------------\nValor inválido para o status da reserva. A reserva não foi alterada.\n--------------------------------")  # Exibe uma mensagem de erro se o valor do status não for válido
                            arquivo.write(reserva)  # Escreve a reserva original no arquivo, sem alterações
                    else:
                        arquivo.write(reserva)  # Escreve a reserva original no arquivo, sem alterações

            if not encontrou_reserva:
                print("--------------------------------\nReserva não encontrada.\n--------------------------------")  # Exibe uma mensagem de erro se a reserva não foi encontrada

        #voltar menu
        elif opcao == "4":
            print("voltando...")
            break

#Função para remover

#Função para remover
def remover():
    while True:
            print("\n------------------------------")
            print("------------------------------\n")
            print("=== Remover ===")
            print("1. Remover livro")
            print("2. Remover usuário")
            print("3. Remover reserva")
            print("4. Voltar")
            #menu de remover
            opcao = input("Selecione uma opção: ")
            if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
                print("Opção incorreta. Por favor, tente novamente!")
            if opcao == "1":
                codigo_livro = input("--------------------------------\nDigite o código do livro: ")  # Solicita o código do livro ao usuário
                livro_encontrado = False  # Variável para indicar se o livro foi encontrado ou não

                with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
                    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

                with open("livros.txt", "w") as arquivo:  # Abre o arquivo de livros no modo de escrita, sobrescrevendo o arquivo existente
                    for linha in linhas:  # Itera sobre cada linha do arquivo
                        dados_livro = linha.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                        if dados_livro[0] != codigo_livro:  # Verifica se o código do livro atual é diferente do código fornecido pelo usuário
                            arquivo.write(linha)  # Escreve a linha no arquivo, exceto a linha correspondente ao livro a ser removido
                        else:
                            livro_encontrado = True  # Marca que o livro foi encontrado e será removido

                if livro_encontrado:
                    print("--------------------------------\nLivro removido com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se o livro foi encontrado e removido
                else:
                    print("--------------------------------\nLivro não encontrado.\n--------------------------------")  # Exibe uma mensagem de erro se o livro não foi encontrado

            # Função para remover usuário
            if opcao == "2":
                codigo_usuario = input("--------------------------------\nDigite o código do usuário: ")  # Solicita o código do usuário ao usuário
                usuarios = []  # Cria uma lista vazia para armazenar os usuários

                with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
                    usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

                encontrou_usuario = False  # Variável para indicar se o usuário foi encontrado ou não

                if usuarios:
                    with open("usuarios.txt", "w") as arquivo:  # Abre o arquivo de usuários no modo de escrita, sobrescrevendo o arquivo existente
                        for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
                            dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                            if dados_usuario[0] == codigo_usuario:  # Verifica se o código do usuário atual é igual ao código fornecido pelo usuário
                                encontrou_usuario = True  # Marca que o usuário foi encontrado e será removido
                            else:
                                arquivo.write(usuario)  # Escreve o usuário no arquivo, exceto o usuário que será removido

                if encontrou_usuario:
                    print("--------------------------------\nUsuário removido com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se o usuário foi encontrado e removido
                else:
                    print("--------------------------------\nUsuário não encontrado.\n--------------------------------")  # Exibe uma mensagem de erro se o usuário não foi encontrado

            # Função para remover reserva
            if opcao =="3":
                codigo_reserva = input("--------------------------------\nDigite o código da reserva: ")  # Solicita o código da reserva ao usuário
                reservas = []  # Cria uma lista vazia para armazenar as reservas

                with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
                    reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

                encontrou_reserva = False  # Variável para indicar se a reserva foi encontrada ou não

                with open("reservas.txt", "w") as arquivo:  # Abre o arquivo de reservas no modo de escrita, sobrescrevendo o arquivo existente
                    for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
                        dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                        if dados_reserva[0].strip() == codigo_reserva.strip():  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário (removendo espaços em branco)
                            encontrou_reserva = True  # Marca que a reserva foi encontrada e será removida
                        else:
                            arquivo.write(reserva)  # Escreve a reserva no arquivo, exceto a reserva que será removida

                if encontrou_reserva:
                    print("--------------------------------\nReserva removida com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se a reserva foi encontrada e removida
                else:
                    print("--------------------------------\nReserva não encontrada.\n--------------------------------")  # Exibe uma mensagem de erro se a reserva não foi encontrada
            if opcao == "4":
                print("Voltando...")
                break

# Função para pesquisar livros
    # Função para pesquisar livros
def pesquisar():
    while True:
        print("\n------------------------------")
        print("------------------------------\n")
        print("=== Menu de Pesquisa ===")
        print("1. Pesquisar livros")
        print("2. Pesquisar usuários")
        print("3. Pesquisar reservas")
        print("4. Voltar")
        # M3nu pesquisar
        opcao = input("Selecione uma opção: ")
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
            print("Opção incorreta. Por favor, tente novamente!")
        if opcao == "1":
            codigo_livro = input("--------------------------------\nDigite o código do livro: ")  # Solicita o código do livro ao usuário
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
        if opcao =="2":
            codigo_usuario = input("--------------------------------\nDigite o código do usuário: ")  # Solicita o código do usuário ao usuário
            usuarios = []  # Cria uma lista vazia para armazenar os usuários

            with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
                usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

            encontrado = False  # Variável para indicar se o usuário foi encontrado ou não

            for usuario in usuarios:  # Itera sobre cada usuário na lista de usuários
                dados_usuario = usuario.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                if dados_usuario[0] == codigo_usuario:  # Verifica se o código do usuário atual é igual ao código fornecido pelo usuário
                    print("------------------------\nUsuário encontrado:\n------------------------")
                    print(f"Código: {dados_usuario[0]}")
                    print(f"Nome: {dados_usuario[1]}")
                    print(f"E-mail: {dados_usuario[2]}")
                    print(f"Telefone: {dados_usuario[3]}")
                    encontrado = True
                    break

            if not encontrado:
                print("Usuário não encontrado.")  # Exibe uma mensagem de erro se o usuário não foi encontrado

        # Função para pesquisar reservas
        if opcao == "3":
            codigo_reserva = input("Digite o código da reserva: ")  # Solicita o código da reserva ao usuário
            reservas = []  # Cria uma lista vazia para armazenar as reservas

            with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
                reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

            encontrado = False  # Variável para indicar se a reserva foi encontrada ou não

            for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
                dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
                if dados_reserva[0].strip() == codigo_reserva.strip():  # Verifica se o código da reserva atual é igual ao código fornecido pelo usuário
                    print()
                    print("Reserva encontrada:")
                    print(f"Código: {dados_reserva[0]}")
                    print(f"Usuário: {dados_reserva[1]}")
                    print(f"Livro: {dados_reserva[2]}")
                    print(f"Data: {dados_reserva[3]}")
                    print(f"Status: {dados_reserva[4]}")
                    encontrado = True
                    break

            if not encontrado:
                print()
                print("Reserva não encontrada.")  # Exibe uma mensagem de erro se a reserva não foi encontrada
        if opcao == "4":
            print("Voltando...")
            break

# Função para listar 
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
        #menu de listagem
        opcao = input("Selecione uma opção: ")
        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6":
            print("Opção incorreta. Por favor, tente novamente!")
        #listagem de livros
        if opcao == "1":
            with open("livros.txt", "r") as arquivo:  # Abre o arquivo de livros no modo de leitura
                livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

            if len(livros) <= 1:
                print("Não há livros cadastrados.")
            else:
                for i in range(len(livros)):
                    print(livros[i].strip())

        # funçao listar usuarios cadastrados
        if opcao == "2":
            with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
                usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

            if len(usuarios) <= 1:
                print("Não há usuários cadastrados.")
            else:
                for i in range(len(usuarios)):
                    print(usuarios[i].strip())  # Exibe o usuário atual da lista removendo os espaços em branco no início e fim

        #listar reservas
        if opcao == "3":
            with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
                reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

            if len(reservas) <= 1:
                print("Não há reservas cadastradas.")
            else:
                print("Lista de reservas:")
                for reserva in reservas[1:]:  # Itera sobre cada reserva na lista de reservas, começando do índice 1
                    codigo, usuario, livro, data, status = reserva.strip().split("|")  # Divide os dados da reserva
                    print(f"{codigo} | {usuario} | {livro} | {data} | {status}")  # Exibe os dados da reserva formatados
                print("\n")  # Exibe uma linha em branco para separar as informações na saída

        #reservas ativas
        if opcao == "4":
            with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
                reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

            reservas_finalizadas = [reserva.strip().split("|") for reserva in reservas if reserva.strip().split("|")[4] == "Ativa"]

            if reservas_finalizadas:
                print("Lista de reservas Ativas:")
                for reserva in reservas_finalizadas:
                    codigo, usuario, livro, data, status = reserva
                    print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
                print("\n")
            else:
                print("Não há reservas Ativas.")



        # Função para listar reservas finalizadas
        if opcao == "5":
            with open("reservas.txt", "r") as arquivo:
                reservas = arquivo.readlines()

            reservas_ativas = [reserva.strip().split("|") for reserva in reservas if reserva.strip().split("|")[4].strip() == "Finalizada"]

            if reservas_ativas:
                print("Lista de reservas finalizadas:")
                for reserva in reservas_ativas:
                    codigo, usuario, livro, data, status = reserva
                    print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
                print("\n"*2)
            else:
                print("Nenhuma reservas finalizadas  encontrada.")
        if opcao == "6":
            print("Voltando...")
            break

# Função para gerar relatório
def gerar_relatorio():
    with open("livros.txt", "r") as arquivo_livros:  # Abre o arquivo de livros no modo de leitura
        livros = arquivo_livros.readlines()  # Lê todas as linhas do arquivo e armazena na lista de livros

    with open("usuarios.txt", "r") as arquivo_usuarios:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo_usuarios.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    with open("reservas.txt", "r") as arquivo_reservas:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo_reservas.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    total_livros = len(livros)  # Calcula o total de livros cadastrados
    total_usuarios = len(usuarios)  # Calcula o total de usuários cadastrados
    total_reservas = len(reservas)  # Calcula o total de reservas realizadas
    total_reservas_ativas = 0  # Inicializa o contador de reservas ativas
    total_reservas_finalizadas = 0  # Inicializa o contador de reservas finalizadas

    for reserva in reservas:  # Itera sobre cada reserva na lista de reservas
        dados_reserva = reserva.strip().split("|")  # Remove os espaços em branco no início e fim da linha e divide os dados pelo caractere "|"
        if len(dados_reserva) >= 5 and "Ativa" in dados_reserva[4].strip():  # Verifica se a reserva possui todos os campos necessários e se o status é "Ativa"
            total_reservas_ativas += 1  # Incrementa o contador de reservas ativas
        elif len(dados_reserva) >= 5 and "Finalizada" in dados_reserva[4].strip():  # Verifica se a reserva possui todos os campos necessários e se o status é "Finalizada"
            total_reservas_finalizadas += 1  # Incrementa o contador de reservas finalizadas

    print("Relatório:")
    print(f"Total de livros cadastrados: {total_livros}")  # Exibe o total de livros cadastrados
    print(f"Total de usuários cadastrados: {total_usuarios}")  # Exibe o total de usuários cadastrados
    print(f"Total de reservas realizadas: {total_reservas}")  # Exibe o total de reservas realizadas
    print(f"Total de reservas ativas: {total_reservas_ativas}")  # Exibe o total de reservas ativas
    print(f"Total de reservas finalizadas: {total_reservas_finalizadas}")  # Exibe o total de reservas finalizadas

# Menu principal
def main():
    while True:
        #limpar()
        print("\n")
        print("======= MENU =======")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Reservar livro")
        print("4. Devolver livro")
        print("5. Alterar ")
        print("6. Remover ")
        print("7. Pesquisar")
        print("8. listagem")
        print("9. gerar relatorio")
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
            alterar()
        elif opcao == "6":
            remover()
        elif opcao == "7":
            pesquisar()
        elif opcao == "8":
            listagem()
        elif opcao == "9":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")
if __name__ == "__main__":
    main()
