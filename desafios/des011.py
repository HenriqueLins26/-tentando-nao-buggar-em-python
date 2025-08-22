from time import sleep
lista = list()

while True:
    print("""MENU:
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair""")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        lista.append(str(input("Digite a tarefa: ")))

    elif escolha == 2:
        if len(lista) >= 1:
            print("Tarefas")
            for c, l in enumerate(lista):
                print(f"{c+1} - {l}")
        else:
            print("A lista de tarefas esta vazia!")
            
    elif escolha == 3:
        delet = int(input("Digite o número da tarefa a remover: "))

        if 1 <= delet <= len(lista): 
            lista.pop(delet - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido!")

    elif escolha == 4:
        print("Saindo do programa...")
        sleep(1)
        break

    else:
        print("Opção inválida! Tente novamente!")
    print()
