import pandas as pd

column = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region']
spotify_data = pd.read_csv('data.csv', names=column)

print(spotify_data.head())

artists = spotify_data.Artist
print(artists.value_counts())

tracks = spotify_data['Track Name']
print(tracks.value_counts())


