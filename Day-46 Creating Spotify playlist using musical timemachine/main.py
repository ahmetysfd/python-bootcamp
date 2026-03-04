from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print(song_names)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="7043e8f5627a4df4877754a938b1e747",
    client_secret="ff8ce5c2d59b4ddc9ab4a46377a183a2",
    redirect_uri="https://example.com/callback",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    username="ahmetyusuf21",
))

user_id = sp.current_user()["id"]
print(user_id)

track_uris = []


for song in song_names:
    result = sp.search(q=f"track:{song}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)

    except IndexError:
        print(f"Not found: {song}")

playlist = sp.user_playlist_create(
    user=user_id,
    name=date + "Billboard 100",
    public=False,  # False = private playlist
    description="Created with Spotipy"
)
sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
