from google.colab import drive
drive.mount('/content/drive')

%cd "/content/drive/MyDrive/ArtStyleClassifier"
!ls

import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.applications.vgg16 import VGG16

from tensorflow.keras import optimizers
from tensorflow.keras import models
from tensorflow.keras import layers

base_dir = 'PaintingsDataset'
test_dir = os.path.join(base_dir, 'test')
new_model = tf.keras.models.load_model('ArtStyleModel_VGG16.keras')

test_datagen = ImageDataGenerator(1./255)
test_generator = test_datagen.flow_from_directory(
							test_dir,
							target_size = (150, 150),
							batch_size = 32,
							class_mode ='binary',
							)


test_loss_cnn, test_acc_cnn = new_model.evaluate(test_generator, steps=10)
print('\ntest acc :\n', test_acc_cnn)