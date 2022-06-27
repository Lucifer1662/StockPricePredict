import numpy as np
import random

from discretePercent import getNormalizeFileNames 
from loadPercentJson import loadFromFile, toList, splitIntoTraining

def createTrainingData(days, filter_pred = None):
    fileNames = getNormalizeFileNames()
    if(filter_pred != None):
        fileNames = filter(filter_pred, fileNames)
    xs = []
    ys = []
    for fileName in fileNames:
        data = loadFromFile(fileName, "discrete")
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
    xNP.astype("int8")
    yNP.astype("int8")


    return (xNP, yNP)



(x,y) = createTrainingData(3)
np.save("trainingValue/discretex", x)
np.save("trainingValue/discretey", y)