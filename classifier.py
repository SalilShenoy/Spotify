import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns

import graphviz
import pydotplus
import io
from scipy import misc

data = pd.read_csv('data1.csv')
#print data.describe()
#print data.head()
#print data.info()

train, test = train_test_split(data, test_size = 0.15)

print("Training size: {}; Test size: {}".format(len(train), len(test)))

sns.set_style('white')

pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']
pos_acoust = data[data['target'] == 1]['acousticness']
neg_acoust = data[data['target'] == 0]['acousticness']
pos_dance = data[data['target'] == 1]['danceability']
neg_dance = data[data['target'] == 0]['danceability']
pos_duration = data[data['target'] == 1]['duration_ms']
neg_duration = data[data['target'] == 0]['duration_ms']
pos_energy = data[data['target'] == 1]['energy']
neg_energy = data[data['target'] == 0]['energy']
pos_instru = data[data['target'] == 1]['instrumentalness']
neg_instru = data[data['target'] == 0]['instrumentalness']
pos_key = data[data['target'] == 1]['key']
neg_key = data[data['target'] == 0]['key']
pos_liveliness = data[data['target'] == 1]['liveness']
neg_liveliness = data[data['target'] == 0]['liveness']
pos_loudness = data[data['target'] == 1]['loudness']
neg_loudness = data[data['target'] == 0]['loudness']
pos_mode = data[data['target'] == 1]['mode']
neg_mode = data[data['target'] == 0]['mode']
pos_speech = data[data['target'] == 1]['speechiness']
neg_speech = data[data['target'] == 0]['speechiness']
pos_ts = data[data['target'] == 1]['time_signature']
neg_ts = data[data['target'] == 0]['time_signature']
pos_valence = data[data['target'] == 1]['valence']
neg_valence = data[data['target'] == 0]['valence']

#fig = plt.Figure(figsize=(12, 8))
#plt.title("Song tempo Like / Dislike Distribution")

#pos_tempo.hist(alpha = 0.7, bins = 30, label = 'positive')
#neg_tempo.hist(alpha = 0.7, bins = 30, label = 'negative')
#plt.legend(loc = 'upper right')

fig2 = plt.figure(figsize=(15, 15))
ax3 = fig2.add_subplot(331)
ax3.set_xlabel('Danceability')
ax3.set_ylabel('Count')
ax3.set_title('Song Danceability')
pos_dance.hist(alpha=0.5, bins=30)
ax4 = fig2.add_subplot(331)
neg_dance.hist(alpha=0.5, bins=30)

ax5 = fig2.add_subplot(332)
ax5.set_xlabel('Tempo')
ax5.set_ylabel('Count')
ax5.set_title('Song Tempo')
pos_tempo.hist(alpha=0.5, bins=30)
ax6 = fig2.add_subplot( 332)
neg_tempo.hist(alpha=0.5, bins=30)

ax7 = fig2.add_subplot(333)
ax7.set_xlabel('Accoust')
ax7.set_ylabel('Count')
ax7.set_title('Song Accoust')
pos_acoust.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(333)
neg_acoust.hist(alpha=0.5, bins=30)

ax9 = fig2.add_subplot(334)
ax9.set_xlabel('Duration')
ax9.set_ylabel('Count')
ax9.set_title('Song Duration')
pos_duration.hist(alpha=0.5, bins=30)
ax10 = fig2.add_subplot(334)
neg_duration.hist(alpha=0.5, bins=30)

ax11 = fig2.add_subplot(335)
ax11.set_xlabel('Duration')
ax11.set_ylabel('Count')
ax11.set_title('Song Duration')
pos_energy.hist(alpha=0.5, bins=30)
ax12 = fig2.add_subplot(335)
neg_energy.hist(alpha=0.5, bins=30)

ax13 = fig2.add_subplot(336)
ax13.set_xlabel('Duration')
ax13.set_ylabel('Count')
ax13.set_title('Song Duration')
pos_instru.hist(alpha=0.5, bins=30)
ax14 = fig2.add_subplot(336)
neg_instru.hist(alpha=0.5, bins=30)

ax15 = fig2.add_subplot(337)
ax15.set_xlabel('Key')
ax15.set_ylabel('Count')
ax15.set_title('Song Key')
pos_key.hist(alpha=0.5, bins=30)
ax16 = fig2.add_subplot(337)
neg_key.hist(alpha=0.5, bins=30)

ax17 = fig2.add_subplot(338)
ax17.set_xlabel('Key')
ax17.set_ylabel('Count')
ax17.set_title('Song Key')
pos_liveliness.hist(alpha=0.5, bins=30)
ax18 = fig2.add_subplot(338)
neg_liveliness.hist(alpha=0.5, bins=30)

ax19 = fig2.add_subplot(339)
ax19.set_xlabel('Loudness')
ax19.set_ylabel('Count')
ax19.set_title('Song Loudness')
pos_loudness.hist(alpha=0.5, bins=30)
ax20 = fig2.add_subplot(339)
neg_loudness.hist(alpha=0.5, bins=30)

#plt.show()

#Decision Tree Classifier
c = DecisionTreeClassifier(min_samples_split=100)
#Set of Features to be used by Decision Tree model
features = ['danceability', 'loudness', 'valence', 'energy', 'instrumentalness', 'acousticness', 'key',
            'speechiness', 'duration_ms', 'tempo', 'time_signature', 'mode']
X_train = train[features]
y_train = train['target']
X_test = test[features]
y_test = test['target']

#Create a model
dt = c.fit(X_train, y_train)


def show_tree(tr, feature, path):
    f = io.StringIO()
    export_graphviz(tr, out_file=f, feature_names=feature)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"] = (20, 20)
    plt.imshow(img)

show_tree(dt, features, 'dt_tree.png')

y_pred = c.predict(X_test)

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, y_pred) * 100

print 'Accuracy using decision tree: ', round(score, 1), '%'
