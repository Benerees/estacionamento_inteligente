import cv2

def read_bounding_boxes_from_txt(file_path):
    bounding_boxes = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split()
            label = int(data[0])
            x = float(data[1])
            y = float(data[2])
            width = float(data[3])
            height = float(data[4])
            bounding_box = (x, y, width, height)
            bounding_boxes.append(bounding_box)

    return bounding_boxes

cars_file = 'D:/Projetos/estacionamento_inteligente/data/images/imagens_30m/foto_30.txt'
parking_spots_file = 'D:/Projetos/estacionamento_inteligente/data/map_estacionamento/foto_30.txt'

cars = read_bounding_boxes_from_txt(cars_file)
parking_spots = read_bounding_boxes_from_txt(parking_spots_file)

# print("Cars:")
# for car in cars:
#     print(car)

# print("Parking Spots:")
# for spot in parking_spots:
#     print(spot)

def calculate_overlap(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[0] + box1[2], box2[0] + box2[2])
    y2 = min(box1[1] + box1[3], box2[1] + box2[3])

    intersection_area = max(0, x2 - x1) * max(0, y2 - y1)
    box1_area = box1[2] * box1[3]
    overlap_percentage = intersection_area / box1_area

    return overlap_percentage

image_path = 'D:/Projetos/estacionamento_inteligente/data/images/imagens_30m/foto_30.jpg'
frame = cv2.imread(image_path)

height, width, canais = frame.shape



def count_parking_status(parking_spots, cars):
    occupied_count = 0
    vacant_count = len(parking_spots)
    carros_transito = len(cars);
    ocupacao_irregular = 0;

    cars_list = []
    for spot in parking_spots:
        spot_occupied = False
        mal_estacionado = False

        for car in cars:
            overlap_percentage = calculate_overlap(spot, car)

            if overlap_percentage >= 0.6:
                carros_transito -= 1
                spot_occupied = True
                break
            elif overlap_percentage >= 0.3:
                if car in cars_list:
                    print("já está na lista")
                else:
                    cars_list.append(car)
                    carros_transito -= 1
                    ocupacao_irregular +=1

                mal_estacionado = True
                break
        
        x, y, width_y, height_y = spot
       
        x1 = x - (width_y/2)
        x2 = x + (width_y/2)
        y1 = y - (height_y/2)
        y2 = y + (height_y/2)

        x1 = x1 * width
        y1 = y1 * height
        x2 = x2 * width
        y2 = y2 * height

        if spot_occupied:
            occupied_count += 1
            vacant_count -= 1
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
            cv2.putText(frame, "Vaga ocupada".upper(), (int(x1), int(y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        elif mal_estacionado:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 1)
            cv2.putText(frame, "Mal estacionado".upper(), (int(x1), int(y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            occupied_count += 1
            vacant_count -= 1
        else:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
            cv2.putText(frame, "Vaga vazia".upper(), (int(x1), int(y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    return occupied_count, vacant_count, carros_transito, ocupacao_irregular

occupied, vacant, carros_transito, ocupacao_irregular = count_parking_status(parking_spots, cars)


cv2.putText(frame, f'Vagas ocupadas: {occupied}', (int(20), int(30)),
cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.putText(frame, f'Vagas vazias: {vacant}', (int(20), int(60)),
cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.putText(frame, f'Carros em transito: {carros_transito}', (int(20), int(90)),
cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
cv2.putText(frame, f'Carros mal estacionados: {ocupacao_irregular}', (int(20), int(120)),
cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv2.LINE_AA)
cv2.imwrite('D:/Projetos/estacionamento_inteligente/teste/result.JPEG', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

