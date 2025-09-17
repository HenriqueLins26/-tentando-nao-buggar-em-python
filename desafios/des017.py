saque = float(input("Digite um valor para saque: "))

total = saque
ced = 50
tot = 0

while True:
    if total >= ced:
        total -= ced
        tot +=1
    else:
        if tot > 0:
            print(f"Notas de R${ced}: {tot}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if total == 0:
            break
if tot > 0:
    print(f"Notas de R${ced}: {tot}")