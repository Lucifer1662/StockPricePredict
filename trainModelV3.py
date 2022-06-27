import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import json
from loadPercentJson import loadPercentJsonAsTensor, loadJsonAsTensor 
from tensorflow.keras.models import load_model
import numpy as np
amountOfDays = 10
from loadTraining import loadTraining
import random
import math
import threading
import time
import os


(xD,yD) = loadTraining("1")

class CustomCallback(keras.callbacks.Callback):
    def __init__(self):
        self.loss = 1000

    def on_train_end(self, logs=None):
        keys = list(logs.keys())
        self.loss = logs["loss"]
    

    def getLoss(self):
        return self.loss
    


run = True

def trainCharacteristic(name, suffix, characteristicIndex, callbacks):
    global run
    try:
        model = load_model(name + suffix)
        print(model)
    except:
        inputs = keras.Input(shape=(5*amountOfDays,), name="Stonks")
        x = layers.Dense(35, activation=tf.nn.sigmoid, name="dense_1")(inputs)
        x = layers.Dense(15, activation=tf.nn.sigmoid, name="dense_2")(x)
        outputs = layers.Dense(1, activation=tf.nn.sigmoid, name="predictions")(x)

        model = keras.Model(inputs=inputs, outputs=outputs)
        model.save(name + suffix)



    model.summary()

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.00001),  # Optimizer
        # Loss function to minimize
        loss=keras.losses.MSE,
        
    )



    

    def sigmoid(x):
        return 1/(1 + np.exp(-x)) 


    def sigmoidInverse(x):
        return np.log(x/(1-x))

    x = xD
    y = yD[:,characteristicIndex]

    #y = sigmoid(yD)

    # use = 10000

    # splits = math.floor(len(x)/use)
    # x = x[:splits*use]
    # y = y[:splits*use]
    # x_splits = np.split(x, splits)
    # y_splits = np.split(y, splits)
    while(run):
        x_train = x
        y_train = y
        history = model.fit(
            x_train,
            y_train,
            batch_size=6000,
            epochs=10,
            verbose=1,
            callbacks=callbacks
        )
        model.save(name+suffix)  # creates a HDF5 file 'my_model.h5'
        if(not run):
            return
    

name = "version2/"

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
        



i = 2
suffix = "_" + str(i) + ".h5"
callback = CustomCallback()
trainCharacteristic(name, suffix, i, [callback])
