try:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    n3 = int(input("Digite o terceiro valor: "))

    maior = n1
    menor = n1

    if n2 > maior:
        maior = n2
    if n2 < menor:
        menor = n2

    if n3 > maior:
        maior = n3
    if n3 < menor:
        menor = n3

    mid = n1 + n2 + n3 - maior - menor

    print(f"\nMaior: {maior}")
    print(f"Meio: {mid}")
    print(f"Menor: {menor}")

except ValueError:
    print("Erro: digite apenas números inteiros válidos!")
