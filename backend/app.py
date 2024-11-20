from flask import Flask, render_template, request, redirect, jsonify, session
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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
    scope="user-library-read playlist-read-private"
)

# Flask 애플리케이션 초기화
app = Flask(__name__)
app.secret_key = SECRET_KEY  

@app.route("/")
def home():
    message = "안녕하세요 시작해봅시다"
    return render_template("home.html", user=None, playlists=[], message=message)

#스포티파이 API를 받아오기 위해서 연결해야함 
@app.route("/login", methods=["GET"])
def login():
    auth_url = sp_oauth.get_authorize_url() #스포티파이 인증페이지 반환
    return redirect(auth_url)

#로그인 버튼을 누른 후 인증 코드를 받아올 메서드
@app.route("/api/callback", methods=["GET"])
def callback():
    code = request.args.get("code")         #받은 데이터를 가져올때 .args.get을 사용한다. 
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info["access_token"]

    session["token_info"] = token_info

    #spotipy api객체 초기화 
    sp = spotipy.Spotify(auth=access_token)
    #user정보 가져오기 
    user_info = sp.current_user()

    # 사용자 플레이리스트 가져오기
    playlists = sp.current_user_playlists(limit=10)

    # 플레이리스트 데이터 정리
    playlist_data = [
        {"name": playlist["name"], "id": playlist["id"]}
        for playlist in playlists["items"]
    ]
    return render_template(
        "home.html",
        user=user_info,
        playlists=playlist_data,
        message="안녕하세요 시작해봅시다"
    )
    
if __name__ == "__main__":
    app.run(debug=True)
