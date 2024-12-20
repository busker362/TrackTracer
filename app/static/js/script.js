document.addEventListener("DOMContentLoaded", async () => {
    const sideMenu = document.getElementById("side-menu");
    const openMenuButton = document.getElementById("open-menu-button");
    const closeMenuButton = document.getElementById("close-menu");

    const vinylImage = document.querySelector(".vinyl-image"); // LP 디스크
    const progressBar = document.getElementById("progress");
    const currentTimeDisplay = document.getElementById("current-time");
    const totalTimeDisplay = document.getElementById("total-time");
    const playPauseButton = document.getElementById("play-pause");

    const trackRank = document.getElementById("track-rank");
    const trackTitle = document.getElementById("track-title");
    const artistName = document.getElementById("artist-name");
    const prevButton = document.getElementById("prev-music");
    const nextButton = document.getElementById("next-music");

    let tracks = [];
    let currentIndex = 0;

    let isPlaying = false;
    let currentTime = 0;
    const totalTime = 225; // 음악 총 길이 (초 단위)
    let progressInterval;

    let currentRotation = 0; // LP 디스크의 현재 회전 각도
    let rotationInterval; // LP 디스크 회전 애니메이션 간격

    // Tracks 데이터를 가져오기
    async function fetchTracks() {
        try {
            const response = await fetch("/api/tracks");
            tracks = await response.json();
            updateUI();
        } catch (error) {
            console.error("Failed to fetch tracks:", error);
        }
    }

    function getOrdinalNumber(rank) {
        const suffixes = ["th", "st", "nd", "rd"];
        const value = rank % 100; // 마지막 두 자리 숫자
        const suffix = suffixes[(value - 20) % 10] || suffixes[value] || suffixes[0];
        return rank + suffix;
    }

    // UI 업데이트 함수
    function updateUI() {
        if (tracks.length === 0) return;

        const currentTrack = tracks[currentIndex];
        trackRank.textContent = getOrdinalNumber(currentTrack.rank); // 서수로 변환
        trackTitle.textContent = currentTrack.name;
        artistName.textContent = currentTrack.artists;

        // 버튼 활성화/비활성화
        prevButton.disabled = currentIndex === 0;
        nextButton.disabled = currentIndex === tracks.length - 1;

        // 진행 바 및 시간 초기화
        currentTime = 0;
        progressBar.style.width = "0%";
        currentTimeDisplay.textContent = formatTime(currentTime);
        totalTimeDisplay.textContent = formatTime(totalTime);
    }

    // 시간 형식 변환
    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${minutes}:${secs < 10 ? "0" : ""}${secs}`;
    }

    // 진행 바 업데이트
    function updateProgress() {
        currentTime++;
        if (currentTime >= totalTime) {
            currentTime = totalTime;
            clearInterval(progressInterval);
            clearInterval(rotationInterval); // LP 디스크 회전 멈춤
            isPlaying = false;
            playPauseButton.innerHTML = "&#9658;"; // 재생 아이콘
        }
        const progressPercent = (currentTime / totalTime) * 100;
        progressBar.style.width = `${progressPercent}%`;
        currentTimeDisplay.textContent = formatTime(currentTime);
    }

    // LP 디스크 회전 제어
    function startRotation() {
        rotationInterval = setInterval(() => {
            currentRotation = (currentRotation + 1) % 360; // 각도 업데이트 (0 ~ 359도)
            vinylImage.style.transform = `translate(-20%, -50%) rotate(${currentRotation}deg)`;
        }, 100); // 100ms마다 1도 회전
    }

    function stopRotation() {
        clearInterval(rotationInterval); // 회전 멈춤
    }

    // Play/Pause 버튼 클릭 이벤트
    playPauseButton.addEventListener("click", () => {
        if (isPlaying) {
            clearInterval(progressInterval);
            stopRotation(); // LP 디스크 회전 멈춤
            playPauseButton.innerHTML = "&#9658;"; // 재생 아이콘
        } else {
            progressInterval = setInterval(updateProgress, 1000); // 매초 업데이트
            startRotation(); // LP 디스크 회전 시작
            playPauseButton.innerHTML = "&#10074;&#10074;"; // 일시 정지 아이콘
        }
        isPlaying = !isPlaying;
    });

    // 이전 곡으로 이동
    prevButton.addEventListener("click", () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateUI();
        }
    });

    // 다음 곡으로 이동
    nextButton.addEventListener("click", () => {
        if (currentIndex < tracks.length - 1) {
            currentIndex++;
            updateUI();
        }
    });

    // 초기 값 설정
    totalTimeDisplay.textContent = formatTime(totalTime);

    // 초기 데이터 가져오기
    await fetchTracks();
});
