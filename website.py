from flask import Flask, render_template, request
from clean_data import get_clean_data
from final_model import predict_movie_rating

app = Flask(__name__)

file_n = 'movie_metadata.csv'
get_clean_data(file_n)


@app.route('/')
def hello_world():
    return render_template('index.html')

user_iputs = [2010,111,111,112,435,2,4,500000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
@app.route('/submission', methods=['POST'])
def inputs():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        print name
    else:
        error = 'Error: Please fill out all fields'

    user_inputs.append(name)
    apply_model()

    return render_template('index.html')

def apply_model():
    predict_movie_rating(user_inputs)
    user_inputs = []

if __name__ == '__main__':
    app.run()
