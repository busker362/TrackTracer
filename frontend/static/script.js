document.addEventListener("DOMContentLoaded", () => {
    const sideMenu = document.getElementById("side-menu");
    const openMenuButton = document.getElementById("open-menu-button");
    const closeMenuButton = document.getElementById("close-menu");

    // 메뉴 열기 (열기 버튼 클릭 시)
    if (openMenuButton) {
        openMenuButton.addEventListener("click", () => {
            sideMenu.classList.add("active");
        });
    }

    // 메뉴 외부 클릭 시 닫기
    document.addEventListener("click", (event) => {
        const isClickInsideMenu = sideMenu.contains(event.target);
        const isClickOnOpenButton = openMenuButton?.contains(event.target); // Optional chaining
        if (!isClickInsideMenu && !isClickOnOpenButton) {
            sideMenu.classList.remove("active");
        }
    });
});

// 재생목록 토글 함수
function togglePlaylist(playlistId) {
    const allPlaylists = document.querySelectorAll(".playlist-details");
    allPlaylists.forEach(div => {
        if (div.id !== `playlist-${playlistId}`) {
            div.style.display = "none";
        }
    });

    const playlistDiv = document.getElementById(`playlist-${playlistId}`);
    playlistDiv.style.display = playlistDiv.style.display === "none" || !playlistDiv.style.display
        ? "block"
        : "none";
}
