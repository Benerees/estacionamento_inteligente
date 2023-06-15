import cv2

# Vetores para armazenar as coordenadas das vagas livres e ocupadas
vagas_livres = []
vagas_ocupadas = []

# Função de callback do mouse para rotular as bounding boxes
def mouse_callback(event, x, y, flags, param):
    global drawing, top_left_pt, bottom_right_pt, vagas_livres, vagas_ocupadas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_pt = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bottom_right_pt = (x, y)
        cv2.rectangle(image, top_left_pt, bottom_right_pt, (0, 255, 0), 2)

        # Verifica se a vaga está livre ou ocupada
        resposta = input("A vaga está livre (L) ou ocupada (O)? ")

        if resposta.upper() == "L":
            vagas_livres.append((top_left_pt, bottom_right_pt))
        elif resposta.upper() == "O":
            vagas_ocupadas.append((top_left_pt, bottom_right_pt))

        cv2.imshow('Imagem', image)

# Carrega a imagem usando o OpenCV
image = cv2.imread('caminho/para/imagem.jpg')

# Cria uma janela para exibir a imagem
cv2.namedWindow('Imagem')

# Registra a função de callback para o evento do mouse
cv2.setMouseCallback('Imagem', mouse_callback)

# Exibe a imagem na janela
cv2.imshow('Imagem', image)

# Loop para esperar por eventos do teclado
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Verifica se a tecla Esc foi pressionada
        break

# Fecha a janela
cv2.destroyAllWindows()

# Imprime as coordenadas das vagas livres e ocupadas
print("Coordenadas das vagas livres:", vagas_livres)
print("Coordenadas das vagas ocupadas:", vagas_ocupadas)
