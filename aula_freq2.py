#Carregamento das bibliotecas 
import numpy as np
import matplotlib.pyplot as plt


# Entrada de Dados 

tempos_banho = [
    2, 3, 4, 5, 5, 5, 5, 6, 7, 8,
    8, 8, 9, 10, 10, 12, 12, 14, 14, 14,
    16, 20, 23, 25, 25, 28, 30, 32, 35, 38
]

# Processamento dos Dados 

print("==========================================")
print("   ANÁLISE DE FREQUÊNCIA - TEMPOS DE BANHO  ")
print("==========================================\n")

N = len(tempos_banho)   #Acha Número de observações
#Uso de Sturges para determinar a quantidade de BINS
k = 1 + 3.32* np.log10(N)   #Número de classes
k = int(np.round(k))   #Arredonda para cima 

# Criaçao da tabela de distribuição de frequências
frequencias, classes = np.histogram(tempos_banho, bins=k)   # Cria a tabela de frequencia


# Apresentação dos Dados 
print("Número de bins: ", k)
print("Frequências: ", frequencias)
print("Classes: ", classes)

#Criação do Histograma
plt.hist(tempos_banho, k)
plt.xlabel("Tempo de banho (minutos)")    # Rótulo do X
plt.ylabel("Frequência")            # Rótulo do Y
plt.title("Histograma do tempo de banho ")
plt.show()
