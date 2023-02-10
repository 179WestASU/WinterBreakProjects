from lyricsgenius import Genius
access_token = "6xJB3zvFP3WThcY1DZP2xTjyDzOYU1AB7cDeapkZs-ENucboyiqPmb2OtdmR1bhT"

genius = Genius(access_token)
artist = genius.search_artist('Andy Shauf', max_songs=0)
song = genius.search_song('To You', artist.name)
# same as: song = genius.search_song('To You', 'Andy Shauf')
print(song.lyrics)