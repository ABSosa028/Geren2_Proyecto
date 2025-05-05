import cv2
import os
import numpy as np
import time

# Lista de emociones
emociones = ['feliz', 'triste', 'enojo', 'sorpresa', 'neutral']

# Cargar el clasificador de rostro preentrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Configura la cámara
cap = cv2.VideoCapture(0)

# Crea el directorio para guardar las imágenes de cada emoción
for emocion in emociones:
    if not os.path.exists(f'rostros_emociones/{emocion}'):
        os.makedirs(f'rostros_emociones/{emocion}')

# Instrucciones
print("Presiona 1-5 para elegir la emoción que estás mostrando:")
print("1: Feliz, 2: Triste, 3: Enojo, 4: Sorpresa, 5: Neutral")
print("Presiona 'q' para salir, 'r' para reanudar la captura, 'p' para pausar la captura")

paused = True  # Comienza en pausa para darte tiempo de cambiar de gesto
emocion_actual = None  # Inicialmente sin emoción seleccionada

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara.")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convierte la imagen a escala de grises
    
    # Detecta las caras solo si no está en pausa y si hay una emoción seleccionada
    if not paused and emocion_actual:
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
        for (x, y, w, h) in faces:
            # Dibuja un rectángulo alrededor de la cara detectada
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Recorta la cara
            face = gray[y:y + h, x:x + w]

            # Guardar automáticamente la imagen si hay una cara detectada
            timestamp = time.time()
            img_path = f'rostros_emociones/{emocion_actual}/{emocion_actual}_{int(timestamp)}.jpg'
            cv2.imwrite(img_path, face)
            print(f"Imagen de {emocion_actual} guardada en {img_path}")

            # Mostrar la imagen capturada
            cv2.imshow('Captura de Rostros', frame)
    
    # Mostrar nombre de la emoción actual en la pantalla
    if emocion_actual:
        cv2.putText(frame, f"Emoción actual: {emocion_actual}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar instrucciones
    cv2.putText(frame, "Presiona 'r' para reanudar la captura", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, "Presiona 'p' para pausar la captura", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Mostrar la vista previa de la cámara
    cv2.imshow('Captura de Rostros', frame)

    # Control de teclas
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):  # Salir con 'q'
        break
    elif key == ord('1'):  # Emoción Feliz
        emocion_actual = 'feliz'
        paused = True  # Pausar para cambiar de gesto
        print(f"Emoción cambiada a: {emocion_actual}")
    elif key == ord('2'):  # Emoción Triste
        emocion_actual = 'triste'
        paused = True  # Pausar para cambiar de gesto
        print(f"Emoción cambiada a: {emocion_actual}")
    elif key == ord('3'):  # Emoción Enojo
        emocion_actual = 'enojo'
        paused = True  # Pausar para cambiar de gesto
        print(f"Emoción cambiada a: {emocion_actual}")
    elif key == ord('4'):  # Emoción Sorpresa
        emocion_actual = 'sorpresa'
        paused = True  # Pausar para cambiar de gesto
        print(f"Emoción cambiada a: {emocion_actual}")
    elif key == ord('5'):  # Emoción Neutral
        emocion_actual = 'neutral'
        paused = True  # Pausar para cambiar de gesto
        print(f"Emoción cambiada a: {emocion_actual}")
    elif key == ord('r'):  # Reanudar la captura
        paused = False
        print("Captura reanudada.")
    elif key == ord('p'):  # Pausar la captura
        paused = True
        print("Captura pausada.")
    
cap.release()
cv2.destroyAllWindows()
