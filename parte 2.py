import csv
import statistics as st


# utlizei o site https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php para testar os valores

def ler_arquivo(nome):
    with open(nome + '.txt', 'r', newline='') as arquivo:
        dados = csv.reader(arquivo, delimiter='\n')
        dados = list(map(lambda x: float(x[0].replace(',', '.')), dados))
        return dados


lista = ler_arquivo('dados2')
print(lista)
print("média: ", st.mean(lista))
print("mediana: ", st.median(lista))
print("maior:", max(lista))
print("menor: ", min(lista))
print("moda: ", st.multimode(lista))
print("1º quartil: ", st.quantiles(lista)[0])
print("2º quartil: ", st.median(lista))
print("3º quartil: ", st.quantiles(lista)[2])
