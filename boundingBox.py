import cv2

# Lista para armazenar as bounding boxes
bounding_boxes = []

def draw_bounding_box(event, x, y, flags, param):
    global bounding_boxes

    if event == cv2.EVENT_LBUTTONDOWN:
        bounding_boxes.append([(x, y)])
    elif event == cv2.EVENT_LBUTTONUP:
        bounding_boxes[-1].append((x, y))
        cv2.rectangle(image, bounding_boxes[-1][0], bounding_boxes[-1][1], (0, 255, 0), 2)
        cv2.imshow('Image', image)

# Carregar a imagem
image = cv2.imread('ocupadas_set1_30m_2.jpg')

# Criar a janela e definir o callback do mouse
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_bounding_box)

# Loop principal
while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF

    # Pressione a tecla 'esc' para sair do loop
    if key == 27:
        break

# Salvar as imagens de todas as bounding boxes
for i, bbox in enumerate(bounding_boxes):
    xmin, ymin = bbox[0]
    xmax, ymax = bbox[1]
    cropped_image = image[ymin:ymax, xmin:xmax]
    cv2.imwrite(f'bounding_box_ocupadas2{i}.jpg', cropped_image)

cv2.destroyAllWindows()
