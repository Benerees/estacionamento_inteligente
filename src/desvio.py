import math

def calcular_desvio_padrao(vetor):
    media = sum(vetor) / len(vetor)

    soma_quadrados_diff = sum((x - media) ** 2 for x in vetor)

    variancia = soma_quadrados_diff / len(vetor)

    desvio_padrao = math.sqrt(variancia)

    print("media ",media)
    return desvio_padrao

vetor = [0.997684,    0.999094,      0.999880 ,    0.999689 ,   0.996764  , 0.999774]
desvio = calcular_desvio_padrao(vetor)
print(f"desvio: {desvio}")