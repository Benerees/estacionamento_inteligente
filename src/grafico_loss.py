import matplotlib.pyplot as plt
import numpy as np

alturas = [30, 40, 50 , 60, 70]  # Exemplo de lista de alturas
loss = [0.77229, 0.78438, 0.94614, 1.0806, 1.0538]  # Exemplo de lista de F1-scores correspondentes

plt.plot(alturas, loss, marker='o', linestyle='-', color='blue')  # Cria o gráfico
plt.xlabel('Alturas')
plt.ylabel('Loss')
plt.title('Desempenho do YOLO em relação às alturas')
plt.grid(True)  # Adiciona grade no gráfico
plt.show()  # Exibe o gráfico
