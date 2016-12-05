from flask import Flask, render_template, request
from clean_data import get_clean_data

app = Flask(__name__)


file_n = 'movie_metadata.csv'
get_clean_data(file_n)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submission', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        print name
    else:
        error = 'Error: Please fill out all fields'

    return render_template('index.html')

#def apply_model():

if __name__ == '__main__':
    app.run()
