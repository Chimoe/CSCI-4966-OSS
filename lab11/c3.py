from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras


from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-pic/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)


test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)

# First custom


pic = Image.open("ponto.jpg").convert('L')
pic.save('g1.png')
pic = Image.open("g1.png")
pic = pic.resize((28, 28))
pic.save('g1.png')
pic=ImageOps.invert(pic)

subject = np.array(pic) / 255

test = model.predict(np.expand_dims(subject, 0))

result = np.argmax(test)
print(class_names[result])

# Second custom

pic = Image.open("LO.png").convert('L')
pic.save('g2.png')
pic = Image.open("g2.png")
pic = pic.resize((28, 28))
pic.save('g2.png')
pic=ImageOps.invert(pic)

subject = np.array(pic) / 255

test = model.predict(np.expand_dims(subject, 0))

result = np.argmax(test)
print(class_names[result])

# Third custom

pic = Image.open("yeezy.jpg").convert('L')
pic.save('g3.png')
pic = Image.open("g3.png")
pic = pic.resize((28, 28))
pic.save('g3.png')
pic=ImageOps.invert(pic)

subject = np.array(pic) / 255

test = model.predict(np.expand_dims(subject, 0))

result = np.argmax(test)
print(class_names[result])