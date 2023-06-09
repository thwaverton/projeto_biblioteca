
def menu_principal():# menu principal
    while True: # verdade quando
        print("=== Menu Principal ===")  # vai imprir esses caracteres
        print("1. Fazer pedido")
        print("2. Verificar status do pedido")
        print("3. Menu de opções adicionais")
        print("4. Sair")

        opcao = input("Selecione uma opção: ") # pedir uma opcao ao usario

        if opcao == "1":
            fazer_pedido()

        elif opcao == "2":
            verificar_status_pedido()

        elif opcao == "3":
            menu_opcoes_adicionais()

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def fazer_pedido():
    print("=== Fazer Pedido ===")
    item = input("Digite o nome do item que deseja pedir: ")
    quantidade = input("Digite a quantidade desejada: ")
    # Lógica para fazer um pedido
    print("Pedido de", quantidade, item, "realizado com sucesso!")

def verificar_status_pedido():
    print("=== Verificar Status do Pedido ===")
    numero_pedido = input("Digite o número do pedido: ")
    # Lógica para verificar o status de um pedido
    print("Status do pedido", numero_pedido, ": Em andamento")

def menu_opcoes_adicionais():
    while True:
        print("=== Menu de Opções Adicionais ===")
        print("1. Adicionar bebida")
        print("2. Adicionar sobremesa")
        print("3. Voltar")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            adicionar_bebida()

        elif opcao == "2":
            adicionar_sobremesa()

        elif opcao == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")

        if opcao not in ["1", "2", "3"]: #retorna se caso o caractere digitado pelo usuario fou errado
            print("Retornando ao Menu Principal...")
            menu_principal()
            break


def adicionar_bebida():
    print("=== Adicionar Bebida ===")
    bebida = input("Digite o nome da bebida: ")
    tamanho = input("Digite o tamanho da bebida (P, M, G): ")
    # Lógica para adicionar uma bebida ao pedido
    print(bebida, tamanho, "adicionada ao pedido.")

def adicionar_sobremesa():
    print("=== Adicionar Sobremesa ===")
    sobremesa = input("Digite o nome da sobremesa: ")
    quantidade = input("Digite a quantidade desejada: ")
    # Lógica para adicionar uma sobremesa ao pedido
    print(quantidade, sobremesa, "adicionada ao pedido.")

menu_principal()
