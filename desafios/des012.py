from time import sleep
alunos = list()


while True:
    print("""MENU:
1 - Adicionar aluno
2 - Lista de alunos
3 - Remover aluno
4 - Mostrar média da turma
5 - Sair""")
    opc = int(input("Escolha: "))

    if opc == 1:
        nome = str(input("Nome do aluno(a): "))
        nota = float(input("Nota: "))
        alunos.append([nome, nota])

    elif opc == 2:
        if len(alunos) >= 1:
            for c, a in enumerate(alunos):
                print(f"{c+1} - {a[0]}: {a[1]}")
        else:
            print("Nenhum aluno cadastrado")

    elif opc == 3:
        remove = int(input("Digite o número do aluno a remover: "))
        if 1 <= remove <= len(alunos): 
            alunos.pop(remove - 1)
            print("Aluno removido com sucesso!")
        else:
            print("Número inválido!")

    elif opc == 4:
        if len(alunos) > 0:
            soma = 0
            for n in alunos:
                soma += n[1]
            media = soma / len(alunos)
            print(f"Média da turma: {media:.2f}")
        else:
            print("Nenhum aluno cadastrado!")

    elif opc == 5:
        print("Saindo do programa...")
        sleep(1)
        break

    else:
        print("Opção inválida! Tente novamente.")
    print()
