import gdax
import json

import smtplib
import infoPerso
import time

import matplotlib.pyplot as plt


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

    labels = None
    sizes = []
    
    for ac in acounts:
        balance = float(ac['balance'])

        if( ac['currency'] == 'EUR'):
            value = balance;
            print(ac['currency'], balance, value)
            total += value
            labels.append('EUR')
            sizes.append(value)
        else: 
            for product in products:
                if( ac['currency'] == product['currency']):
                    ticker = publicClient.get_product_ticker(product['id'])
                    value = float(balance)*float(ticker['bid'])
                    print(ac['currency'], ticker['bid'], balance, value)
                    total += value
                    labels.append(ac['currency'])
                    sizes.append(value)
                    
    print( 'my total is:', total)
    
    ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.show()
        
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
    
    print( orders)  


def buyCoins( price='100.00', #EUR
               size='0.001', #BTC
               product_id='BTC-EUR'):
    
    myInfo = infoPerso.infoPerso()

    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)

    keys = {'size': size, 'product_id':product_id, 'price': price}
    order = auth_client.buy(**keys)
    
    
    return order

def buyAtBestPrice( size='0.01',
               product_id='LTC-EUR'):
    
    myInfo = infoPerso.infoPerso()

    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)

    publicClient = gdax.PublicClient()
    ticker = publicClient.get_product_ticker(product_id)
    
    price =  float(ticker['price'])- 0.5
    keys = {'size': size, 'product_id':product_id, 'price': price}
    order = auth_client.buy(**keys)
    print(order)
        
    count = 0
    while (count < 60):
        time.sleep(1)
        auth_client.cancel_order(order['id'])
        ticker = publicClient.get_product_ticker(product_id)
        price = float(ticker['price']) - 0.5;
        keys = {'size': size, 'product_id':product_id, 'price': price}
        order = auth_client.buy(**keys)
        print(order)
        count = count + 1
        
    
        
    
    return order

    
    
def sellCoins( price='20000.00', #EUR
               size='0.001', #BTC
               product_id='BTC-EUR'):
    
    myInfo = infoPerso.infoPerso()

    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)

    keys = {'size': size, 'product_id':product_id, 'price': price}
    order = auth_client.sell(**keys)
    
    return order
    
def cancelOrder( order_id ):
    myInfo = infoPerso.infoPerso()

    auth_client = gdax.AuthenticatedClient( myInfo.gdax_key, myInfo.gdax_b64secret, myInfo.gdax_passphrase)
    
    if order_id :
        orders = auth_client.cancel_order(order_id) 
        print( orders)
    else:
        print( 'no order to cancel')  

