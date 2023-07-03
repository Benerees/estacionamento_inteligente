import cv2

def extract_frame(video_path, output_path, frame_time):
    # Abre o vídeo
    video = cv2.VideoCapture(video_path)

    # Obtém a taxa de frames por segundo (fps) do vídeo
    fps = video.get(cv2.CAP_PROP_FPS)

    # Calcula o número do frame com base no tempo fornecido
    frame_number = int(frame_time * fps)

    # Define a posição do vídeo para o frame desejado
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Lê o frame
    ret, frame = video.read()

    # Verifica se o frame foi lido corretamente
    if ret:
        # Salva o frame como uma imagem
        cv2.imwrite(output_path, frame)
        print(f"O frame do tempo {frame_time} segundos foi salvo com sucesso como {output_path}.")
    else:
        print("Não foi possível ler o frame do vídeo.")

    # Libera os recursos
    video.release()


video_path = "C:/Users/dani/Downloads/DJI_0030.MOV"  # Substitua pelo caminho do seu vídeo
output_path = "foto_30_7.jpg"  # Substitua pelo caminho onde deseja salvar o frame
frame_time = 279 # Substitua pelo tempo desejado em segundos

extract_frame(video_path, output_path, frame_time)