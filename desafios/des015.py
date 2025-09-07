num = [[],[]]

for c in range(1, 11):
    n = int(input(f"Digite o {c}º número: "))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

print(f"Lista de pares: {num[0]}")
print(f"lista de impares: {num[1]}")
print(f"Total de pares: {len(num[0])}")
print(f"Total de impares: {len(num[1])}")
