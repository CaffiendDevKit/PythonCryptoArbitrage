'''
Created on 5 Mar. 2018

@author: Alex
'''
from connection import *

class CryptoArbitage():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getKeys(self):  
        '''
        Parses keys file and returns a dictionary with the key as the exchange name and the store a list of public and secret keys.
        '''   
        filename = "keys"  
        try:
            keys = open(filename, 'r+')
        except FileNotFoundError:
            print("Keys file not found")
        else:
            #===================================================================
            # Maybe change this to a loop that looks for headers then decides if the next line is
            # a key or secret. Could also be used to find what exchange the keys are for.
            # 
            #===================================================================
            exchange = keys.readline().rstrip()
            apiHeader = keys.readline().rstrip()
            apiKey = keys.readline().rstrip()
            secretHeader = keys.readline().rstrip()
            secretKey = keys.readline().rstrip()
            
        keys.close()
        return({exchange:[apiKey,secretKey]})
    
        
if __name__ == '__main__': 
    crypto = CryptoArbitage()
    
    binance = Connection("Binance")
    binance.setKeys(crypto.getKeys())
    
    print('Welcome to Crypto Arbitage made with python')
    print('Arbitage is taking three coin pairs and seeing if a profit can be made trading between them')
    print('Please enter the coin pair to search for')
    
    #===========================================================================
    # coin1 = input("Coin pair 1:")
    # coin2 = input("Coin pair 2:")
    # coin3 = input("Coin pair 3:")
    # 
    # coin1 = CoinPair(coin1)
    # coin2 = CoinPair(coin2)
    # coin3 = CoinPair(coin3)
    #===========================================================================
    
    #For testing
    coin1Name="ETHBTC"
    coin2Name="LTCETH"
    coin3Name="LTCBTC"
    
    coin1 = CoinPair(coin1Name)
    coin2 = CoinPair(coin2Name)
    coin3 = CoinPair(coin3Name)

    coin1.setPrice(binance.getCoinPrice(coin1Name))
    coin2.setPrice(binance.getCoinPrice(coin2Name))
    coin3.setPrice(binance.getCoinPrice(coin3Name))
    
    print("Coin Pair: {} - Price: {}".format(coin1.getName(), coin1.price))
    print("Coin Pair: {} - Price: {}".format(coin2.getName(), coin2.price))
    print("Coin Pair: {} - Price: {}".format(coin3.getName(), coin3.price))
    
    #===========================================================================
    # Production code
    # coin1.setPrice(binance.getCoinPrice(coin1.getName()))
    # coin2.setPrice(binance.getCoinPrice(coin2.getName()))
    # coin3.setPrice(binance.getCoinPrice(coin3.getName()))
    #===========================================================================