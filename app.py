import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Load the dataset
# ----------------------------
st.set_page_config(page_title="🎬 Movie Recommendation System", layout="centered")

@st.cache_data
def load_data():
    movies_data = pd.read_csv("movies.csv")
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    combined_features = (
        movies_data['genres'] + ' ' +
        movies_data['keywords'] + ' ' +
        movies_data['tagline'] + ' ' +
        movies_data['cast'] + ' ' +
        movies_data['director']
    )

    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(feature_vectors)

    return movies_data, similarity

movies_data, similarity = load_data()

# ----------------------------
# UI Layout
# ----------------------------
st.title("🎥 Movie Recommendation System")
st.write("Type a movie you love and get similar recommendations!")

# Input movie name
movie_name = st.text_input("Enter a movie name:")

if st.button("🎬 Get Recommendations"):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        st.error("❌ No matching movie found. Try typing a more accurate name.")
    else:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.subheader(f"🎯 Top recommendations similar to **{close_match}**:")
        for i, movie in enumerate(sorted_similar_movies[1:11], start=1):
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            st.write(f"**{i}.** 🎞️ {title_from_index}")
