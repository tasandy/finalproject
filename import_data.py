import pandas as pd
import matplotlib.pyplot as plt



mydata=pd.read_csv('movie_metadata.csv')

#sort by years

mydata.sort_values(by='title_year')

#binning response variable - imdb

bins_response = [0, 5, 7, 10]
movie_response_group = ['Bad', 'Average', 'Good']

mydata['movie_response'] = pd.cut(mydata['imdb_score'], bins_response, labels = movie_response_group)

#finding the missing values

#create a new function

def num_missing(x):
    return sum(x.isnull())

print "Missing values per column:"
print mydata.apply(num_missing, axis = 0)


#print mydata.tail(10)
