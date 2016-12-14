import pandas

def recommend_movie(genre_from_user, data_used_for_recommendation):
    #filtering user_input for movie recommendation
    for genres in genre_from_user:
        data_used_for_recommendation = data_used_for_recommendation[data_used_for_recommendation[genres]== 1]
    data_used_for_recommendation.sort_values(by='imdb_score')
    #keep only movies of high scores
    data_used_for_recommendation = data_used_for_recommendation.drop(data_used_for_recommendation[data_used_for_recommendation.imdb_score < 7].index)

    movie_for_recommendation = data_used_for_recommendation['movie_title'].map(lambda x: str(x)[:-2])
    movie_for_recommendation = movie_for_recommendation.tolist()


    return movie_for_recommendation[:3]
