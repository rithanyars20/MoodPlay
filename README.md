# MoodPlay
## AI-Powered Mood-Based Music Playlist Generator
This project is an AI-based music playlist generator that predicts the mood of a track and creates personalized playlists based on the user's current mood. The model is built using a Random Forest Classifier and leverages audio features from Spotify to perform mood predictions.

## Features
### Mood-based Playlist Generation: 
Select a mood, and the system generates a playlist that matches it.
### Mood Prediction Model: 
Trained on various audio features like energy, danceability, acousticness, and more to predict moods such as "Happy", "Chill", "Energetic", "Sad", and "Romantic".
### Streamlit Web App: 
An interactive UI that allows users to easily input moods and get generated playlists.

## Dataset

The dataset used for this project is available on Kaggle. You can access it here

https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db


## Technologies Used

Python (Primary language)
Scikit-learn (For building and training machine learning models)
Spotify API (For fetching music data)
Streamlit (For building the web interface)
Pandas (For data manipulation)


## How It Works

Data Collection: Music data is fetched from Spotify's API, which includes features like valence, energy, danceability, and more.
Mood Mapping: A rule-based system assigns moods to the songs based on their audio features.
Model Training: A Random Forest Classifier is used to predict moods based on the features of the songs.
Playlist Generation: Based on the mood selected by the user, the app generates a playlist by sampling songs that match the predicted mood.

