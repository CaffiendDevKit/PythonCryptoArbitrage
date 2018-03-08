'''
Created on 6 Mar. 2018

@author: Alex
'''

class Trade():
    '''
    classdocs
    '''
    
    tradeType = ""
    orderPair = ""
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
        
    def setTradeType(self, tradeType):
        self.tradeType = tradeType
        
    def setOrderPair(self, orderPair):
        self.orderPair = orderPair
        
    def getTradeType(self):
        return(self.tradeType)
    
    def getOrderPair(self):
        return(self.orderPair)

class TriArbitrage():
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def isPossible(self, coinP1, coinP2, coinP3):    
        coins = set()
        coins.update([coinP1.getTopCoin(), coinP1.getBaseCoin()])
        coins.update([coinP2.getTopCoin(), coinP2.getBaseCoin()])
        coins.update([coinP3.getTopCoin(), coinP3.getBaseCoin()])
        
        nameCP1 = coinP1.getName()
        nameCP2 = coinP2.getName()
        nameCP3 = coinP3.getName()
        #=======================================================================
        # print(coins)
        # for i in coins:
        #     for y in coins:
        #         if i != y:
        #             for x in coins:
        #                 if y != x and i != x:
        #                     print("{}->{}->{}->{}".format(i,y,x,i))
        #=======================================================================
        
        
        sell = "Sell"
        buy = "Buy" 
        it = 0
        trades = dict()    
        for i in coins:
            listTrades = list()
            for y in coins:
                if i != y:
                    first = Trade()
                    test1 = i+y
                    if test1 == nameCP1:
                        print()
                        print("Order Type: Sell")
                        print("Order pair: {}".format(nameCP1))
                        first.setTradeType(sell)
                        first.setOrderPair(nameCP1)
                        listTrades.append(first)
                    elif test1 == nameCP2:
                        print()
                        print("Order Type: Sell")
                        print("Order pair: {}".format(nameCP2))
                        first.setTradeType(sell)
                        first.setOrderPair(nameCP2)
                        listTrades.append(first)
                    elif test1 == nameCP3:
                        print()
                        print("Order Type: Sell")
                        print("Order pair: {}".format(nameCP3))
                        first.setTradeType(sell)
                        first.setOrderPair(nameCP3)
                        listTrades.append(first)
                    test2 = y+i
                    if test2 == nameCP1:
                        print()
                        print("Order Type: Buy")
                        print("Order pair: {}".format(nameCP1))
                        first.setTradeType(buy)
                        first.setOrderPair(nameCP1)
                        listTrades.append(first)
                    elif test2 == nameCP2:
                        print()
                        print("Order Type: Buy")
                        print("Order pair: {}".format(nameCP2))
                        first.setTradeType(buy)
                        first.setOrderPair(nameCP2)
                        listTrades.append(first)
                    elif test2 == nameCP3:
                        print()
                        print("Order Type: Buy")
                        print("Order pair: {}".format(nameCP3))
                        first.setTradeType(buy)
                        first.setOrderPair(nameCP3)
                        listTrades.append(first)
                    for x in coins:
                        if y != x and i != x:
                            second = Trade()
                            test1 = y+x
                            if test1 == nameCP1:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP1))
                                second.setTradeType(sell)
                                second.setOrderPair(nameCP1)
                                listTrades.append(second)
                            elif test1 == nameCP2:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP2))
                                second.setTradeType(sell)
                                second.setOrderPair(nameCP2)
                                listTrades.append(second)
                            elif test1 == nameCP3:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP3))
                                second.setTradeType(sell)
                                second.setOrderPair(nameCP3)
                                listTrades.append(second)
                            test2 = x+y
                            if test2 == nameCP1:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP1))
                                second.setTradeType(buy)
                                second.setOrderPair(nameCP1)
                                listTrades.append(second)
                            elif test2 == nameCP2:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP2))
                                second.setTradeType(buy)
                                second.setOrderPair(nameCP2)
                                listTrades.append(second)
                            elif test2 == nameCP3:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP3))
                                second.setTradeType(buy)
                                second.setOrderPair(nameCP3)
                                listTrades.append(second)
                                
                            third = Trade()
                            test1 = x+i
                            if test1 == nameCP1:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP1))
                                third.setTradeType(sell)
                                third.setOrderPair(nameCP1)
                                listTrades.append(third)
                            elif test1 == nameCP2:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP2))
                                third.setTradeType(sell)
                                third.setOrderPair(nameCP2)
                                listTrades.append(third)
                            elif test1 == nameCP3:
                                print()
                                print("Order Type: Sell")
                                print("Order pair: {}".format(nameCP3))
                                third.setTradeType(sell)
                                third.setOrderPair(nameCP3)
                                listTrades.append(third)
                            test2 =i+x
                            if test2 == nameCP1:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP1))
                                third.setTradeType(buy)
                                third.setOrderPair(nameCP1)
                                listTrades.append(third)
                            elif test2 == nameCP2:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP2))
                                third.setTradeType(buy)
                                third.setOrderPair(nameCP2)
                                listTrades.append(third)
                            elif test2 == nameCP3:
                                print()
                                print("Order Type: Buy")
                                print("Order pair: {}".format(nameCP3))
                                third.setTradeType(buy)
                                third.setOrderPair(nameCP3)
                                listTrades.append(third)
                            print("{}->{}->{}->{}".format(i,y,x,i))
                            trades[it]=listTrades
                            it = it + 1
        print("Trades dict: {}".format(trades))
        if len(trades) > 0:
            return(True)
        else:
            return(False)
    
    def tryArbitrage(self, coinP1, coinP2, coinP3):
        #I have 1 BTC to trade with
        BTC = 1
        if(coinP1.baseCoin == "BTC"):
            #BTC - > ETH
            first = BTC/coinP1.price
            print("Amount of ETH: {}".format(first))
            
            #ETH - > LTC
            second= first/coinP2.price
            print("Amount of LTC: {}".format(second))
            #LTC -> BTC
            third = second/coinP3.price
            print("Amount of BTC: {}".format(third))
            
    
if __name__ == '__main__':
    #For unit testing
    from connection import *
    from crypto_arbitage import *
    from arbitrage import *
    
    #For testing
    
    tryArb = TriArbitrage()
    
    #===========================================================================
    # coin1Name="ETHBTC"
    # coin2Name="LTCETH"
    # coin3Name="LTCBTC"
    #===========================================================================
    
    coin1Name="ETHBTC"
    coin2Name="MTHETH"
    coin3Name="LTCBTC"
    
    coin1 = CoinPair(coin1Name)
    coin2 = CoinPair(coin2Name)
    coin3 = CoinPair(coin3Name)

    coin1.setPrice(0.7)
    coin2.setPrice(0.2)
    coin3.setPrice(1.5)
    #===========================================================================
    # coin2.setPrice(binance.getCoinPrice(coin2Name))
    # coin3.setPrice(binance.getCoinPrice(coin3Name))
    #===========================================================================
    #===========================================================================
    # tryArb.tryArbitrage(coin1, coin2, coin3)
    #===========================================================================
    
    tryArb.isPossible(coin1, coin2, coin3)
    