import cv2
import os
import datetime

# Lista de clases de gestos
gestos = ["a_feliz", "v_sorpresa", "c_neutral", "d_enojado", "e_asco", "f_miedo", "g_tristeza"]

# Crear carpetas para cada gesto si no existen
for gesto in gestos:
    os.makedirs(f'gestos2/{gesto}', exist_ok=True)

# Captura de video desde la cámara (NO forzamos resolución)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

gesto_actual = gestos[0]
print(f"Capturando imágenes para: {gesto_actual}")
print("Presiona G para cambiar de gesto, S para guardar imagen, Q para salir.")

indice_gesto = 0
contador = len(os.listdir(f'gestos2/{gesto_actual}'))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara.")
        break

    

    cv2.imshow("Captura de Gestos", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # Salir
        break
    elif key == ord('s'):  # Guardar imagen con resolución original
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        ruta = f"gestos2/{gesto_actual}/{gesto_actual}_{timestamp}.png"
        cv2.imwrite(ruta, frame)
        print(f"Imagen guardada en {ruta}")
        contador += 1
        cv2.waitKey(300)  # Evitar doble captura
    elif key == ord('g'):  # Cambiar gesto
        indice_gesto = (indice_gesto + 1) % len(gestos)
        gesto_actual = gestos[indice_gesto]
        contador = len(os.listdir(f'gestos2/{gesto_actual}'))
        print(f"Gesto cambiado a: {gesto_actual}")

cap.release()
cv2.destroyAllWindows()
