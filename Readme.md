Plotagem de Razões Trigonométricas
Este código em Python utiliza a biblioteca Matplotlib para criar uma figura com quatro subplots, cada um representando uma razão trigonométrica: seno, cosseno, tangente e cotangente.

Instalação
Para executar este código, você precisará ter Python instalado em seu sistema. Além disso, é necessário instalar as bibliotecas Matplotlib e NumPy. Você pode instalar essas bibliotecas via pip, executando o seguinte comando:

Copy code
pip install matplotlib numpy
Como Usar
Importe as bibliotecas necessárias:
python
Copy code
# Importando pyplot da biblioteca Matplotlib e dando-lhe um apelido (alias) de plt
from matplotlib import pyplot as plt
# Importando a biblioteca NumPy e dando-lhe um apelido (alias) de np
import numpy as np
Defina os valores de x:
python
Copy code
# Criando um array de valores de 0 a 10 com intervalo de 0.1
x = np.arange(0, 10, 0.1)
Crie uma figura e subplots:
python
Copy code
# Criando uma figura e um conjunto de subplots com 2 colunas e 2 linhas, e definindo o tamanho da figura
fig_1, axes_1 = plt.subplots(ncols=2, nrows=2, figsize=(5, 5))
Adicione títulos aos subplots e plote as funções trigonométricas:
python
Copy code
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

# Plotando a cotangente de x no quarto subplot
axes_1[1, 1].plot(1/np.tan(x))
axes_1[1, 1].set_title("Cotangente")
Exiba os gráficos:
python
Copy code
# Exibindo os gráficos
plt.show()
Contribuições
Contribuições são bem-vindas! Se você encontrar qualquer problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Este README.md fornece uma visão geral do que o código faz, como usá-lo e como contribuir para ele. Você pode personalizá-lo conforme necessário para o seu projeto.