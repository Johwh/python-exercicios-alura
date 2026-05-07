# senha correta definida no sistema
senha_correta = "1234"

# contador de tentativas
tentativas = 0

# permite no máximo 3 tentativas
while tentativas < 3:

    senha = input("Senha: ")

    # verifica se acertou a senha
    if senha == senha_correta:
        print("Acesso liberado")
        break

    # incrementa tentativas se errar
    tentativas += 1
