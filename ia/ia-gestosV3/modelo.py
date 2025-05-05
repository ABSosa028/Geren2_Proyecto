import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import numpy as np
import os
from sklearn.model_selection import train_test_split

ruta_base = "rostros_emociones"  # tu nueva carpeta
tamanio_img = (400, 400)  # mejor resolución para precisión
clases = sorted(os.listdir(ruta_base))  # Detecta clases automáticamente

imagenes = []
etiquetas = []

for i, clase in enumerate(clases):
    carpeta = os.path.join(ruta_base, clase)
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(carpeta, archivo)
            img = load_img(img_path, color_mode='grayscale', target_size=tamanio_img)  # <--- aún se redimensiona
            img_array = img_to_array(img) / 255.0
            imagenes.append(img_array)
            etiquetas.append(i)


# Convertir a arrays
X = np.array(imagenes).reshape(-1, tamanio_img[0], tamanio_img[1], 1)
y = np.array(etiquetas)

# Dividir
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el generador de datos de entrenamiento con data augmentation
datagen = ImageDataGenerator(
    rotation_range=30,          # Rotación aleatoria de las imágenes
    width_shift_range=0.2,      # Desplazamiento horizontal
    height_shift_range=0.2,     # Desplazamiento vertical
    shear_range=0.2,            # Cizalladura (distorsión de la imagen)
    zoom_range=0.2,             # Zoom aleatorio
    horizontal_flip=True,       # Voltear las imágenes aleatoriamente
    fill_mode='nearest'         # Rellenar el área vacía después de la transformación
)

# Ajustar el generador a los datos de entrenamiento
datagen.fit(X_train)

# Definir modelo
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(tamanio_img[0], tamanio_img[1], 1)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(clases), activation='softmax')  # Salida según número de clases
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(datagen.flow(X_train, y_train, batch_size=32), epochs=50, validation_data=(X_test, y_test))

#model.fit(X_train, y_train, epochs=50,batch_size=32, validation_data=(X_test, y_test))

# Guardar el modelo
model.save("gestos.keras")
model.save("gestos.h5")
