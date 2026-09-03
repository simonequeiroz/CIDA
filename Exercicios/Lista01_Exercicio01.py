# Carregamento de bibliotecas
import numpy as np
import scipy as sp


# Entrada de Dados

# Lista com os valores de resistência à compressão do material, em MPa.
resistencia_compressao = np.array([348.5, 340.1, 360.8, 353.2, 357.6])


# Processamentos de dados
# Calcula a média dos valores de resistência.
media = np.mean(resistencia_compressao)
# Calcula a distância média entre os valores e a média.
desvio_medio = np.mean(np.abs(resistencia_compressao - media))
# Calcula o desvio-padrão amostral para medir a variação dos valores.
desvio_padrao = np.std(resistencia_compressao, ddof=1)

# Exibe os resultados dos cálculos na tela.
print("LISTA DE EXERCÍCIOS 01 - EXERCÍCIO 1")
print("Resistência mecânica")
# Mostra a resistência média dos corpos de prova.
print(f"\nTensão média: {media:.2f} MPa")
# Mostra a diferença média entre cada valor e a média.
print(f"Desvio-médio absoluto: {desvio_medio:.2f} MPa")
# Mostra quanto os valores variam em relação à média.
print(f"Desvio-padrão amostral: {desvio_padrao:.2f} MPa")