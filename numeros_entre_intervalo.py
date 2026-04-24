try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    inicio = min(n1, n2)
    fim = max(n1, n2)

    if inicio == fim:
        print("Os numeros sao iguais")

    for i in range(inicio + 1, fim):
        print(i)

except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")
