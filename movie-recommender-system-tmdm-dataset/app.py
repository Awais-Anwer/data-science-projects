import streamlit as st
import pickle as pkl
import pandas as pd
import requests

movie_dict = pkl.load(open('movie_dict.pkl', 'rb'))
similarity = pkl.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict) 

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4f66ea4df974cbce59d7e8a0cedc2010'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] 
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # storing title
        recommended_movies.append(movies.iloc[i[0]].title)
        # storing posters address fetched from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters
        


st.title('Movie Recommender System')
selected_movie = st.selectbox(
    'Choose a movie',
    movies['title'].values)

if st.button("Recommend", type="primary"):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
