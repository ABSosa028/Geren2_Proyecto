import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from sklearn.model_selection import train_test_split

ruta_base = "gestos"  # << Cambiado de "datos" a "gestos"
tamanio_img = (64, 64)  # Puedes ajustar esto, 64x64 da mejores resultados para rostros/gestos
clases = sorted(os.listdir(ruta_base))  # Detecta clases automáticamente

imagenes = []
etiquetas = []

for i, clase in enumerate(clases):
    carpeta = os.path.join(ruta_base, clase)
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(carpeta, archivo)
            img = load_img(img_path, color_mode='grayscale', target_size=tamanio_img)
            img_array = img_to_array(img) / 255.0
            imagenes.append(img_array)
            etiquetas.append(i)

# Convertir a arrays
X = np.array(imagenes).reshape(-1, tamanio_img[0], tamanio_img[1], 1)
y = np.array(etiquetas)

# Dividir
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Guardar el modelo
model.save("modelo_gestos_custom.keras")
model.save("modelo_gestos_custom.h5")
