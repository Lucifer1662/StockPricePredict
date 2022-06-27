import numpy as np

def loadTraining(name:str, path = "training/"):
    x = np.load(path+name+"x.npy")
    y = np.load(path+name+"y.npy")
    return (x,y)


(x,y) = loadTraining("discrete","trainingValue/")



x.astype("int8")
y.astype("int8")


def toHotOne(h):
    w = np.zeros((h.shape[0],h.shape[1],8),dtype=int)
    for i in range(0, len(h)):
        a = h[i]
        size = a.size
        b = np.zeros((size, 8))
        for j in range(len(a)):
            b[j, a[j]] = 1
        w[i] = b

    return w

    
np.save("trainingValue/discreteHotx", toHotOne(x))
np.save("trainingValue/discreteHoty", toHotOne(y))

