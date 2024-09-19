import pandas as pd
import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e2559f4930ec442547d1d1b0d367ee4c&language=en-US'.format(movie_id))
    data = requests.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters

movies_dict = pickle.load(open('movie_list.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('How would you like to recommend ?', movies['title'].values)

if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta.columns(5)
    with col1:
      st.text(name[0])
      st.image(posters[0])

    with col2:
      st.text(name[1])
      st.image(posters[1])

    with col3:
      st.text(name[2])
      st.image(posters[2])

    with col4:
      st.text(name[3])
      st.image(posters[3])

    with col5:
      st.text(name[4])
      st.image(posters[4])    
