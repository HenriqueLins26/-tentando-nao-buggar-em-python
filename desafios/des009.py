nota = []
soma = 0

nome = str(input("Digite o nome do aluno: "))

for c in range(1, 6):
    nota.append(float(input(f"Digite a {c}ª nota: ")))

media = sum(nota) / len(nota)

print(f"""
Nome: {nome}
Notas: {nota}
Média: {media:.1f}
Maior nota: {max(nota)}
Menor nota: {min(nota)}
Situação: """,end='')

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
