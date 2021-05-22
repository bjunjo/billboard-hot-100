# billboard-hot-100
## Problem: Add Billboard's Hot 100 songs from the specified date
## Solutions:

1. Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret.
```
scope = "playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope=scope,
    cache_path="token.txt",
    show_dialog=True
    ))
user_id = sp.current_user()["id"]
print(f"user_id: {user_id}")
```
2. Scraping the Billboard Hot 100-Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List
```
# Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format.
travel_date = input("What year would you like to travel to? (format: YYYY-MM-DD) ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_date}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
songs_list_with_tags = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
songs_list = [song.text for song in songs_list_with_tags]
```
3. Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).
```
song_uris = []
year = travel_date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} can't be found on Spotify.")
```
4. Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date you inputted in step 1.
```
new_playlist = sp.user_playlist_create(user=os.getenv("USER_ID"), name=f"{travel_date} Billboard 100", public=False, description="Testing API in Python")
playlist_id = new_playlist['id']
```
5. Add each of the songs found in Step 3 to the new playlist.
```
sp.playlist_add_items(playlist_id, song_uris)
```
## Lessons
1.API is awesome. Once I figure out how it works, it does stuff automatically.
2. Authentication then implementation
