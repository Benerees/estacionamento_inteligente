import pandas as pd
import numpy as np


dataset = pd.read_csv('D:/estacionamento_inteligente/runs/detect/train_set1_70m_1/results.csv')
#print(dataset.columns)


loss = dataset['           val/box_loss']
epoch = dataset['                  epoch']

F1 = []
menor = loss[0]

for n in range(len(epoch)):
    if(loss[n] < menor and loss[n] != 0):
        menor = loss[n]
        epoca = epoch[n]


print('epoca =',epoca )
print('loss =',menor )
