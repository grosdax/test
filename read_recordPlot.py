import pickle
import numpy as np
import matplotlib.pyplot as plt

# output file name
fileName = 'orders.dat'


f = open(fileName, "rb")

    
try:
    while(True):
        orders = pickle.load(f)
        value = pickle.load(f)

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
                                
        plt.plot( x, y,  color='r')
                 
        ymax = np.max(y)
        ytext=ymax*0.8
                    
                 
        point0= x[50]
        plt.axvline(point0, color='black', lw=2, ymax=0.5)
                  
        price = 'price= {0}'.format(orders['asks'][0][0])
        plt.annotate(price, xy=(point0, ytext) )

        plt.show()
        

except:
    f.close()
