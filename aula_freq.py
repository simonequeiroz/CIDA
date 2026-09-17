# Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Entrada de dados
emprestimos = [2, 3, 5, 4, 7, 4, 2, 5, 1, 3, 3, 5,
               3, 4, 0, 3, 4, 1, 2, 3]

# Processamento dos dados
L = 1   # Tamanho da classe
col_freq, classes = np.histogram(emprestimos)   # Cria a tabela de frequencia

# Calcula o número de classes
K = (max(emprestimos) - min(emprestimos)) / L   
k = int(np.ceil(K))   # Arredonda para cima


# Apresentação dos resultados
print("Número de classes: ", K)
print("Frequências: ", col_freq)
print("Classes: ", classes)

plt.hist(emprestimos,k)
plt.xlabel("Qtd de empréstimos")    # Rótulo do X
plt.ylabel("Frequência")            # Rótulo do Y
plt.title("Estudo da qtd de empréstimos nas 20 sem.")
plt.show()

