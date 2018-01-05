import gdax
import json

import matplotlib.pyplot as plt
import time

def plotProductHistoricRates(product_id):
    # Set a default product
    publicClient = gdax.PublicClient()
    
    # To include other parameters, see official documentation:
    products = publicClient.get_products()
    
    data24 = publicClient.get_product_historic_rates(product_id)
    
    t= data24[0][0]
    
    print(time.ctime(t))
    
    #print( len(data24))
    x=[]
    y=[]
    
    for d in data24:
        x.append(d[0])
        y.append(d[1])
        
    plt.plot(x, y)
    
    plt.show()

def plotProductOrders(product_id):
    # Set a default product
    publicClient = gdax.PublicClient()
    
    # To include other parameters, see official documentation:
    orders = publicClient.get_product_order_book(product_id, 2)
    
    xbids=[]
    ybids=[]
     
    for d in orders['bids']:
            xbids.append(d[0])
            ybids.append(d[1])
     
    plt.plot(xbids, ybids, 'r')
  
    xasks=[]
    yasks=[]
    for d in orders['asks']:
            xasks.append(d[0])
            yasks.append(d[1])
     
    plt.plot(xasks, yasks, 'g')
     
    plt.show()

publicClient = gdax.PublicClient()
for i in range(5):
	orders = publicClient.get_product_order_book('BTC-EUR', 2)
	print orders
		
#plotProductOrders('BTC-EUR')
