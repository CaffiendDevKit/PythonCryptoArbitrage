'''
Created on 6 Mar. 2018

@author: Alex

This Module is used to manage the connection and API commands of several exchanges.
'''
import urllib.request #used for URL requests #used to get UTC time for API
import hmac
import hashlib
import json

class Connection():
    '''
    classdocs
    '''
    
    EXCHANGE = "None"
    SECRETKEY = ""
    PUBLICKEY = ""
    
    def setKeys(self, keys):
        '''
        dict{exchange[public:secret]} -> none
        used to set the public and private keys class variables.
        '''
        keysList = keys[self.EXCHANGE]
        self.PUBLICKEY = keysList[0]
        self.SECRETKEY = keysList[1]
    
    def serverTimeConvert(self, time):
        '''
        bytes -> str
        Takes a bytes string and returns a string.
        designed to take binance api server time response and convert it to a string for url requests.
        '''
        if(self.EXCHANGE == "Binance"):
            time = time.decode('UTF-8')
            string,strTime = time.split(":")
            strTime = strTime.strip('}')
            return(strTime)
        else:
            #Throw error here
            return("0")
    
    def testConnection(self):
        '''
        Test if there is a connection possible with api
        Returns True if connection is made
        Returns False if no connection is made
        '''
        if(self.EXCHANGE == "Binance"):
            contents = urllib.request.urlopen("https://api.binance.com/api/v1/ping").read()
            contents = contents.decode('UTF-8') #Changes from byte literal string to string https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
            if (contents != "{}"):
                return(False)
            else:
                return(True)
            
        else:
            return(False)
        
    def getServerTime(self):
        if(self.EXCHANGE == "Binance"):
            return(urllib.request.urlopen("https://api.binance.com/api/v1/time").read())
        
    def getAccountInfo(self,serverTime):
        if(self.EXCHANGE == "Binance"):
            request = bytes('timestamp={}'.format(serverTime), 'UTF-8')
            secret = bytes(self.SECRETKEY, 'UTF-8')
            h = hmac.new( secret, request, hashlib.sha256 ) #creates HMAC SHA256 signature for request.
            requestUrl = "https://api.binance.com/api/v3/account?" \
                + 'timestamp={}'.format(serverTime) \
                + '&signature={}'.format(h.hexdigest())
              
            publicKeyHeader = {"X-MBX-APIKEY": self.PUBLICKEY}
            request = urllib.request.Request(requestUrl, headers=publicKeyHeader)
            return(urllib.request.urlopen(request).read())
        
    def getCoinPrice(self,pair):
        if(self.EXCHANGE == "Binance"):
            requestUrl = "https://api.binance.com/api/v3/ticker/price?" \
                + 'symbol={}'.format(pair)
            priceArray = urllib.request.urlopen(requestUrl).read().decode('UTF-8')
            priceArray = json.loads(priceArray)
            return(priceArray['price'])

    def __init__(self, userExchange):
        '''
        Constructor
        '''
        self.EXCHANGE = userExchange
            
        if(self.testConnection()):
            print("Connection successful: got ping response")
        else:
            print("Connection failed: no ping response")
            

class CoinPair():
    '''
    classdocs
    '''
    
    pairName = ""
    price = 0
    baseCoin = ""
    topCoin = ""
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.pairName = name
        n = 3
        self.topCoin, self.baseCoin = [self.pairName[i:i+n] for i in range(0, len(self.pairName), n)]
        
    def setPrice(self, userPrice):
        # Not working
        self.price = userPrice
        
    def getName(self):
        return(self.pairName)
        
            
if __name__ == '__main__':
    #For unit testing
    import crypto_arbitage
    
    binance = Connection("Binance")
    
    crypto = crypto_arbitage.CryptoArbitage()
    
    binance.setKeys(crypto.getKeys())
    
    serverTimeStamp = binance.serverTimeConvert(binance.getServerTime())
        
    accountInfo = binance.getAccountInfo(serverTimeStamp)
    print('Account Info : {}'.format(accountInfo))
    
    pairName = "ETHBTC"
    pair = CoinPair(pairName)
    pair.setPrice(binance.getCoinPrice(pairName))
    print(pair.price)

    
    