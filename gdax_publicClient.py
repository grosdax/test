import gdax
import json

import numpy as np
import matplotlib.pyplot as plt
import time

import smtplib
import infoPerso

# Import the email modules we'll need
from email.mime.text import MIMEText


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
    
    x=[]
    y=[]

    som=0    
    print "bids"    
    for d in orders['bids']:
            x.insert(0,float(d[0]))
            som+=float(d[1])
            y.insert(0,som)
    
    som=0
    print "asks"
    for d in orders['asks']:
            x.append(float(d[0]))
            som+=float(d[1])
            y.append(som)
 
       
#     x=scale_linear(x)
#     y=scale_linear(y)

    plt.plot( x, y,  color='r')
 
    ymax = np.max(y)
    ytext=ymax*0.8
    
 
    point0= x[50]
    plt.axvline(point0, color='black', lw=2, ymax=0.5)
  
    price = 'price= {0}'.format(orders['asks'][0][0])
    plt.annotate(price, xy=(point0, ytext) )
    
    plt.show()

def scale_linear(rawpoints, high=100.0, low=0.0):
    mins = np.min(rawpoints)
    maxs = np.max(rawpoints)
    rng = maxs - mins
    return high - (((high - low) * (maxs - rawpoints)) / rng)