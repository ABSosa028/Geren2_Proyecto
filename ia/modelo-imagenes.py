import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from sklearn.model_selection import train_test_split

ruta_base = "datos"
tamanio_img = (28, 28)

imagenes = []
etiquetas = []

for etiqueta in range(10):
    carpeta = os.path.join(ruta_base, str(etiqueta))
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".png"):
            img_path = os.path.join(carpeta, archivo)
            img = load_img(img_path, color_mode='grayscale', target_size=tamanio_img)
            img_array = img_to_array(img) / 255.0
            imagenes.append(img_array)
            etiquetas.append(etiqueta)

X = np.array(imagenes).reshape(-1, 28, 28, 1)
y = np.array(etiquetas)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir y entrenar modelo
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Guardar el modelo
model.save("modelo_numeros_custom.keras")
model.save("modelo_numeros_custom.h5")
#model.export("modelo_numeros_customizer")
