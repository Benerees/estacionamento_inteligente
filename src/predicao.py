# Valores fornecidos
VP = 62
VN = 0
FN = 3
FP = 0

precisao = VP / (VP + FP)

recall = VP / (VP + FN)

f1= 2 * (precisao * recall) / (precisao + recall)

print("F1 Score: ", f1)


#30m  0.96,  0.96 - 0.96
#40m  0.97,  1.0  - 0,98
#50m  1.0,     0.98,    1.0 - 0.99
#60m  1.0,  0.95, 0.98, 1.0, 0.92, 1.0, 0.98, 0.98, 1.0 - 0,97
#70m  0.97, 1.0 - 0.985