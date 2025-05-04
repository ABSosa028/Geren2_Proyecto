import cv2
import os

def quitar_fondo_simple(img_path, out_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    b, g, r = cv2.split(img)
    rgba = [b, g, r, alpha]
    result = cv2.merge(rgba)
    cv2.imwrite(out_path, result)

# Ejemplo de uso
carpeta_entrada = "gestos/dedo_arriba"
carpeta_salida = "gestos_limpios/dedo_arriba"
os.makedirs(carpeta_salida, exist_ok=True)

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        quitar_fondo_simple(
            os.path.join(carpeta_entrada, archivo),
            os.path.join(carpeta_salida, archivo)
        )
