🚀 Movie Recommendation System

🎞️ Find your next favorite movie — crafted with the magic of cinema!

This project is an intelligent Movie Recommendation System that suggests movies similar to the ones you love.
Built with machine learning and a cinematic Streamlit UI, it blends data science and design to deliver a personalized movie experience — right from your browser.

✨ Key Features

🎯 Smart Recommendations
Get personalized movie suggestions based on your chosen film using content-based filtering with TF-IDF and cosine similarity.

🎬 Interactive Streamlit Interface
A visually stunning, fully responsive web app with a cinematic background, neon glow titles, and movie poster previews.

📸 TMDB Poster Integration
Real movie posters fetched dynamically via TMDB API, giving your recommendations a real-world movie feel.

🔍 Search Functionality
Search for any movie title and instantly get similar films, complete with titles and posters.

⚡ Fast Caching & Optimization
Uses @st.cache_data and @st.cache_resource to reduce load time and improve performance.

📱 Fully Responsive Design
Optimized for both desktop and mobile — the background scales beautifully across all devices.

🧠 How It Works

This system uses Content-Based Filtering, where each movie is represented as a combination of:

🎭 Genres

✍️ Keywords

💬 Taglines

👨‍🎤 Cast

🎬 Director

The TF-IDF Vectorizer converts these text features into numerical vectors.
Then, Cosine Similarity measures how close movies are to each other — allowing the system to find and recommend similar ones.

🧰 Tech Stack

Language: Python 🐍
Framework: Streamlit 💻
Data: Movies Dataset (CSV file)
API: TMDB (for fetching posters)

Libraries Used:

pandas — data handling and preprocessing

numpy — numerical computations

scikit-learn — TF-IDF Vectorizer & Cosine Similarity

requests — TMDB API integration

streamlit — interactive and cinematic frontend

🖼️ UI Highlights

🎥 Dark Cinematic Theme
Immersive design with a blurred movie-theater background and gradient overlays.

✨ Neon Glow Headings
Dynamic glowing titles styled with CSS animations.

🍿 Poster Cards
Each recommendation appears as a movie card with rounded corners, hover effects, and shadowed posters.

📱 Mobile Responsive
Fully optimized for mobile screens — background fills 100% viewport with no cut-off.

⚙️ Installation
# Clone this repository
git clone https://github.com/imsudhanshu09/Movie_Recommendation.git

# Navigate to project directory
cd Movie_Recommendation

# Install dependencies
pip install -r requirements.txt

▶️ Usage
🧩 Run the system:
streamlit run app.py


Then open:
👉 http://localhost:8501

💡 How to Use:

Enter your favorite movie name.

Click “Show Recommendations”.

Instantly view the top 10 similar movies with posters and titles!

🔐 Secrets Management (for TMDB API Key)

To protect your API key:

Create .streamlit/secrets.toml:

TMDB_API_KEY = "your_tmdb_key_here"


Add .streamlit/secrets.toml to .gitignore.

On Streamlit Cloud → go to Settings → Secrets → paste your key there.

🧩 Models Used

Content-Based Filtering:
Uses metadata (genres, cast, keywords, director, tagline) to find similar movies.

Cosine Similarity:
Computes similarity between movie feature vectors.

TF-IDF Vectorization:
Extracts weighted importance of words to represent movie features numerically.

🚀 Future Enhancements

🔹 Add Hybrid Recommendation Model (merge collaborative & content-based filtering)
🔹 Use Deep Learning (Autoencoders) for better personalization
🔹 Integrate User Login & Watch History
🔹 Include Real-Time Trending Movies (via TMDB API)
🔹 Enhance UI with cinematic animations & background music

🤝 Contributing

Contributions are always welcome!
If you’d like to improve the UI, optimize algorithms, or add features:

Fork the repo

Create a new branch (feature/new-feature)

Commit changes

Submit a pull request

🧑‍💻 Developed By

Sudhanshu Kumar
🎓 IIIT Pune |
📫 portfolio-sudhanshu-one.vercel.app

💼 Passionate about AI, Web Development, and Clean UI Design

⭐ Show Your Support

If you like this project, please consider giving it a ⭐ on GitHub —
Your support inspires me to keep building awesome stuff! 💖
