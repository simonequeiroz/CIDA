# Carregamento de bibliotecas
import numpy as np
import scipy as sp


# Entrada de Dados
dureza_aco = np.array([
    83.3, 80.7, 86.4, 88.3, 84.7,
    85.2, 82.8, 87.8, 86.9, 86.2,
    83.5, 84.4, 87.2, 85.5, 86.3,
])


# Processamentos de dados
media = np.mean(dureza_aco)
mediana = np.median(dureza_aco)
desvio_padrao = np.std(dureza_aco, ddof=1)

print("===== LISTA DE EXERCÍCIOS 01 - EXERCÍCIO 3 =====")
print("Dureza do corpo de prova de aço")
print(f"\nDureza média: {media:.2f}")
print(f"Dureza mediana: {mediana:.2f}")
print(f"Desvio-padrão amostral: {desvio_padrao:.2f}")