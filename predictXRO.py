from predict import Predictor
from loadPercentJson import loadPercentJsonAsTensor, loadJsonAsTensor
import numpy as np
predicator = Predictor("XRO")

(x,y) = loadPercentJsonAsTensor("XRO")

reserve = 100
# Reserve 10,000 samples for validation
x = x[-reserve:]
y = y[-reserve:]
print(x)

pY = predicator.predict(x)

stats = [[0,0], [0,0]]

for i in range(len(pY)):
    j = int(y[i][3] >= 0)
    k = int(pY[i][3] >= 0)
    stats[j][k] += pY[i][3]
    print(stats)
    # if(y[i] >= 0):
    #     if()

    # print("Predict:")
    # print(pY[i])
    # print("Expect:")
    # print(y[i])
    # print("Dif")
    # print(y[i]-pY[i])
    # print("TotalDif")
    # print( np.sum(y[i]-pY[i]) )


print(np.sum(y-pY))