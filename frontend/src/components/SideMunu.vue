<template>
    <div id="side-menu" class="side-menu">
      <template v-if="user">
        <div class="namebackground">
          <img src="@/assets/images/SpotifyLogo.png" alt="Spotify Logo" />
          <h2>{{ user.displayName }}</h2>
        </div>
        <a href="/logout" class="logout-btn">Logout</a>
      </template>
      <template v-else>
        <button class="loginbtn" @click="loginWithSpotify">Login with Spotify</button>
      </template>
    </div>
  </template>
  
  <script>
  export default {
    name: "SideMenu",
    props: {
      user: Object,
    },
    methods: {
      loginWithSpotify() {
        window.location.href = "/login";
      },
    },
  };
  </script>
  
  <style scoped>
  .side-menu {
    background-color: #444;
    color: #fff;
    padding: 20px;
  }
  </style>
  