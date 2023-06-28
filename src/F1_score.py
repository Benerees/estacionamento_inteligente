import pandas as pd
import numpy as np


dataset = pd.read_csv('D:/estacionamento_inteligente/runs/detect/train_set2_30m_2/results.csv')

precision = dataset['   metrics/precision(B)']
recall = dataset['      metrics/recall(B)']
epoch = dataset['                  epoch']

F1 = []
maior = 0

for n in range(len(epoch)):
    f1 = 2 * ((recall[n] * precision[n]) / (recall[n] + precision[n]))
    
    if(f1 > maior):
        maior = f1
        epoca = epoch[n]

print()     
print('maior ',maior )
print('epoca ',epoca )





# 0.9990440871031836 + 0.9999449969748336