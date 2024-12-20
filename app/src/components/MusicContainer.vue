<template>
    <main class="music-container">
      <div class="content-wrapper">
        <h3 class="album-name">Album_Name</h3>
        <div class="vinyl-image"></div>
        <div id="music-info" class="music-info">
          <div id="track-rank" class="track-rank">1st</div>
          <div class="track-details">
            <h1 id="track-title" class="track-title">Music_Name</h1>
            <p id="artist-name" class="artist-name">Artists_Name</p>
          </div>
          <div class="progress-container">
            <div class="time-display-container">
              <span id="current-time" class="time-display">0:00</span>
              <span id="total-time" class="time-display">3:45</span>
            </div>
            <div class="progress-bar">
              <div id="progress" class="progress"></div>
            </div>
          </div>
          <div class="controls">
            <button id="prev-music" class="prev-music">Prev<br />Music</button>
            <button id="play-pause" class="play-pause">&#9658;</button>
            <button id="next-music" class="next-music">Next<br />Music</button>
          </div>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    name: "MusicContainer",
  };
  </script>
  
  <style scoped>
  .music-container {
    padding: 20px;
  }
  </style>
  