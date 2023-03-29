import csv


# utlizei o site https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php para testar os valores

def ler_arquivo(nome):
    with open(nome + '.txt', 'r', newline='') as arquivo:
        dados = csv.reader(arquivo, delimiter='\n')
        dados = list(map(lambda x: float(x[0].replace(',', '.')), dados))
        return dados


def media(conjunto):
    soma = 0
    for i in conjunto:
        soma += i

    media = round(soma / len(conjunto), 3)
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
        somaMedianas = conjunto[int(meio_conjunto)] + conjunto[int(meio_conjunto) - 1]
        return round(somaMedianas / 2, 3)
    return round(conjunto[int(meio_conjunto)], 3)


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


def iqr(conjunto):
    return terceiro_quartil(conjunto) - primeiro_quartil(conjunto)


def corte_superior(conjunto):
    return round(terceiro_quartil(conjunto) + 1.5 * iqr(conjunto), 2)


def corte_inferior(conjunto):
    return round(primeiro_quartil(conjunto) - 1.5 * iqr(conjunto), 2)


lista = ler_arquivo('dados')
print(lista)
print("média: ", media(lista))
print("mediana: ", mediana(lista))
print("maior:", maior(lista))
print("menor: ", menor(lista))
print("moda: ", moda(lista))
print("1º quartil: ", primeiro_quartil(lista))
print("2º quartil: ", mediana(lista))
print("3º quartil: ", terceiro_quartil(lista))
print("corte superior: ", corte_superior(lista))
print("corte inferior: ", corte_inferior(lista))

