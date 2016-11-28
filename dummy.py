import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans



mydata=pd.read_csv('movie_metadata.csv')

#sort by years

mydata.sort_values(by='title_year')

#binning response variable - imdb

bins_response = [0, 5, 7, 10]
movie_response_group = ['Bad', 'Average', 'Good']

mydata['movie_response'] = pd.cut(mydata['imdb_score'], bins_response, labels = movie_response_group)

#keeping only USA
mydata = mydata[mydata['country']== 'USA']
#get rid of NaN in year
mydata = mydata.dropna(subset = ['title_year'])

#creating dummy variables for genres
dummy_genre=mydata['genres'].str.get_dummies(sep='|')

#drop genre from mydata

mydata.drop(['genres'], axis = 1, inplace = True)
merged_data = pd.concat([mydata, dummy_genre], axis = 1)

mydata = merged_data

#drop unnecessary columns
mydata.drop(['aspect_ratio'], axis = 1, inplace = True)
mydata.drop(['plot_keywords'], axis = 1, inplace = True)
mydata.drop(['director_name'], axis = 1, inplace = True)
mydata.drop(['actor_1_name'], axis = 1, inplace = True)
mydata.drop(['actor_2_name'], axis = 1, inplace = True)
mydata.drop(['actor_3_name'], axis = 1, inplace = True)
mydata.drop(['gross'], axis = 1, inplace = True)
mydata.drop(['country'], axis = 1, inplace = True)
mydata.drop(['movie_title'], axis = 1, inplace = True)

#managing categorical variables

#COLOR - 1 if color, 0 if black and white
mydata.loc[mydata['color']==" Black and White", "color"] = 0
mydata.loc[mydata['color']=="Color", "color"] = 1
mydata['color']=mydata['color'].fillna(1)
#print mydata['color'].unique()

#Language - 0 if English, 1 if non-english
mydata["language"] = mydata["language"].fillna("English")
mydata.loc[mydata["language"] != "English", "language"] = 1
mydata.loc[mydata["language"] == "English", "language"] = 0
#print mydata["language"].unique()

#content rating...putting into 6 different categories...
#Unrated,G, PG, PG-13, R, NC-17 -> 0,1,2,3,4,5
#print mydata['content_rating'].unique()
mydata.loc[mydata["content_rating"]=="X", "content_rating"] = "NC-17"
mydata.loc[mydata["content_rating"]=="GP", "content_rating"] = "PG"
mydata.loc[mydata["content_rating"]=="TV-G", "content_rating"] = "G"
mydata.loc[mydata["content_rating"]=="TV-PG", "content_rating"] = "PG"
mydata.loc[mydata["content_rating"]=="M", "content_rating"] = "PG"
mydata.loc[mydata["content_rating"]=="TV-14", "content_rating"] = "PG-13"
mydata.loc[mydata["content_rating"]=="Not Rated", "content_rating"] = "Unrated"
mydata.loc[mydata["content_rating"]=="Passed", "content_rating"] = "Unrated"
mydata.loc[mydata["content_rating"]=="Approved", "content_rating"] = "Unrated"
mydata["content_rating"] = mydata["content_rating"].fillna("Unrated")

mydata.loc[mydata["content_rating"] == "Unrated", "content_rating"] = 0
mydata.loc[mydata["content_rating"] == "G", "content_rating"] = 1
mydata.loc[mydata["content_rating"] == "PG", "content_rating"] = 2
mydata.loc[mydata["content_rating"] == "PG-13", "content_rating"] = 3
mydata.loc[mydata["content_rating"] == "R", "content_rating"] = 4
mydata.loc[mydata["content_rating"] == "NC-17", "content_rating"] = 5
#print mydata['content_rating'].unique()

def num_missing(x):
    return sum(x.isnull())

#print "Missing values per column:"
#print mydata.apply(num_missing, axis = 0)


#droppping Actors

mydata = mydata.dropna(subset=["actor_1_facebook_likes","actor_2_facebook_likes","actor_3_facebook_likes"])

#dropping columns with missing values for NOWWWWW

mydata = mydata .dropna(subset = ["duration", "num_critic_for_reviews", "facenumber_in_poster", "num_user_for_reviews", "budget"])

print "Missing values per column:"
print mydata.apply(num_missing, axis = 0)

#mydata.to_csv("rough_cleandata.csv")
