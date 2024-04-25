# Importando pyplot da biblioteca Matplotlib e dando-lhe um apelido (alias) de plt
from matplotlib import pyplot as plt
# Importando a biblioteca NumPy e dando-lhe um apelido (alias) de np
import numpy as np

# Criando um array de valores de 0 a 10 com intervalo de 0.1
x = np.arange(0, 10, 0.1)

# Criando uma figura e um conjunto de subplots com 2 colunas e 2 linhas, e definindo o tamanho da figura
fig_1, axes_1 = plt.subplots(ncols=2, nrows=2, figsize=(5, 5))

# Adicionando um título à figura
fig_1.suptitle("Plotagem de Razões Trigonométricas ")

# Plotando o seno de x no primeiro subplot
axes_1[0, 0].plot(np.sin(x))
axes_1[0, 0].set_title("Seno")

# Plotando o cosseno de x no segundo subplot
axes_1[0, 1].plot(np.cos(x))
axes_1[0, 1].set_title("Cosseno")

# Plotando a tangente de x no terceiro subplot
axes_1[1, 0].plot(np.tan(x))
axes_1[1, 0].set_title("Tangente")

# Plotando a tangente de x no quarto subplot
# Plotando a cotangente de x no quinto subplot
axes_1[1, 1].plot(1/np.tan(x))
axes_1[1, 1].set_title("Cotangente")


# Exibindo os gráficos
plt.show()


