# Music Recommendation System

This is a Music Recommendation System built with Python, Streamlit, and Docker. It provides users with personalized music suggestions based on their preferences using the Spotify API.

---

## Live Deployment on AWS EC2

You can deploy this project to an AWS EC2 instance using Docker.

👉 Follow the guide here:** [aws_deployment.md](./aws_deployment.md)

---

## Technologies Used

- Python
- Streamlit
- Spotipy (Spotify API wrapper)
- Docker
- AWS EC2 (for deployment)

---

## Setup Locally

```bash
git clone https://github.com/Gaurvi11/Music-recommendation-system.git
cd Music-recommendation-system
pip install -r requirements.txt
streamlit run app.py

Docker Usage
docker build -t music-recommender .
docker run -p 8501:8501 music-recommender
