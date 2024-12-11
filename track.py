import json
from spotapi import Song

def get_track_raw_json(track_url):
    track_id = track_url.split('/')[-1]
    song = Song()
    return song.get_track_info(track_id)

track_url = "https://open.spotify.com/track/2plbrEY59IikOBgBGLjaoe"
raw_json = get_track_raw_json(track_url)
print(json.dumps(raw_json, indent=2))
