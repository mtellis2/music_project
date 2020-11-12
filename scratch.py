import os
import tekore as tk

client_id = os.environ.get("SPOT_CLIENT_ID")
secret_client_id = os.environ.get("SPOT_SECRET_CLIENT_ID")
app_token = tk.request_client_token(client_id, secret_client_id)

# conf = tk.config_from_environment()

# token = tk.prompt_for_user_token(app_token)


spotify = tk.Spotify(app_token)

playlist = spotify.followed_playlists(limit=1).items[0]
track = spotify.playlist_items(playlist.id, limit=1).items[0].track
name = f'"{track.name}" from {playlist.name}'


# album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
# for track in album.tracks.items:
#     print(track.track_number, track.name)

