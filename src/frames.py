import cv2

video = cv2.VideoCapture('C:/Users/dani/Desktop/videos_davi/DJI_0270.mp4')
count = 0
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
tempo_desejado = 2
tempo_desejado_em_frames = int(tempo_desejado * fps)
if tempo_desejado_em_frames >= total_frames:
    tempo_desejado_em_frames = total_frames - 1

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    count += 1
    if count == tempo_desejado_em_frames:
        cv2.imwrite('frame_extraido7.jpg', frame)
        break


video.release()
cv2.destroyAllWindows()
