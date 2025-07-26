nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você pode entrar no evento. Boa diversão!")
else:
    opc = str(input("Você está acompanhado(a) dos pais? (s/n)")).strip().lower()

    if opc == 's':
        print(f"{nome}, por estar acompanhado(a) dos pais, sua entrada está permitida.")
    elif opc == 'n':
        print(f"{nome}, infelizmente você não pode entrar no evento.")
    else: 
        print("Opção inválida")
