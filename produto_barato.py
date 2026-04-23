try:
    prod1 = float(input("Indique o preço do primeiro produto: "))
    prod2 = float(input("Indique o preço do segundo produto: "))
    prod3 = float(input("Indique o preço do terceiro produto: "))

    menor = prod1
    produtos_menores = "Primeiro produto"

    if prod2 < menor:
        menor = prod2
        produtos_menores = "Segundo produto"
    elif prod2 == menor:
        produtos_menores += " e Segundo produto"

    if prod3 < menor:
        menor = prod3
        produtos_menores = "Terceiro produto"
    elif prod3 == menor:
        if menor == prod1:
            produtos_menores += " e Terceiro produto"
        else:
            produtos_menores = "Segundo produto e Terceiro produto"

    print(f"Produto(s) mais barato(s): {produtos_menores} com preço de {menor}")

except ValueError:
    print("Erro: digite apenas números válidos!")
