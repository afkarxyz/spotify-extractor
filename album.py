import json
from spotapi.public import Public

def get_album_raw_json(album_url):
    album_id = album_url.split('/')[-1]
    return next(Public.album_info(album_id))

album_url = "https://open.spotify.com/album/4VZ7jhV0wHpoNPCB7Vmiml"
raw_json = get_album_raw_json(album_url)
print(json.dumps(raw_json, indent=2))
