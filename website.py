from flask import Flask, render_template, redirect, url_for, request
from clean_data import get_clean_data
from final_model import predict_movie_rating
from movie_recommend import recommend_movie
import pandas

app = Flask(__name__)

#importing rawdata and cleaning it so that it can be used in the model
file_n = 'movie_metadata.csv'
moviedata=get_clean_data(file_n)

#list of predictors used for calculating/predicting movie response
list_of_predictors = ['title_year', 'director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'facenumber_in_poster', 'content_rating', 'budget',
'Action','Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller','War', 'Western' ]

#predictors and dataset for movie recommendation
predictors_movie_recommend = ['Action','Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller','War', 'Western', 'imdb_score', 'movie_title']
moviedata_recommend = moviedata[predictors_movie_recommend]

#genre list
genrelist = ['Action','Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller','War', 'Western']

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/rating/<movie>')
def rating(movie):
    return render_template('score_page.html', movie = movie)


@app.route('/submission', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        user_input = []
        user_input_genre = []
        for predictor in list_of_predictors:
            value = request.form[predictor]
            value_float = int(value)
            user_input.append(value_float)
        for predictor in genrelist:
            value = request.form[predictor]
            value_float = int(value)
            user_input_genre.append(value_float)

        #print user_input
        movie_rating_index=predict_movie_rating(user_input, moviedata)
        dic = {0:"Not Recommended", 1:"Hmm..I'd consider it", 2:"Go Watch It!"}
        movie_rating = [dic[n] if n in dic.keys() else n for n in movie_rating_index]
        #result = movie_rating[0]
        #movie recommendation
        genre_selected_by_user = []
        for i in range(23):
            if user_input_genre[i]==1:
                genre_selected_by_user.append(genrelist[i])

        movie_recommendation = recommend_movie(genre_selected_by_user, moviedata_recommend)
        result = movie_rating[0] +  ' | ' + 'Based off your genre preferences, we recommend the following movies: ' + movie_recommendation[0] + ", " + movie_recommendation[1] + ", " + movie_recommendation[2]
        return redirect(url_for('rating', movie = result))
    else:
        error = 'Error: Please fill out all fields'

if __name__ == '__main__':
    app.run()
