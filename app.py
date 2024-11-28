
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    """
    Fetch the movie poster URL using the TMDB API.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f86f6e44c9731e9de5b2afc6afc609dc&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Placeholder if no image is found


def recommend_movies(title):

    if title not in movies['title'].values:
        return ["Movie not found. Please try a different title!!"], []

    idx = movies[movies['title'] == title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:11]  # Top 10 recommendations
    movie_indices = [i[0] for i in scores]

    recommended_movies = movies['title'].iloc[movie_indices].values.tolist()
    recommended_movies_posters = [fetch_poster(movies['movie_id'].iloc[i]) for i in movie_indices]

    return recommended_movies, recommended_movies_posters


# Load movie data and cosine similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white; /* Ensures text is visible on black background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.title('Movie Recommender System')

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 2.5rem;
        color: #FFD700; 
        font-weight: bold; 
        text-decoration: underline; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    </style>
    <h1 class="custom-title">Movie Recommender System</h1>
    """,
    unsafe_allow_html=True
)
option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    # Get recommendations and posters
    recommended_movies, recommended_posters = recommend_movies(option)

    if recommended_movies and recommended_posters:

        for i in range(0, len(recommended_movies), 5):  # Display 5 movies per row
            cols = st.columns(5)
            for col, movie, poster in zip(cols, recommended_movies[i:i+5], recommended_posters[i:i+5]):
                with col:
                    st.image(poster, use_container_width=True)  # Updated to use use_container_width
                    st.caption(movie)
    else:
        st.write(recommended_movies[0])





import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    """
    Fetch the movie poster URL using the TMDB API.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f86f6e44c9731e9de5b2afc6afc609dc&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Placeholder if no image is found


def recommend_movies(title):

    if title not in movies['title'].values:
        return ["Movie not found. Please try a different title!!"], []

    idx = movies[movies['title'] == title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:11]  # Top 10 recommendations
    movie_indices = [i[0] for i in scores]

    recommended_movies = movies['title'].iloc[movie_indices].values.tolist()
    recommended_movies_posters = [fetch_poster(movies['movie_id'].iloc[i]) for i in movie_indices]

    return recommended_movies, recommended_movies_posters


# Load movie data and cosine similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white; /* Ensures text is visible on black background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.title('Movie Recommender System')

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 2.5rem;
        color: #FFD700; 
        font-weight: bold; 
        text-decoration: underline; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    </style>
    <h1 class="custom-title">Movie Recommender System</h1>
    """,
    unsafe_allow_html=True
)
option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    # Get recommendations and posters
    recommended_movies, recommended_posters = recommend_movies(option)

    if recommended_movies and recommended_posters:

        for i in range(0, len(recommended_movies), 5):  # Display 5 movies per row
            cols = st.columns(5)
            for col, movie, poster in zip(cols, recommended_movies[i:i+5], recommended_posters[i:i+5]):
                with col:
                    st.image(poster, use_container_width=True)  # Updated to use use_container_width
                    st.caption(movie)
    else:
        st.write(recommended_movies[0])





>>>>>>> 173ce5a6f576ca8c0844a1790ca65e2a7f428b8d
=======
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    """
    Fetch the movie poster URL using the TMDB API.
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f86f6e44c9731e9de5b2afc6afc609dc&language=en-US"
    response = requests.get(url)
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Placeholder if no image is found


def recommend_movies(title):

    if title not in movies['title'].values:
        return ["Movie not found. Please try a different title!!"], []

    idx = movies[movies['title'] == title].index[0]
    scores = list(enumerate(cosine_sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:11]  # Top 10 recommendations
    movie_indices = [i[0] for i in scores]

    recommended_movies = movies['title'].iloc[movie_indices].values.tolist()
    recommended_movies_posters = [fetch_poster(movies['movie_id'].iloc[i]) for i in movie_indices]

    return recommended_movies, recommended_movies_posters


# Load movie data and cosine similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white; /* Ensures text is visible on black background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.title('Movie Recommender System')

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 2.5rem;
        color: #FFD700; 
        font-weight: bold; 
        text-decoration: underline; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    </style>
    <h1 class="custom-title">Movie Recommender System</h1>
    """,
    unsafe_allow_html=True
)
option = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    # Get recommendations and posters
    recommended_movies, recommended_posters = recommend_movies(option)

    if recommended_movies and recommended_posters:

        for i in range(0, len(recommended_movies), 5):  # Display 5 movies per row
            cols = st.columns(5)
            for col, movie, poster in zip(cols, recommended_movies[i:i+5], recommended_posters[i:i+5]):
                with col:
                    st.image(poster, use_container_width=True)  # Updated to use use_container_width
                    st.caption(movie)
    else:
        st.write(recommended_movies[0])






