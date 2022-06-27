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
name = "version3"

try:
    model = load_model(name + '.h5')
    print(model)
except:
    inputs = keras.Input(shape=(5*amountOfDays,), name="Stonks")
    x = layers.Dense(35, activation=tf.nn.sigmoid, name="dense_1")(inputs)
    x = layers.Dense(15, activation=tf.nn.sigmoid, name="dense_2")(x)
    outputs = layers.Dense(5, activation=tf.nn.sigmoid, name="predictions")(x)

    model = keras.Model(inputs=inputs, outputs=outputs)
    model.save(name + '.h5')



model.summary()

model.compile(
    optimizer=keras.optimizers.SGD(),  # Optimizer
    # Loss function to minimize
    loss=keras.losses.MSE,
)



(x,y) = loadTraining("1")

def sigmoid(x):
    return 1/(1 + np.exp(-x)) 


def sigmoidInverse(x):
    return np.log(x/(1-x))



y = sigmoid(y)

use = 10000

splits = math.floor(len(x)/use)
x = x[:splits*use]
y = y[:splits*use]
x_splits = np.split(x, splits)
y_splits = np.split(y, splits)

print(splits)
while(True):
    for i in range(len(x_splits)):
        x_train = x_splits[i]
        y_train = y_splits[i]
        print("Fit model on training data")
        history = model.fit(
            x_train,
            y_train,
            batch_size=64,
            epochs=10,
            # We pass some validation for
            # monitoring validation loss and metrics
            # at the end of each epoch
            # validation_data=(x_val, y_val),
        )

        model.save(name+'.h5')  # creates a HDF5 file 'my_model.h5'

