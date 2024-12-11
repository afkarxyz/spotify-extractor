import json
from spotapi import PublicAlbum

def get_album_raw_json(album_url):
    album = PublicAlbum(album_url)
    return album.get_album_info()

album_url = "https://open.spotify.com/album/4VZ7jhV0wHpoNPCB7Vmiml"
raw_json = get_album_raw_json(album_url)
print(json.dumps(raw_json, indent=2))
