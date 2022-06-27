import json 
import sys
import math
#Comma separated Ticker, Date, Open, High, Low, Close, Volume.
from os import walk
from filesInPath import filesInPath




def getDataFromFile(fileName):
    f = open("percentData/" + fileName + ".json", "r")    

    return json.load(f)

def discretize(value, divisions):
    for i in range(0, len(divisions)):
        div = divisions[i]
        if(value < div):
            return i
    return i



def discretizeData(data, divisions):
    dataNormalize = {}
    for key in data:
        (open, high, low, close, volume) = data[key]
        dataNormalize[key] = (
            discretize(open, divisions),
            discretize(high, divisions),
            discretize(low, divisions),
            discretize(close, divisions)
            )
    return dataNormalize


        

        

def saveToFile(fileName, data):
    jsonFile = open("discrete/"+fileName+".json", "w+")
    jsonFile.write(json.dumps(data))



def getNormalizeFileNames():
    return map(lambda fileName:fileName.replace(".json",""),
        filesInPath("data"))

def normalizeJson(fileNames, divisions):
    for fileName in fileNames:
        data = getDataFromFile(fileName)
        dataDiscrete = discretizeData(data, divisions)
        saveToFile(fileName, dataDiscrete)


normalizeJson(getNormalizeFileNames(),[-0.3,-0.1,-0.03,0,0.03,0.1,0.3,100])