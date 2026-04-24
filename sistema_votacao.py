votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_branco = 0

limite = 15
total_votos = 0

print("=== SISTEMA DE VOTAÇÃO ===")
print("1 - Candidato 1")
print("2 - Candidato 2")
print("3 - Candidato 3")
print("4 - Candidato 4")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("==========================\n")

while total_votos < limite:
    try:
        voto = int(input(f'Voto {total_votos + 1}/{limite} - Informe seu voto: '))

        if voto == 1:
            votos_candidato1 += 1
        elif voto == 2:
            votos_candidato2 += 1
        elif voto == 3:
            votos_candidato3 += 1
        elif voto == 4:
            votos_candidato4 += 1
        elif voto == 5:
            votos_nulos += 1
        elif voto == 6:
            votos_branco += 1
        else:
            print("Voto inválido! Digite um número entre 1 e 6.\n")
            continue

        total_votos += 1

    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")

print("\n=== RESULTADO DA VOTAÇÃO ===")
print(f'Votos candidato 1: {votos_candidato1}')
print(f'Votos candidato 2: {votos_candidato2}')
print(f'Votos candidato 3: {votos_candidato3}')
print(f'Votos candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos em branco: {votos_branco}')

print(f'\nPercentual de votos nulos: {(votos_nulos / total_votos) * 100:.2f}%')
print(f'Percentual de votos em branco: {(votos_branco / total_votos) * 100:.2f}%')


#Adicao propria ao exercicio: vencedor / empate
votos = [votos_candidato1, votos_candidato2, votos_candidato3, votos_candidato4]
maior = max(votos)

if votos.count(maior) > 1:
    print("\nHouve empate entre os candidatos.")
else:
    vencedor = votos.index(maior) + 1
    print(f"\nO candidato vencedor é o candidato {vencedor} com {maior} votos.")
