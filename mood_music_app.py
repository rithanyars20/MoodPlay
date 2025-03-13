import streamlit as st
from mood_music import get_playlist

st.title("🎵 MoodPlay: an AI-Powered Mood-based Music Playlist Generator")

# Mood selection
mood_options = ["Happy", "Chill", "Romantic", "Sad", "Energetic"]
selected_mood = st.radio("How are you feeling today?", mood_options, horizontal=True)

if st.button("Generate Playlist"):
    playlist = get_playlist(selected_mood.lower(), n=100)

    st.subheader(f"Playlist for {selected_mood} Mood 🎧")

    for _, row in playlist.iterrows():
        st.write(f"🎶 **{row['track_name']}** by *{row['artist_name']}* [{row['genre']}]")

        