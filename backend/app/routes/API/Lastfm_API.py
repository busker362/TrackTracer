import requests
import json

class LastfmAPI:
    def __init__(self, config_path="./backend/config.json"):
        # config.json에서 API 키 로드
        with open(config_path) as f:
            config = json.load(f)
        self.LASTFM_API_KEY = config["lastfm_api_key"]

    def get_artist_info(self, artist_name):
        # API URL 생성
        lastfm_url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={self.LASTFM_API_KEY}&format=json"
        
        # API 요청
        response = requests.get(lastfm_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Last.fm API call failed"}
