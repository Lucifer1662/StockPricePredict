from createTrainingData import createTrainingData
import numpy as np



etfsNames = ["ACDC","NDQ","VAS","IOO"]

def onlyEtfs(name:str):
    try:
        etfsNames.index(name)
        print(name)
        return True
    except:
        return False


(x,y) = createTrainingData(10, onlyEtfs)


np.save("trainingValue/etfx", x)
np.save("trainingValue/etfy", y)