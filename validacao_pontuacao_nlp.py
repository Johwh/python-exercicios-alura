lista_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
    'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial'
]

lista_nao_tratada = [
    'Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
    'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
    'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!'
]

def verificar_pontuacao(lista_palavras):
    for palavra in lista_palavras:
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            raise ValueError(
                f'O texto apresenta pontuações na palavra "{palavra}".'
            )

    return "Texto validado com sucesso!"

try:
    resultado = verificar_pontuacao(lista_nao_tratada)
    print(resultado)

except ValueError as erro:
    print(erro)
