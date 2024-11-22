function togglePlaylist(playlistId) {
    const playlistDiv = document.getElementById(`playlist-${playlistId}`);
    if (playlistDiv.style.display === "none") {
        playlistDiv.style.display = "block"; // 펼치기
    } else {
        playlistDiv.style.display = "none"; // 숨기기
    }
}
