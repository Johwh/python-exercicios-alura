try:
    val1 = float(input("Ano 1: "))
    val2 = float(input("Ano 2: "))
    val3 = float(input("Ano 3: "))

    maior = val1
    menor = val1

    if val2 > maior:
        maior = val2
    elif val2 < menor:
        menor = val2

    if val3 > maior:
        maior = val3
    elif val3 < menor:
        menor = val3

    print(f"\nMaior valor: {maior}")
    print(f"Menor valor: {menor}")

except ValueError:
    print("\nEntrada inválida! Use apenas números.")
