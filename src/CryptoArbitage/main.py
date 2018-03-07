'''
Created on 5 Mar. 2018

@author: Alex
'''
import connection

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
if __name__ == '__main__':
    print('Welcome to Crypto Arbitage made with python')
    print('Arbitage is taking three coins and seeing if a profit can be made trading between them')
    print('Please enter the coins to search for')
    #===========================================================================
    # coin1 = input("Coin 1:")
    # coin2 = input("Coin 2:")
    # coin3 = input("Coin 3:")
    #===========================================================================
    
    binance = connection.Connection()
    