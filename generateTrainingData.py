from createTrainingData import createTrainingData
import numpy as np

(x,y) = createTrainingData(10)
np.save("trainingValue/1x", x)
np.save("trainingValue/1y", y)