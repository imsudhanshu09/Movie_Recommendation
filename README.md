# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System** — a smart, cinematic web app that helps you discover movies similar to your favorites.  
Built using **Python**, **Streamlit**, and **Machine Learning**, it combines data-driven intelligence with a stunning UI inspired by the magic of cinema.

---

## 🌐 Live Demo
🎥 **Try it here:** [Movie Recommendation App](https://imsudhanshu09-movie-recommendation-app-uxojgu.streamlit.app/)

---

## ⚙️ Tech Stack

- **Language:** Python 🐍  
- **Framework:** Streamlit  
- **Data Handling:** pandas, numpy  
- **Machine Learning:** scikit-learn (TF-IDF, Cosine Similarity)  
- **API Integration:** TMDB (for fetching real movie posters)  
- **Frontend Styling:** Custom CSS, responsive cinematic UI with gradient overlays  

---

## ✨ Features

- 🎯 **Smart Recommendations** – Suggests movies based on similarity in genres, keywords, cast, and more.  
- 🎬 **Interactive Streamlit UI** – Dark theme with glowing titles, animated buttons, and elegant layout.  
- 🖼️ **TMDB Poster Integration** – Fetches high-quality posters for each recommended movie.  
- ⚡ **Optimized Performance** – Uses `@st.cache_data` and `@st.cache_resource` for faster load times.  
- 🔍 **Search Functionality** – Instantly find and explore movies by name.  
- 📱 **Fully Responsive** – Scales beautifully across desktop, tablet, and mobile.  

---

## 🧠 How It Works

The system uses **content-based filtering**, where each movie is represented using its textual metadata:

- 🎭 Genres  
- ✍️ Keywords  
- 💬 Taglines  
- 👨‍🎤 Cast  
- 🎬 Director  

These are vectorized using **TF-IDF**, and **cosine similarity** is computed between vectors to find the most similar movies.

---

## 🧰 Libraries Used

| Library | Purpose |
|----------|----------|
| **pandas** | Data manipulation |
| **numpy** | Numerical operations |
| **scikit-learn** | TF-IDF & similarity computation |
| **streamlit** | Interactive frontend |
| **requests** | Fetching posters from TMDB API |

---

## 🖥️ UI Highlights

🎥 **Cinematic Background**  
Responsive movie-themed background with gradient overlay for a professional, theater-like feel.  

✨ **Glowing Typography**  
Neon-styled titles that give your app a dramatic look.  

🍿 **Poster Cards**  
Movie cards with hover effects, rounded edges, and real-time poster loading.  

📱 **Mobile-Ready Design**  
Background automatically adjusts to fill the viewport — no cropping or black gaps.  

---

## 📦 Installation & Usage

### 🧩 Step 1 — Clone the Repository
```bash
git clone https://github.com/imsudhanshu09/Movie_Recommendation.git
```
### 🧩 Step 2 — Navigate to the Project Folder
```bash
cd Movie_Recommendation
```
### 🧩 Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### 🧩 Step 4 — Run the Streamlit App
```bash
streamlit run app.py
```

Then open:
👉 http://localhost:8501

### 🧩 Step 5 — Use the App
- 🎞️ **Enter the name of your favorite movie**  
- ✨ **Click “Show Recommendations”**  
- 🍿 **Instantly view 10 similar movies — complete with titles and posters**  

## 🔐 API Key Setup (TMDB)
To fetch posters, add your TMDB API key securely using Streamlit’s secrets system:

### Step 1 — Create .streamlit/secrets.toml
```toml
TMDB_API_KEY = "your_tmdb_api_key_here"
```
### Step 2 — Add to .gitignore
```bash
.streamlit/secrets.toml
```
### Step 3 — For Streamlit Cloud:
Go to Settings → Secrets, and paste:

```ini
TMDB_API_KEY = "your_tmdb_api_key_here"
```
## 🧩 Models Used
### Content-Based Filtering:
Uses textual metadata to find movies with similar features.

### TF-IDF Vectorization:
Converts text data into numerical feature vectors.

### Cosine Similarity:
Measures the angle between movie vectors to find the closest matches.

## 🚀 Future Enhancements  

- 🤖 **Hybrid Filtering** – Combines content-based and collaborative approaches for more personalized movie recommendations.  
- 🧠 **Deep Learning Models** – Introduces advanced models like Autoencoders and NLP embeddings for enhanced accuracy.  
- 🎞️ **Trending & Popular Movies** – Displays real-time trending movies using the TMDB API integration.  
- 🧍 **User Login & Watch History** – Adds user authentication and personalized history-based recommendations.  
- 💻 **Cinematic UI Enhancements** – Features parallax scrolling, smooth transitions, and dynamic visual effects for a more immersive experience.  


## 🧑‍💻 Author  

**Sudhanshu Kumar**  
🎓 IIIT Pune | QuantNum Math Club Head  
💼 Passionate about Machine Learning, Web Development, and Clean Design  
🌐 [Portfolio Website](https://portfolio-sudhanshu-one.vercel.app/)  
🔗 [GitHub](https://github.com/imsudhanshu09) | [LinkedIn](https://www.linkedin.com/in/sudhanshu-kumar-a6657a287)  

---

## 🤝 Contributing  

Contributions are welcome!  
To contribute:  

```bash
1. Fork the repository  
2. Create a new branch: git checkout -b feature-name  
3. Commit your changes: git commit -m "Added a cool feature"  
4. Push the branch: git push origin feature-name  
5. Submit a pull request 🎉  
```
## 📝 License
This project is licensed under the [MIT License](LICENSE).
You’re free to use, modify, and distribute it with proper attribution.

⭐ Support
If you liked this project, please give it a ⭐ on GitHub!
