import json 
import sys
import math
#Comma separated Ticker, Date, Open, High, Low, Close, Volume.
from os import walk
from filesInPath import filesInPath




def getDataFromFile(fileName):
    f = open("percentData/" + fileName + ".json", "r")    

    return json.load(f)

def normalize(value):
    return 1/(1 + math.exp(-value))  

def normalizePercent(data):
    dataNormalize = {}
    for key in data:
        (open, high, low, close, volume) = data[key]
        dataNormalize[key] = (normalize(open),
            normalize(high),
            normalize(low),
            normalize(close),
            normalize(volume))
       
    return dataNormalize


        

        

def saveToFile(fileName, data):
    jsonFile = open("normalize/"+fileName+".json", "w+")
    jsonFile.write(json.dumps(data))



def getNormalizeFileNames():
    return map(lambda fileName:fileName.replace(".json",""),
        filesInPath("normalize"))

def normalizeJson(fileNames):
    for fileName in fileNames:
        data = getDataFromFile(fileName)
        dataPercent = normalizePercent(data)
        saveToFile(fileName, dataPercent)


