salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

try:
    abonos = {}
    total_gasto = 0
    qtd_abono_minimo = 0
    maior_abono = 0

    print("=== SISTEMA DE CÁLCULO DE ABONOS ===")
    print("Regra: 10% do salário com mínimo de R$ 200\n")

    for salario in salarios:
        abono = salario * 0.10

        if abono < 200:
            abono = 200
            qtd_abono_minimo += 1

        abonos[salario] = abono
        total_gasto += abono

        if abono > maior_abono:
            maior_abono = abono

    print("=== ABONOS POR COLABORADOR ===\n")

    for salario, abono in abonos.items():
        print(f"Salário: R$ {salario:.2f}")
        print(f"→ Abono recebido: R$ {abono:.2f}\n")

    print("=== RESUMO FINAL ===")
    print(f"💰 Total gasto com abonos: R$ {total_gasto:.2f}")
    print(f"📉 Colaboradores com abono mínimo (R$200): {qtd_abono_minimo}")
    print(f"📈 Maior abono concedido: R$ {maior_abono:.2f}")

except Exception as e:
    print("Erro ao processar os dados:", e)
