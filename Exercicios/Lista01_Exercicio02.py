# Carregamento de bibliotecas
import numpy as np
import scipy as sp


# Entrada de Dados
pilha_a = np.array([153, 173, 134, 157, 149, 171, 162])
pilha_b = np.array([172, 163, 151, 146, 146])


# Processamentos de dados
media_a = np.mean(pilha_a)
desvio_a = np.std(pilha_a, ddof=1)
media_b = np.mean(pilha_b)
desvio_b = np.std(pilha_b, ddof=1)

print("LISTA DE EXERCÍCIOS 01 - EXERCÍCIO 2")
print("Comparação da duração de duas marcas de pilhas")
print(f"\nMarca A - média: {media_a:.2f} h")
print(f"Marca A - desvio-padrão amostral: {desvio_a:.2f} h")
print(f"Marca B - média: {media_b:.2f} h")
print(f"Marca B - desvio-padrão amostral: {desvio_b:.2f} h")
print("\nA marca B apresenta maior consistência e previsibilidade,")
print("pois possui o menor desvio-padrão.")
print("\nNão é possível afirmar que uma marca tenha duração superior")
print("sem realizar um teste estatístico adequado.")