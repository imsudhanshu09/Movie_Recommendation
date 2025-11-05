# import streamlit as st
# import pandas as pd
# import difflib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # ----------------------------
# # Load the dataset
# # ----------------------------
# st.set_page_config(page_title="🎬 Movie Recommendation System", layout="centered")

# @st.cache_data
# def load_data():
#     movies_data = pd.read_csv("movies.csv")
#     selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

#     for feature in selected_features:
#         movies_data[feature] = movies_data[feature].fillna('')

#     combined_features = (
#         movies_data['genres'] + ' ' +
#         movies_data['keywords'] + ' ' +
#         movies_data['tagline'] + ' ' +
#         movies_data['cast'] + ' ' +
#         movies_data['director']
#     )

#     vectorizer = TfidfVectorizer()
#     feature_vectors = vectorizer.fit_transform(combined_features)
#     similarity = cosine_similarity(feature_vectors)

#     return movies_data, similarity

# movies_data, similarity = load_data()

# # ----------------------------
# # UI Layout
# # ----------------------------
# st.title("🎥 Movie Recommendation System")
# st.write("Type a movie you love and get similar recommendations!")

# # Input movie name
# movie_name = st.text_input("Enter a movie name:")

# if st.button("🎬 Get Recommendations"):
#     list_of_all_titles = movies_data['title'].tolist()
#     find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

#     if len(find_close_match) == 0:
#         st.error("❌ No matching movie found. Try typing a more accurate name.")
#     else:
#         close_match = find_close_match[0]
#         index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
#         similarity_score = list(enumerate(similarity[index_of_the_movie]))
#         sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

#         st.subheader(f"🎯 Top recommendations similar to **{close_match}**:")
#         for i, movie in enumerate(sorted_similar_movies[1:11], start=1):
#             index = movie[0]
#             title_from_index = movies_data[movies_data.index == index]['title'].values[0]
#             st.write(f"**{i}.** 🎞️ {title_from_index}")


import streamlit as st
import pandas as pd
import difflib
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------------------
# Streamlit Page Configuration
# ----------------------------------------------------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="wide")

# ----------------------------------------------------
# Custom Background & Styling
# ----------------------------------------------------
st.markdown("""
<style>
/* Background: cinematic blurred gradient */
.stApp {
    background-image: url("https://static.vecteezy.com/system/resources/previews/001/254/680/large_2x/cinema-background-concept-vector.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Gradient overlay for better readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0;
    right: 0; bottom: 0;
    background: linear-gradient(180deg, rgba(0,0,0,0.85) 10%, rgba(0,0,0,0.6) 90%);
    z-index: 0;
}

/* Movie title glow */
h1, h2, h3, h4 {
    color: #ff4b4b;
    text-shadow: 0px 0px 10px #ff4b4b;
    font-weight: 700;
    letter-spacing: 1px;
    z-index: 2;
}

/* Input box styling */
input {
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Buttons with neon hover */
button[kind="primary"] {
    background: linear-gradient(45deg, #ff4b4b, #d73eff);
    border-radius: 10px;
    color: white;
    border: none;
    font-weight: 600;
    box-shadow: 0 0 10px rgba(255,75,75,0.5);
    transition: 0.3s;
}
button[kind="primary"]:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(255,75,75,0.9);
}

/* Movie cards */
.movie-card {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 15px;
    margin: 10px;
    text-align: center;
    transition: 0.3s ease-in-out;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
}
.movie-card:hover {
    background: rgba(255,255,255,0.18);
    transform: translateY(-6px) scale(1.03);
}

/* Poster styling */
.movie-poster {
    border-radius: 12px;
    box-shadow: 0px 0px 15px #00000088;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Load Movie Data (with caching)
# ----------------------------------------------------
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

# ----------------------------------------------------
# TMDB Poster API
# ----------------------------------------------------
TMDB_API_KEY = st.secrets["TMDB_API_KEY"] # ← Replace with your TMDB API key

@st.cache_data
def get_poster(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
        response = requests.get(url).json()
        results = response.get("results")
        if results and len(results) > 0:
            poster_path = results[0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        pass
    return "https://via.placeholder.com/300x450?text=No+Image"

# ----------------------------------------------------
# Main UI
# ----------------------------------------------------
st.markdown("<h1 align='center'>🍿 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p align='center'>Find movies similar to your favorite one — powered by AI and cinema magic!</p>", unsafe_allow_html=True)

movie_name = st.text_input("🎞️ Enter a movie name to get recommendations:")

if st.button("✨ Show Recommendations"):
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        st.error("❌ No matching movie found. Try a different name.")
    else:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        st.markdown(f"<h3>🎯 Top recommendations similar to <b>{close_match}</b>:</h3>", unsafe_allow_html=True)

        cols = st.columns(5)
        i = 0
        for movie in sorted_similar_movies[1:11]:
            index = movie[0]
            title_from_index = movies_data[movies_data.index == index]['title'].values[0]
            poster_url = get_poster(title_from_index)

            with cols[i % 5]:
                st.markdown(f"""
                <div class="movie-card">
                    <img src="{poster_url}" width="150" class="movie-poster">
                    <p><b>{title_from_index}</b></p>
                </div>
                """, unsafe_allow_html=True)
            i += 1
