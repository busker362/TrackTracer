import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.oauth = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        )

    def get_auth_url(self):
        """Spotify 인증 URL 반환"""
        return self.oauth.get_authorize_url()

    def get_access_token(self, code):
        """인증 코드로 액세스 토큰 가져오기"""
        return self.oauth.get_access_token(code)

    def get_user_info(self, access_token):
        """사용자 정보 가져오기"""
        sp = spotipy.Spotify(auth=access_token)
        return sp.current_user()
    

    def get_user_top_tracks(self, access_token, limit=5, time_range="long_term"):
        sp = spotipy.Spotify(auth=access_token)
        top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        return [
            {
                "rank": idx + 1,
                "name": track["name"],
                "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                "album": track["album"]["name"],
                "album_image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,
                "preview_url": track.get("preview_url")  # 미리듣기 URL
            }
            for idx, track in enumerate(top_tracks["items"])
        ]

    def get_access_token(self, code=None):
        """인증 코드로 액세스 토큰 가져오기 또는 갱신"""
        token_info = self.oauth.get_cached_token()
        if not token_info:
            token_info = self.oauth.get_access_token(code)
        return token_info
        