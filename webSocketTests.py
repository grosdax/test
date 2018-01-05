class myWebsocketClient(gdax.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.gdax.com/"
        self.products = ["ETH-EUR"]
        self.message_count = 0
        print("Lets count the messages!")
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

wsClient = myWebsocketClient()
wsClient.start()
print(wsClient.url, wsClient.products)
while (wsClient.message_count < 500):
    print ("\nmessage_count =", "{} \n".format(wsClient.message_count))
    time.sleep(1)
wsClient.close()


# # import PyMongo and connect to a local, running Mongo instance
# from pymongo import MongoClient
# 
# mongo_client = MongoClient('mongodb://localhost:27017/')
# 
# # specify the database and collection
# db = mongo_client.cryptocurrency_database
# BTC_collection = db.BTC_collection
# 
# # instantiate a WebsocketClient instance, with a Mongo collection as a parameter
# wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD", BTC_collection, False)
# wsClient.start()