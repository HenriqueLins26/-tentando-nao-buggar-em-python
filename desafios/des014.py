frase = str(input("Digite uma frase: ")).strip()
f1 = frase.strip().lower()

print(f"Frase: {frase}")
print(f"Quantidade de 'a': {f1.count('a')}")
print(f"Quantidade de 'e': {f1.count('e')}")
print(f"Quantidade de 'i': {f1.count('i')}")
print(f"Quantidade de 'o': {f1.count('o')}")
print(f"Quantidade de 'u': {f1.count('u')}")

total = f1.count('a') + f1.count('e') + f1.count('i') + f1.count('o') + f1.count('u')

print(f"Total de vogais: {total}")
