from sklearn.model_selection import train_test_split
from PIL import Image
import numpy as np
import os
import cv2

# Pasta contendo as imagens
pasta_imagens = "Base_de_Dados"

# Lista para armazenar os caminhos completos das imagens
caminhos_imagens = []

# Percorre a pasta de imagens e obtém os caminhos completos das imagens
for arquivo in os.listdir(pasta_imagens):
    caminho_imagem = os.path.join(pasta_imagens, arquivo)
    caminhos_imagens.append(caminho_imagem)

# Carrega as imagens como arrays usando o Pillow (PIL) e redimensiona
imagens = []
for caminho_imagem in caminhos_imagens:
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((224, 224))  # Redimensiona para 224x224 (exemplo)
    array_imagem = np.array(imagem)
    imagens.append(array_imagem)

# Converte a lista de imagens em um array NumPy
dados = np.array(imagens)

# Dividindo os dados em treinamento e teste
train_data, test_data = train_test_split(dados, test_size=0.2, random_state=42)

# Imprimindo as dimensões dos conjuntos de treinamento e teste
print("Dimensões do Conjunto de Treinamento:", train_data.shape)
print("Dimensões do Conjunto de Teste:", test_data.shape)
