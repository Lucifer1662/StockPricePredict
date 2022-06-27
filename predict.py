from tensorflow.keras.models import load_model
from tensorflow import keras
import numpy as np

def sigmoidInverse(x):
    return np.log(x/(1-x))

class Predictor:
    def __init__(self, name:str):
        self.model = load_model(name+".h5")
        self.model.compile(
            optimizer=keras.optimizers.Adam(),  # Optimizer
            # Loss function to minimize
            loss=keras.losses.categorical_crossentropy,
            )
    
    def predict(self, x : np.ndarray, n=1):
        newX = x
        if(len(x.shape) == 1):
            newX = np.array([x])
            print("here")

        for i in range(n):
            res = self.model.predict(newX)
            #np.append(newX, res)
        
        res = sigmoidInverse(res)

        if(len(x.shape) == 1):
            return res[0]
        else:
            return res

    def evaluate(self, x,y):
        pY = self.predict(x)
        
        return self.valuate(y, pY)
    
    def valuate(self, y, py):
        return 0

        