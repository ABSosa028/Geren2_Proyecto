import tkinter as tk
from PIL import Image, ImageDraw
import os
import datetime

# Crear carpetas para cada número si no existen
for i in range(10):
    os.makedirs(f'datos/{i}', exist_ok=True)

# Interfaz
class DibujoNumerosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibujador de Números")
        self.numero_actual = tk.StringVar(value="0")

        # Canvas de dibujo
        self.canvas = tk.Canvas(root, width=280, height=280, bg='black')
        self.canvas.grid(row=0, column=0, columnspan=10)
        self.canvas.bind('<B1-Motion>', self.dibujar)

        # Imagen PIL para guardar
        self.imagen = Image.new("L", (280, 280), 'black')
        self.draw = ImageDraw.Draw(self.imagen)

        # Botones del 0 al 9
        for i in range(10):
            btn = tk.Radiobutton(root, text=str(i), variable=self.numero_actual, value=str(i))
            btn.grid(row=1, column=i)

        # Botón para guardar
        guardar_btn = tk.Button(root, text="Guardar imagen", command=self.guardar)
        guardar_btn.grid(row=2, column=3, columnspan=2)

        # Botón para limpiar
        limpiar_btn = tk.Button(root, text="Limpiar", command=self.limpiar)
        limpiar_btn.grid(row=2, column=5, columnspan=2)

    def dibujar(self, event):
        x, y = event.x, event.y
        r = 8  # radio del pincel
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill='white', outline='white')
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill='white')

    def guardar(self):
        numero = self.numero_actual.get()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        path = f"datos/{numero}/{numero}_{timestamp}.png"
        img_28x28 = self.imagen.resize((28, 28))
        img_28x28.save(path)
        print(f"Guardada imagen en: {path}")
        self.limpiar()

    def limpiar(self):
        self.canvas.delete('all')
        self.imagen = Image.new("L", (280, 280), 'black')
        self.draw = ImageDraw.Draw(self.imagen)

# Ejecutar
root = tk.Tk()
app = DibujoNumerosApp(root)
root.mainloop()
