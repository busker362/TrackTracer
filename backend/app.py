from flask import Flask, render_template, request, redirect, jsonify, session
import json , os, requests, sys
from API.Spotify_API import SpotifyAPI
from API.Youtube_API import YoutubeAPI
from API.Lastfm_API import LastfmAPI
sys.stdout.reconfigure(encoding='utf-8')

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
    scope="user-library-read playlist-read-private playlist-read-collaborative user-top-read"
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
    try:
        # 세션에서 사용자 데이터와 재생목록 가져오기
        user_info = session.get("user_info", None)
        playlist_data = session.get("playlists", [])
        track_data = session.get("tracks", [])

        # 디버깅 로그
        print("Debug: User Info in Session:", user_info)
        print("Debug: Playlist Data in Session:", playlist_data)
        print("Debug: Track Data in Session:", track_data)

        return render_template(
            "home.html",
            user=user_info,
            playlists=playlist_data,
            tracks=track_data,  # preview_url 포함된 모든 곡 전달
            message="당신이 가장 많이 재생한 곡과 플레이 리스트를 확인하세요!"
        )
    except Exception as e:
        print("Error in home route:", str(e))
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

@app.route("/login", methods=["GET"])
def login():
    """Spotify 로그인 URL로 리다이렉트"""
    auth_url = spotify_api.get_auth_url()
    return redirect(auth_url)

@app.route("/api/callback", methods=["GET"])
def callback():
    try:
        code = request.args.get("code")
        if not code:
            return jsonify({"error": "Authorization code not found"}), 400

        # Access token 가져오기
        token_info = spotify_api.get_access_token(code)
        session["token_info"] = token_info
        access_token = token_info["access_token"]

        # 사용자 정보 및 곡 데이터 가져오기
        user_info = spotify_api.get_user_info(access_token)
        track_data = spotify_api.get_user_top_tracks(access_token)

        session["user_info"] = user_info
        session["tracks"] = track_data  # 미리듣기 URL 포함

        return redirect("/")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500
    
@app.route("/logout", methods=["GET"])
def logout():
    """로그아웃: 세션 데이터 제거 후 메인 페이지로 리다이렉트"""
    session.clear()  
    print("User logged out.")  
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
