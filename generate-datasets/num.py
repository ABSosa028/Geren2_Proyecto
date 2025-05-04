import tkinter as tk
from PIL import Image, ImageDraw
import os

IMG_SIZE = 28
NUMEROS = [str(i) for i in range(10)]  # 0 al 9

def asegurarse_directorio(num):
    ruta = f'datasets/numeros/{num}'
    os.makedirs(ruta, exist_ok=True)
    return ruta

def contar_imagenes(num):
    return len(os.listdir(asegurarse_directorio(num)))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Dibuja un número")

# Variable seleccionada para el número (DEBE ir después de crear la ventana)
numero_actual = tk.StringVar()
numero_actual.set(NUMEROS[0])

# Dropdown para elegir número
frame_top = tk.Frame(ventana)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Selecciona el número:").pack(side='left')
menu_numeros = tk.OptionMenu(frame_top, numero_actual, *NUMEROS)
menu_numeros.pack(side='left')

# Canvas para dibujar
canvas = tk.Canvas(ventana, width=200, height=200, bg='white')
canvas.pack()

# Imagen y objeto de dibujo
imagen = Image.new("L", (200, 200), color=255)
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
    numero = numero_actual.get()
    ruta = asegurarse_directorio(numero)
    contador = contar_imagenes(numero)
    imagen_redimensionada = imagen.resize((IMG_SIZE, IMG_SIZE))
    filename = f'{numero}_{contador:03d}.png'
    imagen_redimensionada.save(os.path.join(ruta, filename))
    print(f"Imagen guardada: {filename}")
    limpiar()

# Eventos
canvas.bind("<B1-Motion>", dibujar_trazo)

# Botones
botones = tk.Frame(ventana)
botones.pack(pady=10)

tk.Button(botones, text="Guardar", command=guardar).pack(side='left', padx=10)
tk.Button(botones, text="Limpiar", command=limpiar).pack(side='left')

ventana.mainloop()
