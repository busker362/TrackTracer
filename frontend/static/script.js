document.getElementById("open-menu-button").addEventListener("click", () => {
    document.getElementById("side-menu").classList.add("active");
});

document.getElementById("close-menu").addEventListener("click", () => {
    document.getElementById("side-menu").classList.remove("active");
});

function togglePlaylist(playlistId) {
    const playlistDiv = document.getElementById(`playlist-${playlistId}`);
    if (playlistDiv.style.display === "none" || !playlistDiv.style.display) {
        playlistDiv.style.display = "block"; // 펼치기
    } else {
        playlistDiv.style.display = "none"; // 숨기기
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const sideMenu = document.getElementById("side-menu");
    const openMenuButton = document.getElementById("open-menu-button");
    const closeMenuButton = document.getElementById("close-menu");

    // 메뉴 열기
    openMenuButton.addEventListener("click", () => {
        sideMenu.classList.add("active");
    });

    // 메뉴 닫기 (닫기 버튼 클릭 시)
    closeMenuButton.addEventListener("click", () => {
        sideMenu.classList.remove("active");
    });

    // 메뉴 외부 클릭 시 닫기
    document.addEventListener("click", (event) => {
        const isClickInsideMenu = sideMenu.contains(event.target);
        const isClickOnOpenButton = openMenuButton.contains(event.target);

        if (!isClickInsideMenu && !isClickOnOpenButton) {
            sideMenu.classList.remove("active");
        }
    });
});
