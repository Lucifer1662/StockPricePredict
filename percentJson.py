import json 
import sys
#Comma separated Ticker, Date, Open, High, Low, Close, Volume.
from os import walk
from filesInPath import filesInPath
fileName = "XRO"


def getDataFromFile(fileName):
    f = open("data/" + fileName + ".json", "r")    

    return json.load(f)

def percentageChange(start, end):
    if(start == 0):
        return 0
    return (end - start)/start 

def toPercentageChange(data : dict):

    keysView = data.keys()
    keys = []
    for key in keysView:
        keys.append(key)
    keys.sort()
    prevKey = keys[0]
    prevData = data[prevKey]

    percentDatas = {}

    for key in keys[1:]:
        (prevOpen, prevHigh, prevLow, prevClose, prevVolume) = prevData

        (open, high, low, close, volume) = data[key]

        percentDatas[key] = (percentageChange(prevOpen, open),
        percentageChange(prevHigh, high),
        percentageChange(prevLow, low),
        percentageChange(prevClose, close),
        percentageChange(prevVolume, volume))

        prevData = data[key]
       
    return percentDatas


        

def normalizeData(data:dict):
    for key in data:
        (open, high, low, close, volume) = data[key]
        

def saveToFile(fileName, data:dict):
    jsonFile = open("percentData/"+fileName+".json", "w+")
    jsonFile.write(json.dumps(data))


def percentJson(fileNames):
    for fileName in fileNames:
        data = getDataFromFile(fileName)
        dataPercent = toPercentageChange(data)
        saveToFile(fileName, dataPercent)


def getPercentFileNames():
    return list(map(lambda fileName:fileName.replace(".json",""),
        filesInPath("percentData")))


percentJson(["IOO"])