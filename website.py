from flask import Flask, render_template, redirect, url_for, request
from clean_data import get_clean_data
from final_model import predict_movie_rating
import pandas

app = Flask(__name__)

#importing rawdata and cleaning it so that it can be used in the model
file_n = 'movie_metadata.csv'
moviedata=get_clean_data(file_n)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/rating/<movie>')
def rating(movie):
    return '%s' % movie

@app.route('/submission', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        user_input = []
        list_of_predictors = ['title_year', 'director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'facenumber_in_poster', 'content_rating', 'budget',
        'Action','Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
        'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller','War', 'Western' ]
        for predictor in list_of_predictors:
            value = request.form[predictor]
            value_float = int(value)
            user_input.append(value_float)

        print user_input
        movie_rating_index=predict_movie_rating(user_input, moviedata)
        dic = {0:"Not Recommended", 1:"Hmm..I'd consider it", 2:"Go Watch It!"}
        movie_rating = [dic[n] if n in dic.keys() else n for n in movie_rating_index]
        result = movie_rating[0]
        return redirect(url_for('rating', movie = result))
    else:
        error = 'Error: Please fill out all fields'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
