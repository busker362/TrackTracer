import requests
import json

class YoutubeAPI:
    def __init__(self, config_path="./backend/config.json"):
        # config.json에서 API 키 로드
        with open(config_path) as f:
            config = json.load(f)
        self.YOUTUBE_API_KEY = config["youtube_api_key"]

    def search_videos(self, query, max_results=5):
        # API URL 생성
        youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&maxResults={max_results}&key={self.YOUTUBE_API_KEY}"
        
        # API 요청
        response = requests.get(youtube_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "YouTube API call failed"}
