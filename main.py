from gdax_authentiClient import *
from gdax_publicClient import *

product_id = "ETH-EUR"

myInfo = infoPerso.infoPerso()

#plotProductHistoricRates(product_id) 
#plotProductOrders(product_id)
#getPosition()
#mailAlert('un text')

#getMyOrders()

order = buyAtBestPrice()
cancelOrder(order['id'])
#
# order = buyCoins()
# print(order)
# 
# order = sellCoins()
# print(order)

# count = 0
# while (count < 200):
#    val = getMyOrders()
#    time.sleep(30)
#    count = count + 1
#    