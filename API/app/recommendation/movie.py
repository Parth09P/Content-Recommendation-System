import pickle
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


movies = pd.read_csv('E:/PROJECTS/Movie_Recommender/dataset/movies.csv') 
ratings = pd.read_csv('E:/PROJECTS/Movie_Recommender/dataset/ratings.csv') 
links = pd.read_csv('E:/PROJECTS/Movie_Recommender/dataset/links.csv')
tags = pd.read_csv('E:/PROJECTS/Movie_Recommender/dataset/tags.csv')

data = pd.merge(movies, ratings, on='movieId', how='inner')
df = data
df.drop(['genres', 'timestamp'], axis = 1, inplace = True)
data_pivot = pd.pivot(index = "movieId", columns = "userId", data = ratings, values = "rating")

Movie_voted = pd.DataFrame(ratings.groupby("movieId")["rating"].agg("count"))
Movie_voted.reset_index(level = 0, inplace = True)

User_Voted = pd.DataFrame(ratings.groupby("userId")["rating"].agg("count"))
User_Voted.reset_index(level = 0, inplace = True)

data_pivot.fillna(0, inplace = True)  

final_data = data_pivot.loc[Movie_voted[Movie_voted["rating"] > 10]["movieId"],:]
final_data = final_data.loc[:, User_Voted[User_Voted["rating"] > 60]["userId"]]


csr_data = csr_matrix(final_data.values)
final_data.reset_index(inplace=True)


knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(csr_data)

def movie_recommendation(movie_name):
    
    n_movies_to_recommend= 10
    movie_list = movies[movies['title'].str.contains(movie_name)] # Fint movie name
    
    if len(movie_list):
        
        try:
          movie_idx= movie_list.iloc[0]['movieId']
          movie_idx = final_data[final_data['movieId'] == movie_idx].index[0]
        
        except:
          return 'No relevant movies found!'
        
        distances , indices = knn.kneighbors(csr_data[movie_idx],n_neighbors=n_movies_to_recommend+1)    
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
        recommend_frame = []
        
        for val in rec_movie_indices:
            movie_idx = final_data.iloc[val[0]]['movieId']
            idx = movies[movies['movieId'] == movie_idx].index
            recommend_frame.append({'Title':movies.iloc[idx]['title'].values[0],'Distance':val[1]})
        df = pd.DataFrame(recommend_frame,index=range(1,n_movies_to_recommend+1))
        return df
    
    else:
        return "No relevant movies found!"