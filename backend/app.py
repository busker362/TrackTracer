from flask import Flask, render_template, request, redirect, jsonify, session
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Spotify API 인증 설정
with open("./backend/config.json") as f:
    config = json.load(f)

CLIENT_ID = config["client_id"]
CLIENT_SECRET = config["client_secret"]
REDIRECT_URI = "http://127.0.0.1:5000/api/callback"
SECRET_KEY = config["secret_key"]

# SpotifyOAuth 객체 생성
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-read-private user-top-read"
)

# Flask 애플리케이션 초기화
app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), "frontend/templates"),
    static_folder=os.path.join(os.getcwd(), "frontend/static")
)
app.secret_key = SECRET_KEY

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



#스포티파이 API를 받아오기 위해서 연결해야함 
@app.route("/login", methods=["GET"])
def login():
    auth_url = sp_oauth.get_authorize_url()  # Spotify 인증 URL 반환
    return redirect(auth_url)

#로그인 버튼을 누른 후 인증 코드를 받아올 메서드
@app.route("/api/callback", methods=["GET"])
def callback():
    code = request.args.get("code")  # 인증 코드 가져오기

    try:
        token_info = sp_oauth.get_access_token(code)
        session["token_info"] = token_info
        sp = spotipy.Spotify(auth=token_info["access_token"])                 # Spotipy 객체 초기화
       
        # 사용자 정보 가져오기
        user_info = sp.current_user()

        #사용자 Top Tracks 가져오기
        top_tracks = sp.current_user_top_tracks(limit=5, time_range="long_term") # 최대 5곡

        # 필요한 정보만 정리
        track_data = [
            {
                "rank": idx + 1,
                "name": track["name"],
                "artists": ", ".join([artist["name"] for artist in track["artists"]]),
                "album": track["album"]["name"],
                "album_image": track["album"]["images"][0]["url"] if track["album"]["images"] else None,  # 앨범 이미지 URL
                #"preview_url": track.get("preview_url")  # 미리 듣기 URL (없을 수도 있음)
            }
            for idx, track in enumerate(top_tracks["items"])
        ]

        playlists = sp.current_user_playlists(limit=50)
        playlist_data = [
            {
                "id": playlist["id"],
                "name": playlist["name"],
                "tracks": playlist["tracks"]["total"]
            }
            for playlist in playlists["items"]
        ]

        return render_template(
            "home.html",
            user=user_info,
            tracks=track_data,
            playlists=playlist_data,
            message="당신이 가장 많이 재생한 곡과 플레이 리스트를 확인하세요!"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # 에러처리 

    
if __name__ == "__main__":
    app.run(debug=True)
