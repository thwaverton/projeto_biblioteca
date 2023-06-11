from funcoes import cadastrar_livro, cadastrar_usuario, reservar_livro, devolver_livro, alterar, remover, pesquisar, listagem, gerar_relatorio
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
