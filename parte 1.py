# utlizei o site https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php para testar os valores

def ler_arquivo(nome):
    with open(nome + '.txt', 'r', newline='') as arquivo:
        dados = arquivo.readlines()
        dados = list(map(lambda x: float(x.replace(',', '.')), dados))
        return dados


def media(conjunto):
    soma = 0
    for i in conjunto:
        soma += i

    media = soma / len(conjunto)
    return media


def moda(conjunto):
    ocorrencias_por_valor: dict = {i: conjunto.count(i) for i in conjunto}
    ocorrencia_maior = max(ocorrencias_por_valor.values())
    modas = [k for k, v in ocorrencias_por_valor.items() if v == ocorrencia_maior]
    return modas


def mediana(conjunto):
    conjunto.sort()
    meio_conjunto = len(conjunto) / 2

    if len(conjunto) % 2 == 0:
        soma_medianas = conjunto[int(meio_conjunto)] + conjunto[int(meio_conjunto) - 1]
        return soma_medianas / 2
    else:
        return conjunto[int(meio_conjunto)]


def maior(conjunto):
    numero_maior = 0
    for num in conjunto:
        if num > numero_maior:
            numero_maior = num
    return numero_maior


def menor(conjunto):
    numero_menor = None
    for num in conjunto:
        if numero_menor is None or num < numero_menor:
            numero_menor = num
    return numero_menor


def primeiro_quartil(conjunto):
    conjunto.sort()
    tamanho_conjunto = len(conjunto)

    primeira_metade = [conjunto[i] for i in range(0, int(tamanho_conjunto / 2))]
    quartil = mediana(primeira_metade)
    return quartil


def terceiro_quartil(conjunto):
    conjunto.sort()
    tamanho_conjunto = len(conjunto)

    segunda_metade = [conjunto[i] for i in range(0, -int(tamanho_conjunto / 2), -1)]
    quartil = mediana(segunda_metade)
    return quartil


def saida(conjunto):
    with open('saida1.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"média: {round(media(conjunto), 3)}\n")
        arquivo.write(f"mediana: {round(mediana(conjunto), 3)}\n")
        arquivo.write(f"maior: {maior(conjunto)}\n")
        arquivo.write(f"menor: {menor(conjunto)}\n")
        modas = moda(conjunto)
        if len(modas) == 1:
            arquivo.write(f"moda: {modas[0]}\n")
        else:
            for i, valorModa in enumerate(modas):
                arquivo.write(f"moda {i + 1}: {valorModa}\n")
        arquivo.write(f"1º quartil: {round(primeiro_quartil(lista), 3)}\n")
        arquivo.write(f"2º quartil: {round(mediana(lista), 3)}\n")
        arquivo.write(f"3º quartil: {round(terceiro_quartil(lista), 3)}\n")


lista = ler_arquivo('dados3')
saida(lista)
