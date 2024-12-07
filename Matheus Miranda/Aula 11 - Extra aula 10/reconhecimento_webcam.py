#C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR

#1 - Instalação do tesseract
#2 - Instalação da Biblioteca pytesseract
    #pip install pytesseract
    
#3 - Instalação da Biblioteca opencv
    #pip install opencv-python

#Biblioteca para trabalho com imagens
import cv2 
#Biclioteca para reconhecer caracteres
import pytesseract

lista_alunos= ["24263890"]

# #Indicar o pacote de reconhecimento de caracteres
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#Importar biblioteca opencv
import cv2

webcam = cv2.VideoCapture(0)

while True:
    #fazer a leitura da variável webcam
    sucesso, frame = webcam.read()
    cv2.imshow("Camera", frame) 
    
    cv2.imwrite('ImagemSalva.png', frame)
    img_salva = cv2.imread('ImagemSalva.png')
    img_pt_br = cv2.cvtColor(img_salva, cv2.COLOR_BGR2GRAY)
    texto_capturado = pytesseract.image_to_string(img_pt_br, config='-l eng --oem 3 --psm 12')
    print(texto_capturado)

    if cv2.waitKey(1) & 0xff == ord("s"):
        break
    

webcam.release()
cv2.destroyAllWindows()


#Removendo espaços do texto capturado
# captura_sem_espaco = placa_lida.strip()
# print(captura_sem_espaco)

# #Printar informações do proprietário do veículo
for cadastro in lista_alunos:
    if texto_capturado in cadastro:
        print('ALUNO CADASTRADO!')

#Inserir um ponto de parada
cv2.waitKey(0)






    
    