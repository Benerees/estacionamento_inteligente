import matplotlib.pyplot as plt
import numpy as np

alturas = [30, 40, 50 , 60, 70]  # Exemplo de lista de alturas
f1 = [0.9999, 0.9996, 0.9990, 0.9990, 0.9998]  # Exemplo de lista de F1-scores correspondentes


plt.plot(alturas, f1, marker='o', linestyle='-', color='blue')  # Cria o gráfico
plt.xlabel('Alturas')
plt.ylabel('F1 Score')
plt.title('Desempenho do YOLO em relação às alturas')
plt.grid(True)  # Adiciona grade no gráfico
plt.show()  # Exibe o gráfico