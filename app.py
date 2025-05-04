import tensorflow as tf

new_model = tf.keras.models.load_model('modelos/numeros.h5')

#carga imagen de mi carpeta
img = tf.keras.preprocessing.image.load_img('datasets/numeros/1/1_1746303283982.png', target_size=(28, 28), color_mode='grayscale')

#print(new_model.predict('datasets/numeros/1/1_1746303283982.png').shape)
