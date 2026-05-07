# Lista original com números positivos e negativos
numeros = [-2, 5, -1, 10, 3]

# Lista vazia que vai armazenar apenas números positivos
positivos = []

# Loop que percorre cada número da lista
for n in numeros:

    # Verifica se o número é maior que zero
    if n > 0:

        # Adiciona o número positivo na nova lista
        positivos.append(n)

# Mostra o resultado final
print(positivos)
