soma = maior = menor = 0

for c  in range(1,6):
    num = int(input("Digite um número: "))

    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    soma += num

media = soma / 5

print(f"""Soma: {soma}
Média: {media:.1f}
Maior número: {maior}
Menor número: {menor}""")
