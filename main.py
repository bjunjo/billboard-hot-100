from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# TODO: Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret.
# scope = "playlist-modify-private"
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#     client_id=os.getenv("SPOTIPY_CLIENT_ID"),
#     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
#     redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
#     scope=scope,
#     cache_path="token.txt",
#     show_dialog=True
#     ))
# user_id = sp.current_user()["id"]
# print(f"user_id: {user_id}")

# TODO: Scraping the Billboard Hot 100
# Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format.
travel_date = input("What year would you like to travel to? (format: YYYY-MM-DD) ")

# TODO: Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List
response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_date}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
songs_list_with_tags = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# TODO: Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).
song_uris = []
songs_list = [song.search(q=f"track:{song} year:{travel_date}") for song in songs_list_with_tags]
print(f"Songs List: {songs_list}")

# with open("token.txt") as token:
#     header = token.read()
#     sp_search = "https://api.spotify.com/v1/search"
#     params = {
#         "q": songs_list[0],
#         "type": "track"
#     }
#     sp_response = requests.get(url=sp_search, params=params)
#     print(sp_response.status_code)
