from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f'X train shape:{x_train.shape}')
print(f'X test shape:{x_test.shape}')
print(f'Y train shape:{y_train.shape}')
print(f'Y test shape:{y_test.shape}')

x_train = x_train/255.0
x_test = x_test/255.0

mnist_model = Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.InputLayer(748),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax'),
])

mnist_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

mnist_model.summary()


epochs=34
history = mnist_model.fit(
  x=x_train,
  y=y_train,
  validation_data=(x_test, y_test),
  epochs=epochs)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

fig, ax = plt.subplots(1,2)
ax[0].plot(epochs_range, acc, label='Training Accuracy')
ax[0].plot(epochs_range, val_acc, label='Validation Accuracy')
ax[1].plot(epochs_range, loss, label='Training Loss')
ax[1].plot(epochs_range, val_loss, label='Validation Loss')
ax[0].set_title('Training and Validation Accuracy')
ax[1].set_title('Training and Validation Loss')
ax[0].legend(loc='lower right')
ax[1].legend(loc='upper right')
fig.suptitle('Training and Validation Accuracy')
fig.savefig('drop_accuracy.png')
plt.show()
