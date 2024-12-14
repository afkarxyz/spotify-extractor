from spotapi.public import Public
import json

playlist_id = "37i9dQZEVXbNG2KDcFcKOF"
for playlist_items in Public.playlist_info(playlist_id):
    print(json.dumps(playlist_items, indent=2))
