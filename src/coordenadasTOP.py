import cv2

x_min = y_min = largura = altura = None

def clique(event, x, y, flags, param):
    global x_min, y_min, largura, altura

    if event == cv2.EVENT_LBUTTONDOWN:
        x_min = x
        y_min = y

    elif event == cv2.EVENT_LBUTTONUP:
        largura = x - x_min
        altura = y - y_min

        #normalização dos pixeis da imagem, para obter as coordenadas
        x_min_norm = x_min / largura_imagem
        y_min_norm = y_min / altura_imagem
        largura_norm = largura / largura_imagem
        altura_norm = altura / altura_imagem

        #ordem : x,y,largura e altura (todos normalizados)
        print(x_min_norm, y_min_norm , largura_norm,altura_norm)
       

# alterar o caminho da pasta especificada
image = cv2.imread('D:/estacionamento_inteligente/data/Base_de_Dados/ocupadas_set2_60m_1.JPG')
largura_imagem = image.shape[1]
altura_imagem = image.shape[0]
cv2.namedWindow('Imagem')

cv2.setMouseCallback('Imagem', clique)

cv2.imshow('Imagem', image)

#pressionar 'ESC' para fechar a janela
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break

cv2.destroyAllWindows()
