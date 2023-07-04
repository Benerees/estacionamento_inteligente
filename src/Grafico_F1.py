import matplotlib.pyplot as plt
import numpy as np

alturas = [30,40,50,60,70]  # Exemplo de lista de alturas 
f1 = [0.97,0.98,0.97,0.9,0.92]  # Exemplo de lista de F1-scores correspondentes

media = np.mean(f1)
print(media)
desvio = np.std(f1)
print(desvio)

plt.plot(alturas, f1, marker='o', linestyle='-', color='blue')  # Cria o gráfico
plt.xlabel('Alturas')
plt.ylabel('Média F1 Score')
plt.title('Desempenho do YOLO em diferentes alturas')
plt.grid(True)  # Adiciona grade no gráfico
plt.show()  # Exibe oZZZ gráfico

#media e desvio
#30  0.97 -- 0.06
#40 0.99  0.017
#50 0.97 -- 0.030
#60 0.89 0.9 -  0.06
#70 0.925 -- 0.014
