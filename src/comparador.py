import pandas as pd
import numpy as np


dataset = pd.read_csv('D:/estacionamento_inteligente/runs/detect/train_set1_70m_1/results.csv')
print(dataset.columns)


mAP = dataset['    metrics/mAP50-95(B)']
epoch = dataset['                  epoch']
recall = dataset['      metrics/recall(B)']
precision = dataset['   metrics/precision(B)']

map = []
epo =[]
rec = []
prec = []

for n in range(len(epoch)):
    if ((n % 5) == 0 and n != 0):
        map.append(mAP[n])
        epo.append(epoch[n])
        rec.append(recall[n])
        prec.append(precision[n])


print("map: ",map)

print("rec ",rec)

print("prec ",prec)

print("epoch ",epo)


