import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import json
from loadPercentJson import loadPercentJsonAsTensor, loadJsonAsTensor 
from tensorflow.keras.models import load_model
import numpy as np
amountOfDays = 3
oneHotSize = 8
from loadTraining import loadTraining
import random
import math
import threading
import time
import os
import sys


(xD,yD) = loadTraining("discreteHot", "trainingValue/")

class CustomCallback(keras.callbacks.Callback):
    def __init__(self):
        self.loss = 1000

    def on_train_end(self, logs=None):
        keys = list(logs.keys())
        self.loss = logs["loss"]
    

    def getLoss(self):
        return self.loss
    


run = True

def sig1(x):
    y = tf.nn.sigmoid(x)
    return 2*y - 1

def trainCharacteristic(name, suffix, characteristicIndex, callbacks):
    global run
    try:
        model = load_model(name + suffix, custom_objects={'sig1': sig1})
        print(model)
        print("Loaded")
    except:
        
        inputs = keras.Input(shape=(4*amountOfDays*oneHotSize,), name="Stonks")
        x = layers.Dense(40, activation=tf.nn.sigmoid, name="dense_1")(inputs)
        x = layers.Dense(30, activation=tf.nn.sigmoid, name="dense_2")(x)
        outputs = layers.Dense(1, activation=tf.nn.sigmoid, name="predictions")(x)

        model = keras.Model(inputs=inputs, outputs=outputs)
        model.save(name + suffix)
        print("New")



    model.summary()

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.1),  # Optimizer
        # Loss function to minimize
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    )




    x = xD
    y = yD[:,characteristicIndex]

    print(x.shape)
    print(y.shape)

    while(run):
        x_train = x
        y_train = y
        history = model.fit(
            x_train,
            y_train,
            batch_size=600,
            epochs=1,
            verbose=1,
            #callbacks=callbacks
        )
        print()
        print("Saved")
        print()
        model.save(name+suffix)  # creates a HDF5 file 'my_model.h5'
        if(not run):
            return
    

name = "discrete/"

import os, errno

try:
    os.makedirs(name)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


threads = []
callbacks = []

def report(callbacks):
    global run
    print("Start")
    while(run):
        print("report")
        for i in range(len(callbacks)):
            callback = callbacks[i]
            print(str(i) + ": " + str(callback.getLoss())) 
        print(len(xD))
        time.sleep(1)
        


print (sys.argv)
i = int(sys.argv[1])
suffix = "_" + str(i) + ".h5"
callback = CustomCallback()
trainCharacteristic(name, suffix, i, [callback])
