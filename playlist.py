import json
from spotapi import PublicPlaylist

def get_playlist_raw_json(playlist_url):
    playlist = PublicPlaylist(playlist_url)
    return playlist.get_playlist_info()

playlist_url = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
raw_json = get_playlist_raw_json(playlist_url)
print(json.dumps(raw_json, indent=2))
