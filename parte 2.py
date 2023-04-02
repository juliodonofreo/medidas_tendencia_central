import statistics as st


# utlizei o site https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php para testar os valores

def ler_arquivo(nome):
    with open(nome + '.txt', 'r', newline='') as arquivo:
        dados = arquivo.readlines()
        dados = list(map(lambda x: float(x.replace(',', '.')), dados))
        return dados


def saida(conjunto):
    with open("saida2.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"média: {round(st.mean(conjunto), 3)}\n")
        arquivo.write(f"mediana: {round(st.median(conjunto), 3)}\n")
        arquivo.write(f"maior: {max(conjunto)}\n")
        arquivo.write(f"menor: {min(conjunto)}\n")
        modas = st.multimode(conjunto)
        if len(modas) == 1:
            arquivo.write(f"moda: {modas[0]}\n")
        else:
            for i, valorModa in enumerate(modas):
                arquivo.write(f"moda {i + 1}: {valorModa}\n")
        arquivo.write(f"1º quartil: {round(st.quantiles(lista)[0], 3)}\n")
        arquivo.write(f"2º quartil: {round(st.quantiles(lista)[1], 3)}\n")
        arquivo.write(f"3º quartil: {round(st.quantiles(lista)[2], 3)}\n")


lista = ler_arquivo('dados3')
saida(lista)
