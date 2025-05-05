import cv2
import os
import numpy as np
import time

# Cargar el clasificador de rostro preentrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Configura la cámara
cap = cv2.VideoCapture(1)

# Crea el directorio para guardar las imágenes
if not os.path.exists('rostros'):
    os.makedirs('rostros')

# Empezar a capturar imágenes
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convierte la imagen a escala de grises
    
    # Detecta caras
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        # Dibuja un rectángulo alrededor de la cara detectada
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Recorta la cara y la guarda
        face = gray[y:y + h, x:x + w]
        cv2.imwrite(f'rostros/rostro_{int(time.time())}.jpg', face)
    
    cv2.imshow('Captura de Rostros', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
