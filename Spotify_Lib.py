import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os 
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
secret_id = os.getenv("secret_id")
print(client_id, secret_id) 

scope = "user-library-read"
redirect = "http://127.0.0.1:8000/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=secret_id,redirect_uri=redirect,scope=scope))

#max limit is 50 be carful
# results = sp.current_user_saved_tracks(limit = 50)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

#practice run
reading = "playlist-read-public"
sp_read = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=secret_id,redirect_uri=redirect,scope=reading))
results = sp.current_user_saved_albums(limit = 50)
for idx, item in enumerate(results['items']):
    track = item#['track']
    print(idx, track)#['artists'][0]['name'], " – ", track['name'])