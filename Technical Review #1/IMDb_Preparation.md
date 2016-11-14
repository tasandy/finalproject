#Predict the IMDb scores

##Team Ignus: Wayne Kwon, Jason Lee, Alyssa Wu, and Sandy |

###Background and context
**Dataset**: [IMDb Scores](https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset)

We have found an existing data set containing over 5000 data points for movies linked above. The data set contains 28 variables ranging from information such as the director name, main actors and the number of likes that each actor has on Facebook, the movie budget, genre, etc. The objective of our project is to create a program that will take user inputs for a movie and return an accurate imdb score for it. In order to do this, we will be running different statistical prediction models through Python packages such as scikit-learn and pandas.


Currently with the data set, there are a number of missing values. Some columns have hundreds of missing data points. The most missing data points comes from Gross Earnings, which has about 500 missing data points. Other columns have only a few missing data points with the lowest being six missing points. About 16 columns out of the 28 variables have missing values to them.

###Key questions
1. Cleaning Raw Data: Methods of cleaning/filtering the data set? What should we do with the missing values?
  1. Currently 16 out of 28 columns have missing values. Some have up to 500 missing values whilte the ohters have a few
  2. Current Considerations:
    1. Maunally looking up and filling in missing values ourselves
    2. Replacing the missing values with the average for that column
      - Averaging values means skewing data, especially if the range is large
    3. Deleting those data points entirely
      - Deleting missing values means a lot less data
    4. For the variables with wider range, we can standardize or perform a transformation to take different scales into account

2. How should we deal with the data points in the ‘Genre’ variable for movies that have multiple genres? 
  2. Complications:
    1. There are multiple genres associated with one movie
    2. Example: if we filter by 'Actions,' there are only 15 movies
  3. Current Considerations: 
    1. Randomly pick one of the genres listed
    2. Pick the first one in the row listed
    3. Create dummy variables

3. What other statistical models do you suggest using?
  1. Current Considerations:
    1. Multiple Linear Regression (Response: Continuous)
    2. Logistic Regression (Response: Categorical)
    3. Classification Tree (Response: Categorical)
  2. For Logistic Regression and Classification Tree, we will bin the IMDb scores into three categories: Bad, Average, Good

4. Given our project goal to build a model that predicts the IMDb score, what other interests do you have in our dataset?
  1. For example, people may want to figure out if budget, specifically, is highly correlated with the IMDb score
  2. Or, we can compare the significant predictors from different set of years
    1. What variables are more important in pre-2000 vs. post-2000?

5. What other extensions would you recommend that we can build that would interest you?
  1. Current Considerations:
    1. Build a statistical model from scratch, without using scikit-learn
    2. Extend code to be usable with other datasets
    3. Compare the significant predictors from different set of years
      - What's more important in pre-2000 vs. post-2000?

###Agenda
1. Background and context (2 minutes)
2. key questions #1~3 (18 minutes)
  1. Equal time allocated for each key question (6 minutes each)
3. Additional questions #4~5 (if time permits)

**Strategy**: To communicate with our audience, we will have a discussion session after each key question #1~3. If time permits, we will continue on our additional questions #4~5. 

**Notetaker**: Alyssa Wu



