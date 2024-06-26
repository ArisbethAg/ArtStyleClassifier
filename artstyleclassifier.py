# -*- coding: utf-8 -*-
"""ArtStyleClassifier_V7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q_hduAIobzHQwiMTtKxmyj1YquqS9-zy
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd "/Users/arisbethaguirre/Downloads/PaintingsDataset"
!ls

import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


base_dir = "/Users/arisbethaguirre/Downloads/PaintingsDataset"
train_dir = os.path.join(base_dir,'train')
test_dir = os.path.join(base_dir, 'test')
val_dir = os.path.join(base_dir, 'validation')

train_datagen = ImageDataGenerator(
							rescale = 1./255,
							rotation_range = 20,
							horizontal_flip = True,
							brightness_range=(1,0.8),
							vertical_flip = True,
							)

train_generator = train_datagen.flow_from_directory(
							train_dir,
							target_size = (150, 150),
							batch_size = 32,
							class_mode ='binary',
							)
val_datagen = ImageDataGenerator(
							rescale = 1./255,
							)

val_generator = val_datagen.flow_from_directory(
							val_dir,
							target_size = (150, 150),
							batch_size = 32,
							class_mode ='binary',
							)

images , labels = train_generator[0]

from tensorflow.keras.applications.vgg16 import VGG16

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import regularizers

base_model = VGG16(weights="imagenet", include_top=False, input_shape=(150,150,3), pooling="avg")
base_model.trainable = False

model = models.Sequential()
model.add(base_model)
model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu', kernel_regularizer=regularizers.l2(0.012)))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',
						optimizer="Adam",
						metrics=['acc'])

model.build(input_shape=(None, 150, 150, 3))  # Llama a build con la forma de entrada

model.summary()

history = model.fit(
						train_generator,
						validation_data=val_generator,
						epochs = 10)

acc = history.history['acc']
loss = history.history['loss']
val_acc = history.history['val_acc']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

plt.plot(epochs,acc,'bo',label='train accuracy')
plt.title('train acc')
plt.legend()

plt.figure()

plt.plot(epochs,loss, 'bo', label ='training loss')
plt.title('train loss')
plt.legend()

plt.show()

model.save("/Users/arisbethaguirre/Downloads/ArtStyleModels/refined/ArtStyleModel_VGG16_new.h5")