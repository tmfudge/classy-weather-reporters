import imp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import tensorflow as tf
from tensorflow import keras

import pathlib
import glob
import csv
saved_model = "appdata/Weather_model.h5"
Weather_model_trained = tf.keras.models.load_model(saved_model)




with open('appdata/classes.csv', newline='\n') as f:
    reader = csv.reader(f)
    classes = list(reader)
class_names = classes[0]



def weather_prediction (path,accuracy = False):
    
    img = Image.open(path).convert('RGB').resize([240,240])
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    prediction = Weather_model_trained.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    if accuracy:
        return([class_names[np.argmax(score)],np.max(score)])
    else:
        return(class_names[np.argmax(score)])
