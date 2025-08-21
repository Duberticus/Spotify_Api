import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os 
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
secret_id = os.getenv("secret_id")
print(client_id, secret_id) 

# auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret_id)
# sp = spotipy.Spotify(auth_manager=auth_manager)

# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None