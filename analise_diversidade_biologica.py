dados = {
    'Área Norte': {'plantas': 2819, 'animais': 7236},
    'Área Leste': {'plantas': 1440, 'animais': 9492},
    'Área Sul': {'plantas': 5969, 'animais': 7496},
    'Área Oeste': {'plantas': 14446, 'animais': 49688},
    'Área Centro': {'plantas': 22558, 'animais': 45148}
}

try:
    maior_media = float('-inf')  
    area_maior = ""

    print("=== ANÁLISE DE DIVERSIDADE BIOLÓGICA ===\n")

    for area, info in dados.items():
        total = info['plantas'] + info['animais']
        media = total / 2

        print(f"{area}:")
        print(f"  - Plantas: {info['plantas']}")
        print(f"  - Animais: {info['animais']}")
        print(f"  - Média de espécies: {media:.2f}\n")

        if media > maior_media:
            maior_media = media
            area_maior = area

    print("=== RESULTADO FINAL ===")
    print(f"A área com maior diversidade biológica é: {area_maior}")
    print(f"Média de espécies: {maior_media:.2f}")

except Exception as e:
    print("Erro ao processar os dados:", e)
