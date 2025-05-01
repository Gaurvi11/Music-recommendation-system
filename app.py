import streamlit as st
import pandas as pd
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "d1a28e94c4414b81a6af3ade3a816e6e"
CLIENT_SECRET = "45c56366efef4eaa91a9cb64f9baff2e"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load model and data
music_dict = pickle.load(open('spotify.pkl', 'rb'))
music = pd.DataFrame(music_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def get_song_details(song_name, artist_name):
    """Fetch the album cover image URL and Spotify play link."""
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        song_url = track["external_urls"]["spotify"]
        return album_cover_url, song_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png", None

def recommend(song):
    """Recommend songs based on similarity."""
    if song not in music['song'].values:
        return [], [], []

    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_links = []

    for i in distances[1:6]:  # Top 5 recommendations
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        cover_url, song_url = get_song_details(song_name, artist)

        recommended_music_names.append(song_name)
        recommended_music_posters.append(cover_url)
        recommended_music_links.append(song_url)

    return recommended_music_names, recommended_music_posters, recommended_music_links

# Streamlit UI
st.title("🎵 Music Recommendation System")

selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music['song'].values
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters, recommended_music_links = recommend(selected_song)

    if recommended_music_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.text(recommended_music_names[idx])
                st.image(recommended_music_posters[idx])
                if recommended_music_links[idx]:
                    st.markdown(f"[🎧 Play on Spotify]({recommended_music_links[idx]})")
                else:
                    st.write("🔍 Song not found on Spotify.")
    else:
        st.error("No recommendations found!")