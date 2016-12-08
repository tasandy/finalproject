import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

def predict_movie_rating(list_of_user_input, data_for_prediction):

    #storing the resopnse variable in 'response' for easier code writing
    response = data_for_prediction['movie_response']

    #create a list of predictors to include in classification model
    predictor_list = ['title_year', 'director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'facenumber_in_poster', 'content_rating', 'budget',
    'Action','Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
    'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller','War', 'Western' ]
    movie_features = data_for_prediction[predictor_list]

    #transform X from pandas dataframe to numpy arrays
    X = movie_features.as_matrix()
    #transform y from pandas to 1D list
    y = list(data_for_prediction['movie_response'].values)

    #--------------- CARRY OUT CLASSIFICATION MODELS ---------------

    #call in the models
    logreg = LogisticRegression()

    # fit the model with our dataset
    logreg.fit(X, y)

    #make predictions on the testing set
    log_y_pred = logreg.predict(list_of_user_input)

    return log_y_pred
