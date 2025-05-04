import cv2
import os
import datetime

# Lista de clases de gestos
gestos = ["mano_abierta", "puno", "dedo_arriba", "sonrisa", "enojo", "sorpresa", "tristeza", "desprecio", "neutro", "fuck_you"]

# Crear carpetas para cada gesto si no existen
for gesto in gestos:
    os.makedirs(f'gestos/{gesto}', exist_ok=True)

# Captura de video desde la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


gesto_actual = gestos[0]
print(f"Capturando imágenes para: {gesto_actual}")
print("Presiona G para cambiar de gesto, S para guardar imagen, Q para salir.")

indice_gesto = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara.")
        break

    # Mostrar nombre del gesto en pantalla
    cv2.putText(frame, f"Gesto actual: {gesto_actual}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Captura de Gestos", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Salir
        break
    elif key == ord('s'):  # Guardar imagen
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        ruta = f"gestos/{gesto_actual}/{gesto_actual}_{timestamp}.png"
        img_redimensionada = cv2.resize(frame, (128, 128))  # puedes ajustar a 64x64 o 224x224 según el modelo
        cv2.imwrite(ruta, img_redimensionada)
        print(f"Imagen guardada en {ruta}")
    elif key == ord('g'):  # Cambiar de gesto
        indice_gesto = (indice_gesto + 1) % len(gestos)
        gesto_actual = gestos[indice_gesto]
        print(f"Gesto cambiado a: {gesto_actual}")

cap.release()
cv2.destroyAllWindows()
