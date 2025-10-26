Movie Recommendation System
This project is a Movie Recommendation System developed using Python, employing both data analysis and machine learning techniques along with a web-based interface.

Overview
The system provides personalized movie recommendations based on user input, leveraging movie metadata and similarity calculations between movies. It is designed to recommend movies similar in themes, genres, and keywords to the selected movie.

Components
Movie_Recommend_project.ipynb

This Jupyter Notebook includes detailed data processing and analysis steps.

Loads and merges movie datasets including movie details and credits.

Cleans and preprocesses data columns such as genres, keywords, cast, and crew.

Uses TF-IDF vectorization on movie tags for feature representation.

Computes cosine similarity between movie vectors to identify similarity scores.

Implements a function recommend_movie that takes a movie title as input and returns the top 5 similar movies based on computed similarity.

Contains exploratory data analysis and visualization to understand the dataset characteristics.

Also shows merging and cleaning of datasets to form a unified movie data source.

main.py

This Python script uses Streamlit to create a simple and interactive web app interface for the movie recommendation system.

Loads preprocessed movie dictionaries and similarity matrices from pickle files.

Provides a dropdown menu to select a movie title.

On submitting a movie title, it displays the top recommended movies.

Fetches movie posters via an external API for visual display alongside recommendations.

It enables quick deployment of the recommendation system as a user-friendly web app.

Features
Data-driven movie similarity computation using content-based filtering.

Uses TF-IDF vectorization of movie tags for feature extraction.

Cosine similarity for recommending movies with similar content.

Interactive web interface with Streamlit for ease of use.

Poster fetching from an API adds an engaging visual component.

Works with publicly available TMDB movie datasets.

Usage
Run the Jupyter Notebook (Movie_Recommend_project.ipynb) to preprocess data, compute similarity matrices, and experiment with recommendations.

Use the main.py script to launch the Streamlit app for interactive movie recommendations.

Select a movie from the dropdown and get a list of similar movie recommendations.
