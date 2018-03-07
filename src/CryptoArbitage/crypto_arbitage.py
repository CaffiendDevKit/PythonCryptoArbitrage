'''
Created on 5 Mar. 2018

@author: Alex
'''
import connection

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
    print('Welcome to Crypto Arbitage made with python')
    print('Arbitage is taking three coins and seeing if a profit can be made trading between them')
    print('Please enter the coins to search for')
    #===========================================================================
    # coin1 = input("Coin 1:")
    # coin2 = input("Coin 2:")
    # coin3 = input("Coin 3:")
    #===========================================================================
    
    crypto = CryptoArbitage()
    
    binance = connection.Connection("Binance")
    binance.setKeys(crypto.getKeys())
    