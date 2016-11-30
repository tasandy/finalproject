from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submission', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
    else:
        error = 'Error: Please fill out all fields'

    return render_template('index.html')



if __name__ == '__main__':
    app.run()
