produto = []
c = maior = menor = soma = 0

num = int(input("Quantos produtos deseja cadastrar? "))

while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    produto.append([nome, preco])
    

    if len(produto) == 1:
        maior = menor = preco
        
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco

    soma += preco

    c +=1
    if c == num:
        break

print(f"\nProdutos cadastrados: {produto}")

print("Produto mais caro: ", end='')
for p in produto:
    if p[1] == maior:
        print(f"{p[0]} - R${maior:.2f}")

print("Produto mais barato: ", end='')
for p in produto:
    if p[1] == menor:
        print(f"{p[0]} - R${menor:.2f}")
media = soma / len(produto)
print(f"Média dos preços: R${media:.2f}")
print(f"Valor total: R${soma:.2f}")
