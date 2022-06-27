import numpy as np
import random

from percentJson import getPercentFileNames 
from loadPercentJson import loadFromFile, toList, splitIntoTraining

def createTrainingData(days, filter_pred = None):
    fileNames = getPercentFileNames()
    if(filter_pred != None):
        fileNames = filter(filter_pred, fileNames)
    xs = []
    ys = []
    for fileName in fileNames:
        data = loadFromFile(fileName, "percentData")
        print(fileName)
        if(len(data) >= days):
            data = toList(data) 
            (x, y) = splitIntoTraining(data)

            # c = min(count, len(x))
            # x = random.choices(x, k=c)
            # y = random.choices(y, k=c)
            xs.extend(x)
            ys.extend(y)

    s = list(zip(xs,ys))
    random.shuffle(s)
    z = list(zip(*s)) 
    xs = z[0]
    ys = z[1]



    xNP = np.array(xs)
    yNP = np.array(ys)
    xNP.astype("float32")
    yNP.astype("float32")

    def sigmoid(x):
        return 1/(1 + np.exp(-x)) 

    # yNP = yNP * 10
    # yNP = sigmoid(yNP)
    
    # xNP =  np.clip(xNP, -1, 1)
    # xNP = (xNP+1)/2
    # yNP =  np.clip(yNP, -1, 1)
    # yNP = (yNP+1)/2

    return (xNP, yNP)