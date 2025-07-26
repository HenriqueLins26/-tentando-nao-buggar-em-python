while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    opcao = str(input("Escolha a operação (+ - * /): "))

    if opcao == '+':
        print(f"Resultado: {n1 + n2}")

    elif opcao == '-':
        print(f"Resultado: {n1 - n2}")

    elif opcao == '*':
        print(f"Resultado: {n1 * n2}")

    elif opcao == '/':
        if n2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print(f"Resultado: {n1 / n2}")
            
    else:
        print("Opção inválida!")

    sn = str(input("Deseja continuar? (s/n)")).strip().lower()

    if sn == 'n':
        print("Encerrando a calculadora. Até a proxima!")
        break
    