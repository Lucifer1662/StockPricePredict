
import numpy as np

def loadTraining(name:str, path = "training/"):
    x = np.load(path+name+"x.npy")
    y = np.load(path+name+"y.npy")
    return (x,y)