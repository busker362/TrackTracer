from flask import Flask, render_template, request, redirect, jsonify
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API 인증 설정
with open("config.json") as f:
    config = json.load(f)

CLIENT_ID = config["client_id"]
CLIENT_SECRET = config["client_secret"]
REDIRECT_URI = "http://127.0.0.1:5000/callback"

# SpotifyOAuth 객체 생성
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-read-private"
)

# Flask 애플리케이션 초기화
app = Flask(__name__)
    
# @app.route("/")
# def home():
#     return render_template("home.html", user=None, playlists=[])

@app.route("/")
def home():
    message = "안녕하세요 시작해봅시다"
    return render_template("home.html", user=None, playlists=[], message=message)


if __name__ == "__main__":
    app.run(debug=True)
