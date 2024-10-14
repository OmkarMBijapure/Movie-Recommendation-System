#movie recommendation system (content based recommendation)
#text data(feature extraction) find similar movies
#we use cosine similarity algorithm

import pandas as pd
import numpy as np
import difflib #to get closest match of the movie given by the user if any wrong values
from sklearn.feature_extraction.text import TfidfVectorizer #converting txt to numeric
from sklearn.metrics.pairwise import cosine_similarity #to get similarity score of all the movies and recommend it


#data collection and preprocessing

movies_data = pd.read_csv(r"D:\personal project\movies recommendation system\movies.csv")

movies_data.head()

movies_data.shape

#selecting the relevant features for recommendation(also called as feature-selection)
#choosing only 5 colums out of 24
#i.e genres , keywords , tagline , cast , director
selected_features = ['genres' , 'keywords' , 'tagline' , 'cast' ,'director']
print(selected_features)

#replacing the null values with null string

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')
    
#combining all the 5 selected feature, basically all column

combined_features = movies_data['genres']+' '+movies_data ['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

#converting textual data into numerical values using tfidfvectorizer

vectorizer = TfidfVectorizer()

feature_vector = vectorizer.fit_transform(combined_features)

print(feature_vector)
    
#to find similarity score using cosine similarity

similarity = cosine_similarity(feature_vector)

print(similarity)

#getting the movie name from user

movie_name = input('Enter your favourite movie name : ')
    
#creating a list with all the movie names given in the dataset

list_of_all_titles = movies_data['title'].tolist()

print(list_of_all_titles)

#finding the close match for the movie name given by user

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

print(find_close_match)

close_match = find_close_match[0]

print(close_match)

#finding the index of the movie with title so we can find similarity score later

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

print(index_of_the_movie)

#getting the list of similar movies 
#enumerate is used to carry out a loop in a list

similarity_score = list(enumerate(similarity[index_of_the_movie]))

print(similarity_score)

len(similarity_score)

#finding only highest similarity score so that we can recommend it to user
#sorting the movies based on their similarity score
#reverse = true means highest to lowest ,lamda 

sorted_similar_movies = sorted(similarity_score , key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

#print the name of similary movies based on index

print('Movies Suggested for you: \n')

i=1

for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if(i<20):
        print(i, '.', title_from_index)
        i+=1

#go to line 53 

movie_name = input('Enter your favourite movie name : ')
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score , key = lambda x:x[1], reverse = True)
print('Movies Suggested for you: \n')
i=1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if(i<20):
        print(i, '.', title_from_index)
        i+=1



















    
    
    
    
    
    
    
    
    
    