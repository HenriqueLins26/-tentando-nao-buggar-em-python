num = int(input("Digite um número: "))

print(f"\nTabuada do {num}:")
for c in range(1, 11):
    print(f"{num} x {c} = {num * c}")
