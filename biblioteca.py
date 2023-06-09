#Isso permite que você utilize os recursos relacionados a datas  fornecidos pela biblioteca datetime .
from datetime import datetime # importa a classe datetime do módulo datetime
import os  # Importa a biblioteca 'os', que possui várias funções, mas neste caso é usada para limpar o terminal toda vez que o menu for executado.

def limpar():  # Define a função 'limpar' para limpar o terminal e deixá-lo mais organizado.
 os.system("cls")  # Chama a função 'system' do módulo 'os' para executar o comando "cls", que limpa o terminal no Windows.

 #cria os arquivos txt
arquivo =  open("livros.txt","w+")
arquivo = open("usuarios.txt","w+")
arquivo = open("reservas.txt","w+")
 
# Função para verificar se o arquivo está vazio e, caso esteja, adiciona o nome das categorias
def arquivo_vazio(arquivo):
    with open(arquivo, "r") as leitura:  # Abre o arquivo especificado em modo de leitura
        conteudo = leitura.read()  # Lê o conteúdo do arquivo e o armazena na variável 'conteudo'
        return len(conteudo) == 0  # Retorna True se o tamanho do conteúdo for igual a zero, indicando que o arquivo está vazio
    #resumo essa função e para verificar se existe cabeçalho 
def codigo_existente(nome_arquivo, codigo):
    with open(nome_arquivo, "r") as arquivo_leitura:
        # Verifica se o código já existe no arquivo
        for linha in arquivo_leitura:
            campos = linha.strip().split("|")
            if campos[0] == codigo:
                return True
    return False
# Função para cadastrar um livro
def cadastrar_livro():
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



def reservar_livro():
    # Função para reservar um livro
    while True: # enquanto fou verdade
        codigo_reserva = input("\nDigite o código da reserva:: ") #solicitar o codigo da reserva ao usuario
        if codigo_existente("usuarios.txt", codigo_reserva): # chama a função para verificar se o codigo do usuario ja esta em uso
            print("--------------------------------\nO código já está em uso. Insira um código diferente.") #exibir mensagem
        else:
            break # sai do loop se o codigo nao existir
    codigo_usuario = input("Digite o código do usuário: ")  # Solicita o código do usuário ao usuário
    codigo_livro = input("Digite o código do livro: ")  # Solicita o código do livro ao usuário

    # Verifica se existem usuários cadastrados
    if not codigo_existente("usuarios.txt", codigo_usuario):
        print("Usuário não encontrado. Cadastre o usuário antes de fazer a reserva.")
        return
    # Verifica se existem livros cadastrados
    # Verifica se o livro não existe no arquivo "livros.txt"
    if not codigo_existente("livros.txt", codigo_livro):
        print("Livro não encontrado. Cadastre o livro antes de fazer a reserva.")
        return
    data = datetime.now().strftime("%d/%m/%Y")  # Obtém a data atual no formato DD/MM/AAAA
    status = "Ativa"  # Define o status da reserva como "Ativa"

    linha_desejada = "Codigo | Usuario | Livro | Data | Status"  # Define a linha desejada no arquivo
    arquivo = "reservas.txt"  # Define o nome do arquivo onde as reservas serão registradas

    with open(arquivo, "a+") as arquivo_leitura:
        arquivo_leitura.seek(0)  # Volta para o início do arquivo
        if linha_desejada not in arquivo_leitura.read():  # Verifica se a linha desejada já existe no arquivo
            arquivo_leitura.write(linha_desejada + "\n")  # Se não existir, escreve a linha desejada no arquivo
    with open(arquivo, "a") as arquivo_escrita:  # Abre o arquivo no modo de escrita, adicionando ao final do arquivo
        arquivo_escrita.write(f"{codigo_reserva} | {codigo_usuario} | {codigo_livro} | {data} | {status}\n")  # Escreve os dados da reserva no arquivo

    print("--------------------------------\nReserva realizada com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso ao usuário



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


# Função para alterar livro
def alterar_livro():
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

# Função para alterar usuário
def alterar_usuario():
    codigo_usuario = input("--------------------------------\nDigite o código do usuário: ")  # Solicita o código do usuário ao usuário
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
        print("--------------------------------\nUsuário alterado com sucesso!\n--------------------------------")  # Exibe uma mensagem de sucesso se o usuário foi encontrado e atualizado
    else:
        print("Usuário não encontrado.")  # Exibe uma mensagem de erro se o usuário não foi encontrado


def remover_livro():
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
def remover_usuario():
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
def remover_reserva():
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

# Função para pesquisar livros
def pesquisar_livros():
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
def pesquisar_usuarios():
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
def pesquisar_reservas():
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
        livros = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

    if len(livros) <= 1:
        print("Não há livros cadastrados.")
    else:
        for i in range(len(livros)):
            print(livros[i].strip())

# funçao listar usuarios cadastrados
def listar_usuarios():
    with open("usuarios.txt", "r") as arquivo:  # Abre o arquivo de usuários no modo de leitura
        usuarios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de usuários

    if len(usuarios) <= 1:
        print("Não há usuários cadastrados.")
    else:
        for i in range(len(usuarios)):
            print(usuarios[i].strip())  # Exibe o usuário atual da lista removendo os espaços em branco no início e fim

#listar reservas
def listar_reservas():
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

#reservas finalizada
def listar_reservas_finalizadas():
    with open("reservas.txt", "r") as arquivo:  # Abre o arquivo de reservas no modo de leitura
        reservas = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista de reservas

    reservas_finalizadas = [reserva.strip().split("|") for reserva in reservas if reserva.strip().split("|")[4] == "Finalizada"]

    if reservas_finalizadas:
        print("Lista de reservas finalizadas:")
        for reserva in reservas_finalizadas:
            codigo, usuario, livro, data, status = reserva
            print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
        print("\n")
    else:
        print("Não há reservas finalizadas.")



# Função para listar reservas ativas
def listar_reservas_ativas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    reservas_ativas = [reserva.strip().split("|") for reserva in reservas if reserva.strip().split("|")[4].strip() == "Ativa"]

    if reservas_ativas:
        print("Lista de reservas ativas:")
        for reserva in reservas_ativas:
            codigo, usuario, livro, data, status = reserva
            print(f"{codigo} | {usuario} | {livro} | {data} | {status}")
        print("\n"*2)
    else:
        print("Nenhuma reserva ativa encontrada.")

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
        #menu de remover
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
        #menu de listagem
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
