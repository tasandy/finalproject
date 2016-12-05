from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

#must run code to clean the dataset first upon using the linear regression
mydata=pd.read_csv('rough_cleandata.csv', index_col = 0)

#creating variables
predictors = ['color', 'num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_1_facebook_likes', 'num_voted_users', 'cast_total_facebook_likes', 'facenumber_in_poster', 'num_user_for_reviews', 'language', 'content_rating', 'budget', 'actor_2_facebook_likes']
X = mydata[predictors]
y = mydata['imdb_score']

#linear regression
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)
linreg = LinearRegression()
linreg.fit(X_train, y_train)
print(linreg.intercept_)
print list(zip(predictors, linreg.coef_))

#testing the model
y_pred = linreg.predict(X_test)

#MSE
print 'The MSE is'
print(metrics.mean_squared_error(y_test, y_pred))
