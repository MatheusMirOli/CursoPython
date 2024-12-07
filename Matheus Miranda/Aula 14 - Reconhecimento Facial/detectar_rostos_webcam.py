#Importar biblioteca opencv
import cv2

#Utilizar o arquivo detector de rostos/faces
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Abrir a câmera
camera = cv2.VideoCapture(0)

while True:
    sucesso, frame = camera.read()
    #cv2.imshow('webcam', frame)

    #converter frame para P&B
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('webcam', frame_cinza)
    
    #detectar os rostos/faces no frame
    rostos = detector.detectMultiScale(frame_cinza, scaleFactor=1.1, minNeighbors=1, minSize=(100,100))
    
    #desenhar o retângulo no frame
    for (x, y, lar, alt) in rostos:
        cv2.rectangle(frame,(x,y),(x+lar, y+alt),(000,000,255),2)
    
    #Exibindo o frame desenhado    
    cv2.imshow('Rostos Detectados',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    
#fecha streaming    
camera.release