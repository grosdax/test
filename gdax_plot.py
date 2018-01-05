import gdax
import json

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
    
    xbids=[]
    ybids=[]
    
    print(orders['bids'])
     
    for d in orders['bids']:
            xbids.append(d[0])
            ybids.append(d[1])
     
      
    plt.plot(xbids, ybids, 'g')
   
    xasks=[]
    yasks=[]
    for d in orders['asks']:
            xasks.append(d[0])
            yasks.append(d[1])
      
    plt.plot(xasks, yasks, 'r')
      
    plt.show()
      

def getPosition():
    # get the last position for each product
    publicClient = gdax.PublicClient()
    #products = publicClient.get_products()
    
    products = [{'currency':'EUR', 'id': 'EUR'}, {'currency':'LTC', 'id': 'LTC-EUR'}, {'currency':'ETH', 'id':'ETH-EUR'}, {'currency':'BTC', 'id':'BTC-EUR'}] 

    myInfo = infoPerso.infoPerso()
    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)
    
    total = 0
    acounts = auth_client.get_accounts()
    
    with open('C:/Temp/data.txt', 'a') as outfile:  
            json.dump(acounts, outfile)

    for ac in acounts:
        balance = float(ac['balance'])

        if( ac['currency'] == 'EUR'):
            value = balance;
            print(ac['currency'], balance, value)
            total += value
        else: 
            for product in products:
                if( ac['currency'] == product['currency']):
                    ticker = publicClient.get_product_ticker(product['id'])
                    value = float(balance)*float(ticker['bid'])
                    print(ac['currency'], ticker['bid'], balance, value)
                    total += value
    print( 'my total is:', total)
    return total
        
def mailAlert( msg ):

    myInfo = infoPerso.infoPerso()

    server = smtplib.SMTP(myInfo.smpt_server, 587)
    server.starttls()

    server.login(myInfo.smpt_login, myInfo.smpt_pass)
    server.sendmail(myInfo.smpt_from, myInfo.smpt_to, msg)
    server.quit()

def getMyOrders():
    myInfo = infoPerso.infoPerso()

    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)
    
    orders = auth_client.get_orders()
    
    if( len(orders)==0):
        mailAlert()
    
    print( len(orders))  
