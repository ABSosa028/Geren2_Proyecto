import tensorflow as tf
import os

import numpy as np
from PIL import Image



# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess the data
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Build the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=3)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

ruta = f'modelos'
os.makedirs(ruta, exist_ok=True)

model.save('modelos/numeros.keras')



# Cargar imagen y convertir a escala de grises
img = Image.open('datasets/numeros/1/1_1746303351059.png').convert('L')  # 'L' = grayscale

# Redimensionar a 28x28
img = img.resize((28, 28))

# Convertir a arreglo de numpy
img_array = np.array(img)

# Invertir colores si es necesario (MNIST tiene fondo negro y dígitos blancos)
img_array = 255 - img_array

# Normalizar valores [0, 1]
img_array = img_array / 255.0

# Expandir dimensiones para que coincida con el batch (1, 28, 28, 1)
img_array = img_array.reshape(1, 28, 28, 1)

# Hacer la predicción
prediccion = model.predict(img_array)
digito_predicho = np.argmax(prediccion)

print("El modelo predice que el dígito es:", digito_predicho)