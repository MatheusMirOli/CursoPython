import cv2
#capturando uma imagem

imagem = cv2.imread('pessoa1.jpg')
cv2.imshow('pessoa1',imagem)

#carregar características do arquivo
cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('resultado',imagem_cinza)
#verificar se a imagem está preta e branca
cv2.imshow('imagem preta e branca', imagem_cinza)

#detectando rostos e desenhando um quadrado
faces = cascadeFace.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=1, minSize=(100,100))

for (x, y, w, h) in faces:
    cv2.rectangle(imagem,(x,y),(x+w, y+h),(0,0,255),2)
    cv2.imshow('Face Detectada',imagem)
cv2.waitKey(0)
