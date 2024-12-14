from spotapi.public import Public
import json

artist_id = "0du5cEVh5yTK9QJze8zA0C"
for artist_items in Public.artist_search(artist_id):
    print(json.dumps(artist_items, indent=2))
