import pandas as pd

def get_clean_data(file_name):

    moviedata=pd.read_csv('file_name')

    #sort by years and drop observations before year 2000

    moviedata.sort_values(by='title_year')
    moviedata = moviedata.drop(moviedata[moviedata.title_year < 2000].index)

    #binning response variable into categorical variable - imdb movie score

    bins_response = [0, 5, 7, 10]
    movie_response_group = ['Bad', 'Average', 'Good']

    moviedata['movie_response'] = pd.cut(moviedata['imdb_score'], bins_response, labels = movie_response_group)

    #keeping only USA
    moviedata = moviedata[moviedata['country']== 'USA']

    #creating dummy variables for genres
    dummy_genre=moviedata['genres'].str.get_dummies(sep='|')

    #drop genre from moviedata

    moviedata.drop(['genres'], axis = 1, inplace = True)
    merged_data = pd.concat([moviedata, dummy_genre], axis = 1)

    moviedata = merged_data

    #drop unnecessary columns
    moviedata.drop(['aspect_ratio'], axis = 1, inplace = True)
    moviedata.drop(['plot_keywords'], axis = 1, inplace = True)
    moviedata.drop(['director_name'], axis = 1, inplace = True)
    moviedata.drop(['actor_1_name'], axis = 1, inplace = True)
    moviedata.drop(['actor_2_name'], axis = 1, inplace = True)
    moviedata.drop(['actor_3_name'], axis = 1, inplace = True)
    moviedata.drop(['gross'], axis = 1, inplace = True)
    moviedata.drop(['country'], axis = 1, inplace = True)
    moviedata.drop(['movie_title'], axis = 1, inplace = True)

    #managing categorical variables

    # COLOR - 1 if color, 0 if black and white
    moviedata.loc[moviedata['color']==" Black and White", "color"] = 0
    moviedata.loc[moviedata['color']=="Color", "color"] = 1
    moviedata['color']=moviedata['color'].fillna(1)

    #Language - 0 if English, 1 if non-english
    moviedata["language"] = moviedata["language"].fillna("English")
    moviedata.loc[moviedata["language"] != "English", "language"] = 1
    moviedata.loc[moviedata["language"] == "English", "language"] = 0


    #content rating...putting into 6 different categories...
    #Unrated,G, PG, PG-13, R, NC-17 -> 0,1,2,3,4,5
    #print moviedata['content_rating'].unique()
    moviedata.loc[moviedata["content_rating"]=="X", "content_rating"] = "NC-17"
    moviedata.loc[moviedata["content_rating"]=="GP", "content_rating"] = "PG"
    moviedata.loc[moviedata["content_rating"]=="TV-G", "content_rating"] = "G"
    moviedata.loc[moviedata["content_rating"]=="TV-PG", "content_rating"] = "PG"
    moviedata.loc[moviedata["content_rating"]=="M", "content_rating"] = "PG"
    moviedata.loc[moviedata["content_rating"]=="TV-14", "content_rating"] = "PG-13"
    moviedata.loc[moviedata["content_rating"]=="Not Rated", "content_rating"] = "Unrated"
    moviedata.loc[moviedata["content_rating"]=="Passed", "content_rating"] = "Unrated"
    moviedata.loc[moviedata["content_rating"]=="Approved", "content_rating"] = "Unrated"
    moviedata["content_rating"] = moviedata["content_rating"].fillna("Unrated")

    moviedata.loc[moviedata["content_rating"] == "Unrated", "content_rating"] = 0
    moviedata.loc[moviedata["content_rating"] == "G", "content_rating"] = 1
    moviedata.loc[moviedata["content_rating"] == "PG", "content_rating"] = 2
    moviedata.loc[moviedata["content_rating"] == "PG-13", "content_rating"] = 3
    moviedata.loc[moviedata["content_rating"] == "R", "content_rating"] = 4
    moviedata.loc[moviedata["content_rating"] == "NC-17", "content_rating"] = 5

    #get rid of missing values in our dataset
    moviedata = moviedata.dropna(subset = ['title_year'])
    moviedata = moviedata.dropna(subset=["actor_1_facebook_likes","actor_2_facebook_likes","actor_3_facebook_likes"])
    moviedata = moviedata.dropna(subset = ["duration", "num_critic_for_reviews", "facenumber_in_poster", "num_user_for_reviews", "budget"])

    return moviedata
