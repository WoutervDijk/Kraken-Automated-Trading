import krakenex
from time import sleep
import Keys
import pprint
import json

sellTrigger = 235
buyPrice = 0
currentOrder = 1
DidTransactionHappen = False
SellOrderAlreadyCreated = False
k = krakenex.API(Keys.APIKey,Keys.privateKey)
currentPrice = 0

def TrailingSellOrder():
    k.query_private('AddOrder', {'pair': 'XETHZEUR',
                                 'type': 'sell',
                                 'ordertype': 'trailing-stop',
                                 'price': '#5%',
                                 'volume': '1.5',
                                 'userref': str(currentOrder)})
    print("sell order created")
    sleep(4)


while not DidTransactionHappen:
    try:
        response = k.query_public('Depth', {'pair': 'XETHZEUR', 'count': '1'})
        x = json.dumps(response['result'])
        currentPrice = response['result']['XETHZEUR']['asks'][0][0]
        print(currentPrice)
        #z = k.query_private('OpenOrders',{'userref': str(currentOrder)})
        #pprint.pprint(z['result'])
        #sleep(1)
        if(float(currentPrice) > sellTrigger and SellOrderAlreadyCreated == False):
            print('If statement is triggered')
            TrailingSellOrder()
            SellOrderAlreadyCreated = True
            DidTransactionHappen = True
    except Exception as e: print(e)

    sleep(30)




