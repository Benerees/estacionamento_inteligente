import pandas as pd
import numpy as np


dataset = pd.read_csv('D:/estacionamento_inteligente/runs/detect/train_frame_extraido7/results.csv')

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




 
#60m 0,997684    0,999094      0.999880     0.999689    0.996764   0.999774   0.999974    0.99927    0.999984