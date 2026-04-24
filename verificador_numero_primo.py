try:
    n = int(input("Digite um numero inteiro: "))

    if n <= 1:
        print(f"O número {n} não é primo")
    else:
        n_primo = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                n_primo = False
                break

        if n_primo:
            print(f"O número {n} é primo")
        else:
            print(f"O número {n} não é primo")

except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")
