function togglePlaylist(playlistId) {
    const playlistDiv = document.getElementById(`playlist-${playlistId}`);
    if (playlistDiv.style.display === "none") {
        playlistDiv.style.display = "block"; // 펼치기
    } else {
        playlistDiv.style.display = "none"; // 숨기기
    }
}
// API동작 테스트 
// async function testAPI(api) {
//     const response = await fetch(`/test/${api}`);
//     const result = await response.json();
//     if (result.success) {
//         alert(`${api} Test Success: ${api === 'youtube' ? 'Video Title: ' + result.video_title : 'Artist Info: ' + result.artist_info}`);
//     } else {
//         alert(`${api} Test Failed: ${result.error}`);
//     }
// }

