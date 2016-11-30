import pandas as pd
import matplotlib.pyplot as plt

mydata=pd.read_csv('rough_cleandata.csv')



mydata.drop(['Unnamed: 0'], axis = 1, inplace = True)

#correlation of selective variables - put in name of columns you wish to calculate


mydata.loc[mydata["movie_response"]=="Bad", "movie_response"] = 0
mydata.loc[mydata["movie_response"]=="Average", "movie_response"] = 1
mydata.loc[mydata["movie_response"]=="Good", "movie_response"] = 2

response = mydata['movie_response']
#print mydata.corrwith(mydata['movie_response'])

#print type(mydata)

#print mydata[["imdb_score", "budget", "duration"]].corrwith(mydata["movie_response"])

#correlation of all variables
corr_coef=mydata.corr()
print corr_coef['imdb_score']


plt.scatter(mydata['num_user_for_reviews'], mydata['imdb_score'])
#pd.scatter_matrix(mydata, diagonal = 'kde', color = 'k', alpha = 0.3)
#plt.show()
