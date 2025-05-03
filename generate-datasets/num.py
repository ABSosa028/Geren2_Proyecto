import tkinter as tk
from PIL import Image, ImageDraw
import os

# === CONFIGURACIÓN ===
IMG_SIZE = 28
NUMERO = '1'  # Cambia aquí el número que estás dibujando
OUTPUT_DIR = f'datasets/numeros/{NUMERO}'

# Aseguramos que la carpeta exista
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Contador de imágenes
contador = len(os.listdir(OUTPUT_DIR))

# Crear ventana
ventana = tk.Tk()
ventana.title(f"Dibuja el número {NUMERO}")

# Crear canvas para dibujar
canvas = tk.Canvas(ventana, width=200, height=200, bg='white')
canvas.pack()

# Imagen en blanco y objeto de dibujo
imagen = Image.new("L", (200, 200), color=255)  # L: escala de grises
dibujar = ImageDraw.Draw(imagen)

def dibujar_trazo(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
    dibujar.ellipse([x1, y1, x2, y2], fill=0)

def limpiar():
    canvas.delete("all")
    global imagen, dibujar
    imagen = Image.new("L", (200, 200), color=255)
    dibujar = ImageDraw.Draw(imagen)

def guardar():
    global contador
    imagen_redimensionada = imagen.resize((IMG_SIZE, IMG_SIZE))
    ruta = os.path.join(OUTPUT_DIR, f'{NUMERO}_{contador:03d}.png')
    imagen_redimensionada.save(ruta)
    print(f"Imagen guardada: {ruta}")
    contador += 1
    limpiar()

# Vincular eventos
canvas.bind("<B1-Motion>", dibujar_trazo)

# Botones
botones = tk.Frame(ventana)
botones.pack()

btn_guardar = tk.Button(botones, text="Guardar", command=guardar)
btn_guardar.pack(side='left', padx=10)

btn_limpiar = tk.Button(botones, text="Limpiar", command=limpiar)
btn_limpiar.pack(side='left')

ventana.mainloop()
