from enum import Enum
import numpy as np

class Action(Enum):
    Buy = 0
    Sell = 1
    UKNOWN = 2


def buyOrSellOrNeither(data: np.ndarray, future: np.ndarray):
    fudge = 0.1
    (open, high, low, close, volume) = tuple(future.tolist())
    [lastOpen, lastHigh, lastLow, lastClose, lastVolume] = tuple(data[len(data)-5:].tolist())
    if(close+fudge >= lastClose):
        return Action.Buy
    elif(close-fudge <= lastClose):
        return Action.Sell


class BuyOrSell:
    def __init__(self, predictor):
        self.predictor = predictor

    def buyOrSellOrNeither(self, data : np.ndarray):
        future = self.predictor.predict(data, 2)
        return buyOrSellOrNeither(data, future)

    
        

    
