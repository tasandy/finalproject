import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#building a histogram
mydata= pd.read_csv('movie_metadata.csv')

mydata=mydata[mydata['country']=='USA']
mydata=mydata.ix[:50,['first_year'], ['budget']]
mydata=mydata.set_index(['first_year'])

mydata.plot(color='Green')
plt.show()
