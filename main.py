import streamlit as st
import pickle
import pandas as pd
import requests
import gdown

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)




url = "https://drive.google.com/uc?id=17YIQxYY220bMjYdabs0-HUqTaJ4G-izw"
output = "similarity.pkl"
gdown.download(url, output, quiet=False)

similarity = pickle.load(open('similarity.pkl', 'rb'))



# if not os.path.exists("similarity.pkl"):
#     print("similarity.pkl missing! Downloading now...")
#     download_file_from_google_drive("17YIQxYY220bMjYdabs0-HUqTaJ4G-izw", "similarity.pkl")



def recommend(movie):
    if movie not in movies["title"].values:
        return f"{movie} not found in dataset."

        # Find the index of the given movie
    movie_index = movies[movies["title"] == movie].index[0]

    # Get pairwise similarity scores for that movie
    distances = similarity[movie_index]

    # Sort movies by similarity scores (descending)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Return top 5 similar movies
    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies






st.title('Movie Recommendation System')


selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    recommendation = recommend(selected_movie_name)

    for i in recommendation:
        st.write(i)
