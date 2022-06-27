import numpy as np
from loadPercentJson import loadPercentJsonAsTensor, loadFromFile, toList
from BuyOrSell import BuyOrSell, buyOrSellOrNeither, Action
from predict import Predictor

(x,y) = loadPercentJsonAsTensor("XRO")

def controlCase():
    xa = toList(loadFromFile("XRO", "data"))
    closeIndex = 3

    principal = 10000
    startingStockPrice = xa[0][closeIndex]
    endingStockPrice = xa[-1][closeIndex]
    print(startingStockPrice)
    print(endingStockPrice)

    percentage = (endingStockPrice - startingStockPrice)/startingStockPrice 
    endMoney = principal + percentage * principal

    print("Principal")
    print(principal)
    print("Result")
    print(endMoney)

controlCase()




stats = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]



def percentageCorrect(stats : list):
    totalCorrect = 0
    total = 0
    for i in range(len(stats)):
        totalCorrect += stats[i][i]
        for j in range(len(stats[i])):
            total += stats[i][j]

    return totalCorrect/total




def beatTheMarket(xa,x,y,buyOrSell, principal = 10000):
    money = principal
    closeIndex = 3
    stocks = 0

    stock_price = xa[0][closeIndex]
    stocks_bought =  money/stock_price
    price_paid = stocks_bought * stock_price
    stocks += stocks_bought
    money -= price_paid


    for ((open, high, low, close, volume), data, future) in zip(xa, x, y):
        action = buyOrSell(data, future)
        print(money + stocks * close)
        if(money > 0 and action == Action.Buy):
            stock_price = close
            stocks_bought =  money/stock_price
            price_paid = stocks_bought * stock_price
            stocks += stocks_bought
            money -= price_paid
        if(stocks > 0 and action == Action.Sell):
            stock_price = close
            stocks_sold =  stocks
            price_sold = stocks_sold * stock_price
            stocks -= stocks_sold
            money += price_sold
    

    last = xa[-1]
    stock_price = last[closeIndex]
    money += stocks * stock_price
    stocks = 0

    print("Principal")
    print(principal)


    print("Result")
    print(money)

xa = toList(loadFromFile("XRO", "data"))

beatTheMarket(xa, x, y, buyOrSellOrNeither)   

def beatTheMarketPred(xa,x, predicator, principal = 10000):
    money = principal
    closeIndex = 3
    stocks = 0

    stock_price = xa[0][closeIndex]
    stocks_bought =  money/stock_price
    price_paid = stocks_bought * stock_price
    stocks += stocks_bought
    money -= price_paid


    for ((open, high, low, close, volume), data) in zip(xa, x):
        action = predicator.buyOrSellOrNeither(data)
        print(money + stocks * close)
        if(money > 0 and action == Action.Buy):
            stock_price = close
            stocks_bought =  money/stock_price
            price_paid = stocks_bought * stock_price
            stocks += stocks_bought
            money -= price_paid
        if(stocks > 0 and action == Action.Sell):
            stock_price = close
            stocks_sold =  stocks
            price_sold = stocks_sold * stock_price
            stocks -= stocks_sold
            money += price_sold
    

    last = xa[-1]
    stock_price = last[closeIndex]
    money += stocks * stock_price
    stocks = 0

    print("Principal")
    print(principal)


    print("Result")
    print(money)

buyOrSell = BuyOrSell(Predictor("XRO"))
beatTheMarketPred(xa, x, buyOrSell)    

# for (data, future) in zip(x, y):
#     predict = buyOrSell.buyOrSellOrNeither(data)
#     correct = buyOrSellOrNeither(data, future)
#     stats[predict.value][correct.value] += 1
#     print(stats)
#     print( str(percentageCorrect(stats) * 100) + "%")




# print(stats)