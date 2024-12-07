#Utilizar web cam do computador
#Instalar biblioteca opencv:
#                            pip install opencv-python

#biblioteca para trabalhos com imagens
import cv2

webcam = cv2.VideoCapture(0)

while True:
    #fazer a leitura da variável webcam
    sucesso, frame = webcam.read()
    cv2.imshow("Camera", frame) 
    
    if cv2.waitKey(1) & 0xff == ord("s"):
        break
    
webcam.release()
cv2.destroyAllWindows()