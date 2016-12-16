#***Movie Score Predictor***

### ***Description***
What does it do: Our software will predict whether a movie is good, average, or bad based upon the input. This will be useful for determining whether or not it is worth seeing an upcoming movie in theaters upon release. For movie producers, this software will allow them to determine if their movie will be the next big hit! Additionally as an add on feature, our program also returns movie suggestions based off of genre. 

How does it work: The software is built using Python. We tested 28 variables to determine the most relevant ones in calculating imdb rating. Our model uses a logistic regression equation in making predictions. When people input the values for the different variables, the model uses these inputs in the equation and then returns a score for the movie. The movie recommendor outputs the top movies of each genre from our database of over 5000 movies.

### ***Authors***
The developers of this software are Wayne Kwon, Jason Lee, Alyssa Wu, and Sandy Ta.

### ***Getting Started***
In order to use this software, you will need to following Python packages:

numpy

pandas

scikit-learn

flask

To install all these packages, run this line of code in your terminal:

sudo apt-get install matplotlib, numpy, pandas, scikit-learn, flask
To run the software:

1. Clone or download the repo

2. Go to the folder

$ cd .../finalproject

3. Run the website.py file from the terminal and click "Let's Predict," which is at the top of the website

$ python website.py

### ***Usage***

The main files that you will need from the repository are movie_metadata.csv, clean_data.py, movie_recommend.py, website.py, final_model.py, and our flask templates.
First, you will want to run website.py. Be sure to replace file_n with the location of your movie_metadata.csv file if needed. After running the code, you should receive an output of 'bad','average', or 'good' as well as movie suggestions based off of the movie genre. 

###***MIT License***

Copyright (c) 2016 Wayne Kwon, Jason Lee, Alyssa Wu, and Sandy Ta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
