
from predictor import Predictor
from loadTraining import loadTraining
import numpy as np
import random
predictor = Predictor("version2/_2")


(xD,yD) = loadTraining("1", "trainingValue/")

size = len(xD)
x = xD[:]
y = xD[:,2]

py = predictor.predict(x)
print(py)
print(xD)
areSamePositive = 0
areSameNegative = 0
numPositive = np.count_nonzero(y > 0)
numNegative = np.count_nonzero(y < 0)
isAboveThreshholdCorrect = 0
isAboveThreshholdWrong = 0
isAboveThreshhold = 0
threshhold = 0.5

notAboveThresholdButThoughtitWas = 0

totalpercent = 0
numPredictOverThreshold = 0

totalPercentRandom = 0
numPredictOverThresholdRandom = 0

totoalpercentUp = 0
numPercentUp = 0

data = []

i = 0
for (z,w) in zip(y,py):
    if(z < 0 and w < 0):
        areSameNegative += 1
    if(z > 0 and w > 0):
        areSamePositive += 1

    if(z > threshhold):
        isAboveThreshhold += 1
        if w > threshhold:
            isAboveThreshholdCorrect += 1
            data.append(xD[i][:45])
        else:
            isAboveThreshholdWrong += 1
            
        
    else:
        if w > threshhold:
            notAboveThresholdButThoughtitWas += 1
           
    


    if w > threshhold:
        totalpercent += z
        numPredictOverThreshold += 1
        print(z)
    
    if random.choice([True, False]) :
        totalPercentRandom += z
        numPredictOverThresholdRandom += 1

    if(xD[i][49-2] > threshhold):
        totoalpercentUp += z
        numPercentUp += 1

    i += 1
    


numWrong = size - areSamePositive - areSameNegative
# print(data)
# print(xD[0][49-3])
# print(yD[0])
print(isAboveThreshhold)
print(isAboveThreshholdCorrect)
print(isAboveThreshholdWrong)
print(notAboveThresholdButThoughtitWas)
print(totalpercent/numPredictOverThreshold)
print(totalPercentRandom/numPredictOverThresholdRandom)
print(totoalpercentUp/numPercentUp)
print("Total Sample:" + str(size))

print("Total Correct Positive:" + str(areSamePositive))
print("Total Correct Negative:" + str(areSameNegative))
print("Total Wrong:" + str(numWrong))

print("Postive Correct:" + str(areSamePositive/numPositive * 100) + "%")
print("Negative Correct:" + str(areSameNegative/numNegative * 100) + "%")

print("Total Correct:" + str(((areSamePositive + areSameNegative) / size) * 100) + "%")

