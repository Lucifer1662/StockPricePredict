import json 
import sys
#Comma separated Ticker, Date, Open, High, Low, Close, Volume.
from os import walk
import numpy as np



def loadFromFile(fileName, path):
    jsonFile = open(path+"/"+fileName+".json", "r")
    return json.load(jsonFile)

def toList(data : dict):

    keysView = data.keys()
    keys = []
    for key in keysView:
        keys.append(key)
    keys.sort()

    percentDatas = []
    for key in keys[1:]:
        percentDatas.append(data[key])

    return percentDatas



def toTensor(data : list):
    dataArray = np.array(data)
    print(dataArray.shape)
    return dataArray

def splitIntoTraining(data : list):
    exampleXs = []
    exampleYs = []

    amountOfDays = 3
    for i in range(len(data)):
        if(i + amountOfDays < len(data)):
            exampleYs.append(data[i+amountOfDays])

            exampleX = []
            for j in range(amountOfDays):

                exampleX.extend(data[i+j])
            exampleXs.append(exampleX)

    return (exampleXs, exampleYs)
            


        

def loadPercentJsonAsTensor(fileName:str):
    data = loadFromFile(fileName, "percentData")
    data = toList(data)
    (x, y) = splitIntoTraining(data)
    
    xNP = np.array(x)
    yNP = np.array(y)
    xNP.astype("float32")
    yNP.astype("float32")

    print(xNP.shape)
    print(yNP.shape)

    return (xNP, yNP)


def loadJsonAsTensor(fileName: str):
    data = loadFromFile(fileName, "data")
    data = toList(data)
    (x, y) = splitIntoTraining(data)

    
    xNP = np.array(x)
    yNP = np.array(y)
    xNP.astype("float32")
    yNP.astype("float32")

    print(xNP.shape)
    print(yNP.shape)
    
    return (xNP, yNP)