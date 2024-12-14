import json
from spotapi.public import Public

def get_playlist_raw_json(playlist_url):
    playlist_id = playlist_url.split('/')[-1]
    return next(Public.playlist_info(playlist_id))

playlist_url = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
raw_json = get_playlist_raw_json(playlist_url)
print(json.dumps(raw_json, indent=2))
