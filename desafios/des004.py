print("""\tMENU
Adição\t\t+
Subtração\t-
Multiplicação\t*
Divisão\t\t/\n""")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número:"))
opcao = input("Escolha a operação do MENU:")

if opcao == '+':
    print(f"O resultado de {num1} + {num2} é {num1 + num2}")

elif opcao == '-':
    print(f"O resultado de {num1} - {num2} é {num1 - num2}")

elif opcao == '*':
    print(f"O resultado de {num1} * {num2} é {num1 * num2}")

elif opcao == '/':
    if num2 == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        print(f"O resultado de {num1} / {num2} é {num1 / num2}")

else:
    print("Opção inválida!")