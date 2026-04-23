vend2022 = float(input("Quantidade de vendas 2022: "))
vend2023 = float(input("Quantidade de vendas 2023: "))

if vend2022 == 0:
    print("Não é possível calcular a variação (divisão por zero).")
else:
    variacao = 100 * (vend2023 - vend2022) / vend2022
    print(f"Variação: {variacao:.2f}%")

    if variacao > 20:
        print("Bonificação para o time de vendas")
    elif 2 <= variacao <= 20:
        print("Pequena bonificação para o time de vendas")
    elif -10 <= variacao < 2:
        print("Planejamento de políticas de incentivo às vendas.")
    else:
        print("Corte de gastos.")
