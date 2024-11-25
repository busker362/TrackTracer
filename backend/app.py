from flask import Flask, render_template, request, redirect, jsonify, session
import json , os, requests
from API.Spotify_API import SpotifyAPI
from API.Youtube_API import YoutubeAPI
from API.Lastfm_API import LastfmAPI

# Spotify API 설정 로드
with open("./backend/config.json") as f:
    config = json.load(f)

YOUTUBE_API_KEY = config["youtube_api_key"]
LASTFM_API_KEY = config["lastfm_api_key"]
LASTFM_SECRET_KEY = config["lastfm_secret_key"]

# SpotifyAPI 객체 생성
spotify_api = SpotifyAPI(
    client_id=config["client_id"],
    client_secret=config["client_secret"],
    redirect_uri="http://127.0.0.1:5000/api/callback",
    scope="user-library-read playlist-read-private user-top-read"
)

# Flask 애플리케이션 초기화
app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), "frontend/templates"),
    static_folder=os.path.join(os.getcwd(), "frontend/static")
)
app.secret_key = config["secret_key"]

@app.route("/")
def home():
    token_info = session.get("token_info", None)
    access_token = token_info["access_token"] if token_info else None
    print("Access Token from Flask:", access_token)  # 디버깅용 로그 추가
    return render_template(
        "home.html",
        user=None,
        playlists=[],
        message="Hello!",
        access_token=access_token  # HTML로 전달
    )

@app.route("/login", methods=["GET"])
def login():
    """Spotify 로그인 URL로 리다이렉트"""
    auth_url = spotify_api.get_auth_url()
    return redirect(auth_url)

@app.route("/api/callback", methods=["GET"])
def callback():
    """Spotify 인증 후 콜백 처리"""
    code = request.args.get("code")  # 인증 코드 가져오기
    try:
        token_info = spotify_api.get_access_token(code)
        session["token_info"] = token_info

        access_token = token_info["access_token"]

        # 사용자 정보 가져오기
        user_info = spotify_api.get_user_info(access_token)

        # 사용자 Top Tracks 가져오기
        track_data = spotify_api.get_user_top_tracks(access_token)

        # 사용자 플레이리스트 가져오기
        playlist_data = spotify_api.get_user_playlists(access_token)
        playlist_data.reverse()
        
        return render_template(
            "home.html",
            user=user_info,
            tracks=track_data,
            playlists=playlist_data,
            message="당신이 가장 많이 재생한 곡과 플레이 리스트를 확인하세요!"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":
    app.run(debug=True)
