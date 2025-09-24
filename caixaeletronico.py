print("==== Caixa Eletrônico ====")

# Entrada do valor
valor = int(input("Digite o valor para saque (mínimo R$2): "))

if valor < 2:
    print("Valor inválido! O saque deve ser de pelo menos R$2.")
else:
    # Cálculo das notas
    notas100 = valor // 100
    valor %= 100

    notas50 = valor // 50
    valor %= 50

    notas20 = valor // 20
    valor %= 20

    notas10 = valor // 10
    valor %= 10

    notas5 = valor // 5
    valor %= 5

    notas2 = valor // 2
    valor %= 2

    # Saída do resultado
    print("\n=== Saque realizado com sucesso===")

    if notas100 > 0:
        print(f"Notas de 100: {notas100}")
    if notas50 > 0:
        print(f"Notas de 50: {notas50}")
    if notas20 > 0:
        print(f"Notas de 20: {notas20}")
    if notas10 > 0:
        print(f"Notas de 10: {notas10}")
    if notas5 > 0:
        print(f"Notas de 5: {notas5}")
    if notas2 > 0:
        print(f"Notas de 2: {notas2}")
