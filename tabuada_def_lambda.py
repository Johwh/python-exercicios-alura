# Tabuada com função tradicional (def)
n = int(input("Digite um número: "))

def tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

tabuada(n)


# Tabuada com função lambda
n = int(input("Digite um número: "))

tabuada = lambda x: n * x

print(f"Tabuada do {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {tabuada(i)}")
