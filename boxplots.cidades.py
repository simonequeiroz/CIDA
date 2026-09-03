#Carregamentos das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Entrada de Dados
populacao = [988.8, 556.9, 224.6, 210.9, 201.5,
             187.7, 151.6, 135.8, 129.8, 119.4,
             116.0, 102.3, 101.8, 92.4, 84.7,
             83.9, 80.2, 74.7, 72.7, 68.4,
             66.8, 66.8, 63.7, 62.8, 61.9,
             56.2, 54.1, 50.3, 49.7, 46.3]

po_sudeste = [988.8, 556.9, 210.9, 101.8, 92.4,
              84.7, 83.9, 72.7, 68.4, 63.7, 62.8, 61.9,
              50.3, 49.7, 46.3]

# Processamento de Dados 


Q1 = np.percentile(populacao, q=25) # 1º Quartil (25%)
Q2 = np.percentile(populacao, q=50) # 2º Quartil (50%)
Q3 = np.percentile(populacao, q=75) # 3º Quartil (75%)

menor_valor = min(populacao)   #Acha o menor valor da população
maior_valor = max(populacao)   #Acha o maior valor da população
DQ = Q3 - Q1                   #Calcula o intervalo interquartil (IQR)
limite_inferior = max(menor_valor, Q1 - 1.5 * (DQ)) # Acha Limite inferior para outliers
limite_superior = min(maior_valor, Q3 + 1.5 * (DQ)) # Limite superior para outliers

# Processamento de Dados da Região Sudeste
Q1_sudeste = np.percentile(po_sudeste, q=25)
Q2_sudeste = np.percentile(po_sudeste, q=50)
Q3_sudeste = np.percentile(po_sudeste, q=75)

menor_valor_sudeste = min(po_sudeste)
maior_valor_sudeste = max(po_sudeste)
DQ_sudeste = Q3_sudeste - Q1_sudeste
limite_inferior_sudeste = max(
    menor_valor_sudeste, Q1_sudeste - 1.5 * DQ_sudeste
)
limite_superior_sudeste = min(
    maior_valor_sudeste, Q3_sudeste + 1.5 * DQ_sudeste
)


# Apresentação dos resultados
print("Q1: ", Q1)
print("Q2: ", Q2)
print("Q3: ", Q3)
print("limite_inferior: ", limite_inferior)
print("limite_superior: ", limite_superior)
print("Q1 Sudeste: ", Q1_sudeste)
print("Q2 Sudeste: ", Q2_sudeste)
print("Q3 Sudeste: ", Q3_sudeste)
print("limite_inferior Sudeste: ", limite_inferior_sudeste)
print("limite_superior Sudeste: ", limite_superior_sudeste)

plt.boxplot([populacao, po_sudeste], tick_labels=["Brasil", "Sudeste"])
plt.title("Distribuição da população: Brasil e Sudeste")
plt.ylabel("População (milhares de habitantes)")
plt.show()
