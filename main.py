import pandas as pd

column = ['Position', 'Track Name', 'Artist', 'Streams', 'URL', 'Date', 'Region']
spotify_data = pd.read_csv('data.csv', names=column)

#print(spotify_data.head())

artists = spotify_data.Artist
#print(artists.value_counts())

tracks = spotify_data['Track Name']
#print(tracks.value_counts())

globe = spotify_data[spotify_data.Region == 'global']
#print(globe.head())

usa = spotify_data[spotify_data.Region == 'us']
#print(top_usa.head())

argentina = spotify_data[spotify_data.Region == 'ec']
#print(top_argentina.head())

britain = spotify_data[spotify_data.Region == 'gb']
#print(top_britain.head())

mexico = spotify_data[spotify_data.Region == 'mx']
#print(top_mexico.head())

taiwan = spotify_data[spotify_data.Region == 'tw']
#print(top_taiwan.head())

singapore = spotify_data[spotify_data.Region == 'sg']
#print(top_singapore.head())

top_globe = globe.groupby("Track Name").agg({'Streams': 'sum'})
top_globe = top_globe.sort_values(['Streams'], ascending = False)
top_globe['country'] = 'Globe'

top_argentina = argentina.groupby("Track Name").agg({'Streams': 'sum'})
top_argentina = top_argentina.sort_values(['Streams'], ascending = False)
top_argentina['country'] = 'Argentina'

top_usa = usa.groupby('Track Name').agg({'Streams': 'sum'})
top_usa = top_usa.sort_values(['Streams'], ascending = False)
top_usa['country'] = 'USA'

top_britain = britain.groupby('Track Name').agg({'Streams': 'sum'})
top_britain = top_britain.sort_values(['Streams'], ascending = False)
top_britain['country'] = 'Great Britain'

top_mexico = mexico.groupby('Track Name').agg({'Streams': 'sum'})
top_mexico = top_mexico.sort_values(['Streams'], ascending = False)
top_mexico['country'] = 'Mexico'

top_taiwan = taiwan.groupby('Track Name').agg({'Streams': 'sum'})
top_taiwan = top_taiwan.sort_values(['Streams'], ascending = False)
top_taiwan['country'] = 'Taiwan'

top_singapore = singapore.groupby('Track Name').agg({'Streams': 'sum'})
top_singapore = top_singapore.sort_values(['Streams'], ascending = False)
top_singapore['country'] = 'Singapore'


top_globe['prop'] = top_globe['Streams']/sum(top_globe['Streams']) * 100
top_argentina['prop'] = top_argentina['Streams']/sum(top_argentina['Streams']) * 100
top_usa['prop'] = top_usa['Streams']/sum(top_usa['Streams']) * 100
top_britain['prop'] = top_britain['Streams']/sum(top_britain['Streams']) * 100
top_mexico['prop'] = top_mexico['Streams']/sum(top_mexico['Streams']) * 100
top_singapore['prop'] = top_singapore['Streams']/sum(top_singapore['Streams']) * 100
top_taiwan['prop'] = top_taiwan['Streams']/sum(top_taiwan['Streams']) * 100

top_globe = top_globe[0:3]
#print(top_globe)
top_usa = top_usa[0:3]
#print(top_usa)
top_britain = top_britain[0:3]
#print(top_britain)
top_mexico = top_mexico[0:3]
#print(top_mexico)
top_singapore = top_singapore[0:3]
#print(top_singapore)
top_taiwan = top_taiwan[0:3]
#print(top_taiwan)
top_argentina = top_argentina[0:3]

del top_taiwan['Streams']
del top_singapore['Streams']
del top_mexico['Streams']
del top_britain['Streams']
del top_usa['Streams']
del top_globe['Streams']
del top_argentina['Streams']

top_merged = top_globe.append([top_usa, top_argentina, top_britain, top_mexico, top_singapore, top_taiwan])

top_merged = top_merged.reset_index()

tracks = top_merged['Track Name'].value_counts()
tracks = tracks.reset_index()
#print(len(top_merged['Track Name'].value_counts()))

top_globe_artist = globe.groupby('Artist').agg({'Streams': 'sum'})
top_globe_artist = top_globe_artist.sort_values(['Streams'], ascending = False)
top_globe_artist['country'] = 'Globe'
top_globe_artist['prop'] = top_globe_artist['Streams'] / sum(top_globe_artist['Streams']) * 100
top_globe_artist = top_globe_artist[0:3]

top_usa_artist = usa.groupby('Artist').agg({'Streams': 'sum'})
top_usa_artist = top_usa_artist.sort_values(['Streams'], ascending = False)
top_usa_artist['country'] = 'USA'
top_usa_artist['prop'] = top_usa_artist['Streams'] / sum(top_usa_artist['Streams']) * 100
top_usa_artist = top_usa_artist[0:3]

#print(top_globe_artist)
#print(top_usa_artist)

top_artists = top_globe_artist.append([top_usa_artist])
#print(top_artists)

ed_sheeran = spotify_data[spotify_data.Artist == 'Ed Sheeran']
ed_sheeran_tracks = ed_sheeran.groupby('Track Name').agg({'Streams': 'sum'})
ed_sheeran_tracks = ed_sheeran_tracks.sort_values(['Streams'], ascending = False)
#print(ed_sheeran_tracks)

region_contribution = spotify_data.groupby(['Region']).agg({'Streams': 'sum'})
region_contribution['prop'] = region_contribution['Streams'] / sum(region_contribution['Streams']) * 100
region_contribution = region_contribution.sort_values(['prop'], ascending = False)
#print(region_contribution)

artist_region = spotify_data.groupby(['Artist', 'Region']).agg({'Streams': 'sum'})
artist_region_g = artist_region['Streams'].groupby(level=0, group_keys=False)

'''
import plotly.offline as py
import plotly.graph_objs as go
'''
'''
trace1 = go.Bar(
    x = ['Globe', 'USA', 'Argentina', 'Great Britain', 'Singapore', 'Taiwan', 'Mexico'],
    y = [1.940598, 0, 1.651465, 1.838745, 2.047684, 1.742562, 0],
    name = 'Shape of You'
)

trace2 = go.Bar(
    x = ['Globe', 'USA', 'Argentina', 'Great Britain', 'Singapore', 'Taiwan', 'Mexico'],
    y = [0.966961, 0, 1.770332, 0, 0, 0, 1.574358],
    name = 'Despacito (Featuring Daddy Yankee)'
)

data = [trace1, trace2]
layout = go.Layout(barmode = 'stack')
fig = go.Figure(data = data, layout = layout)
py.plot(fig, filename='top-songs.html')

trace1 = go.Bar(
    x = ['Globe', 'USA'],
    y = [5.935890, 0],
    name = 'Ed Sheeran'
)

trace2 = go.Bar(
    x = ['Globe', 'USA'],
    y = [2.913904, 4.742044],
    name = 'Drake'
)

trace3 = go.Bar(
    x=['Globe', 'USA'],
    y = [2.877906, 0],
    name = 'The Chainsmokers'
)

trace4 = go.Bar(
    x=['Globe', 'USA'],
    y = [0, 4.412325],
    name = 'Kendrick Lamar'
)

trace5 = go.Bar(
    x=['Globe', 'USA'],
    y = [0, 3.748599],
    name = 'Post Malone'
)

data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(barmode = 'stack')
fig = go.Figure(data = data, layout = layout)
py.plot(fig, filename = 'top-artists.html')
'''