cont_0_25 = 0 
cont_26_50 = 0 
cont_51_75 = 0 
cont_76_100 = 0 
cont_101_120 = 0

while True:
    entrada = input("Informe a idade (ou digite 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        break

    try:
        idade = int(entrada)

        if idade < 0 or idade > 120:
            print("Idade inválida! Digite um valor entre 0 e 120.\n")
            continue

        if idade <= 25:
            cont_0_25 += 1
        elif idade <= 50:
            cont_26_50 += 1
        elif idade <= 75:
            cont_51_75 += 1
        elif idade <= 100:
            cont_76_100 += 1
        else:
            cont_101_120 += 1

    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'sair'.\n")

print('\nDistribuição de idades:')
print('[0-25]:', cont_0_25)
print('[26-50]:', cont_26_50)
print('[51-75]:', cont_51_75)
print('[76-100]:', cont_76_100)
print('[101-120]:', cont_101_120)
