import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from lyricsgenius import Genius
from bs4 import BeautifulSoup
import re
import urllib

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='63c44819648446c4a912ef816b316eb8', client_secret='7da782d0b9a94d679425bb20fbc4e1da', redirect_uri='http://localhost:8888/callback/', scope=['user-library-read']))

playlist_id = "7god392LYtMerP7cISvyDJ"
username = "Bhargav Chirravuri"
access_token = "6xJB3zvFP3WThcY1DZP2xTjyDzOYU1AB7cDeapkZs-ENucboyiqPmb2OtdmR1bhT"
headers = {'Authorization': "Bearer " + access_token}

results = sp.user_playlist_tracks(username, playlist_id)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

songTitles = []
songArtists = []
count = 0
for track in tracks:
    songTitle = track['track']['name']
    songArtist = track['track']['artists'][0]['name']
    songTitles.append(songTitle)
    songArtists.append(songArtist)
    count += 1

genius = Genius(access_token)
matchCount = 0
matches = []
for i in range(count):
    try:
        song = genius.search_song(songTitles[i], songArtists[i]).lyrics
        if (song.find("I put a spell on you") != -1):
            print("\n\nMATCH FOUND\n")
            matchCount += 1
            matches.append(songTitles[i])
    except:
        pass

print("Report:")
print(str(matchCount) + " matches found.")
for match in matches:
    print("Match: " + str(match))