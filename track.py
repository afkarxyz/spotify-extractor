from spotapi.public import Public
import json

track_id = "2plbrEY59IikOBgBGLjaoe"
track_info = Public.song_info(track_id)
print(json.dumps(track_info, indent=2))
