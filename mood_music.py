import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score

# Load the dataset
df = pd.read_csv("/Users/HP/Downloads/mood_playlist_project/SpotifyFeatures.csv")

# Preview the data
print(df.head())
print(df.columns)

# Input-output or relevant features:
features = ['valence', 'energy', 'danceability', 'acousticness']
target = 'Mood'

# Mood mapping logic (simple rule-based for speed)
def mood_mapper(row):
    if row['valence'] > 0.6 and row['energy'] > 0.6:
        return 'happy'
    elif row['valence'] < 0.4 and row['energy'] < 0.4:
        return 'sad'
    elif row['danceability'] > 0.5 and row['energy'] > 0.7:
        return 'energetic'
    elif row['acousticness'] > 0.6 and row['valence'] > 0.5:
        return 'chill'
    elif row['valence'] > 0.5 and row['acousticness'] > 0.4 and row['danceability'] < 0.6:
        return 'romantic'
    else:
        return 'chill'  # Default fallback

# Apply mood mapping to the dataframe
df['Mood'] = df.apply(mood_mapper, axis=1)

# Encode mood labels
label_encoder = LabelEncoder()
df['Mood_encoded'] = label_encoder.fit_transform(df['Mood'])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df[features], df['Mood_encoded'], test_size=0.2, random_state=42)  # 20% for testing, 80% for training

# Train Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Function to predict mood using ML
def predict_mood(valence, energy, danceability, acousticness):
    mood_encoded = clf.predict([[valence, energy, danceability, acousticness]])[0]
    return label_encoder.inverse_transform([mood_encoded])[0]

# Function to get playlist directly based on mood (no need for valence, energy, etc.)
def get_playlist(mood, n=10):
    playlist = df[df['Mood'] == mood].sample(n=n, random_state=42)
    return playlist[['track_name', 'artist_name', 'genre', 'Mood']]



#Testing Accuracy:

# Evaluate accuracy on the test set
test_accuracy = clf.score(X_test, y_test)
print(f"Test set accuracy: {test_accuracy:.4f}")


# Perform 5-fold cross-validation on the training data
cv_scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy')

# Print the mean and standard deviation of the accuracy across the folds
print(f"Cross-validated accuracy: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
