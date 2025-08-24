from time import sleep
produto = list()

while True:
    print("""MENU:
1 - Adicionar produto
2 - Listar produtos
3 - Remover produtos
4 - Quantidade total no estoque
5 - Sair""")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        nome = str(input("Nome do produto: "))
        quant = int(input("Quantidade: "))
        produto.append([nome, quant])

    elif escolha == 2:
        if len(produto) > 0:
            for c, p in enumerate(produto):
                print(f"{c+1} - {p[0]}: {p[1]}")
        else:
            print("Nenhum produto cadastrado!")

    elif escolha == 3:
        remove = int(input("Digite o número do produto a remover: "))
        if (1 <= remove) and ( remove <= len(produto)): 
            produto.pop(remove - 1)
            print("Produto removido com sucesso!")
        else:
            print("Número inválido!")

    elif escolha == 4:
        if len(produto) > 0:
            total = 0
            for p in produto:
                total += p[1]
            print(f"Quantidade total de itens no estoque: {total}")
        else:
            print("Nenhum produto cadastrado!")
            
    elif escolha == 5:
        print("Saindo do programa...")
        sleep(1)
        break

    else:
        print("Opção inválida! Tente novamente!")
    print()
