import json
from spotapi.public import Public

def get_track_raw_json(track_url):
    track_id = track_url.split('/')[-1]
    return Public.song_info(track_id)

track_url = "https://open.spotify.com/track/2plbrEY59IikOBgBGLjaoe"
raw_json = get_track_raw_json(track_url)
print(json.dumps(raw_json, indent=2))
