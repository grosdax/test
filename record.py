import gdax
import pickle
from threading import *

# refresh rate
rps = 1.0

# product id
product = 'BTC-EUR'

# output file name
fileName = 'orders.dat'

publicClient = gdax.PublicClient()

def update():
        try:
            orders = publicClient.get_product_order_book(product, 2)
            value = float(publicClient.get_product_trades(product)[0]['price'])
            file = open(fileName, "ab")
            pickle.dump(orders, file)
            pickle.dump(value, file)
            file.close()
        except:
            pass
        t = Timer(1.0 / rps, update)
        t.start()

update()
	