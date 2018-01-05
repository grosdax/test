import pickle

# output file name
fileName = 'orders.dat'

f = open(fileName, "rb")
try:
    while(True):
        orders = pickle.load(f)
        value = pickle.load(f)
        print "orders : " + str(orders)
        print "value : " + str(value)
except:
    f.close()
